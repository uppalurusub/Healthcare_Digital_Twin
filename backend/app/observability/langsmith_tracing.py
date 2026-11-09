"""
LangSmith tracing and LLM token/cost accounting for ChatOpenAI/OpenRouter.

Costs use provider-reported values when available. If OpenRouter doesn't expose
cost on the response, optional per-million token rates can be configured via env.
"""
from __future__ import annotations

import os
from typing import Any

from langchain_core.callbacks import BaseCallbackHandler
from langsmith import Client


def configure_langsmith() -> None:
    """Enable LangSmith tracing using environment configuration."""
    os.environ.setdefault("LANGSMITH_TRACING", "true")
    os.environ.setdefault(
        "LANGSMITH_PROJECT",
        os.getenv("LANGCHAIN_PROJECT", "Healthcare_Digital_Twin_Interface"),
    )
    # Backward compatibility with LangChain's legacy env variable names.
    if os.getenv("LANGSMITH_API_KEY") and not os.getenv("LANGCHAIN_API_KEY"):
        os.environ["LANGCHAIN_API_KEY"] = os.environ["LANGSMITH_API_KEY"]
    if os.getenv("LANGSMITH_PROJECT") and not os.getenv("LANGCHAIN_PROJECT"):
        os.environ["LANGCHAIN_PROJECT"] = os.environ["LANGSMITH_PROJECT"]


def _number(value: Any) -> float | None:
    try:
        if value is None:
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


class LangSmithUsageCostCallback(BaseCallbackHandler):
    """Capture usage at the actual LLM response and enrich its LangSmith run."""

    def __init__(self, model_name: str | None = None):
        self.model_name = model_name or os.getenv("model", "unknown")
        self.client = None
        try:
            self.client = Client()
        except Exception:
            # LangChain's normal tracer can still record the run.
            pass

    def on_llm_end(self, response, *, run_id, parent_run_id=None, tags=None,
                   metadata=None, **kwargs):
        llm_output = getattr(response, "llm_output", None) or {}
        generations = getattr(response, "generations", []) or []
        message = None
        if generations and generations[0]:
            message = getattr(generations[0][0], "message", None)

        usage = {}
        if message is not None:
            usage = getattr(message, "usage_metadata", None) or {}
            response_metadata = getattr(message, "response_metadata", None) or {}
            provider_usage = (
                response_metadata.get("token_usage")
                or response_metadata.get("usage")
                or {}
            )
            usage = {**response_metadata, **provider_usage, **usage}
        token_usage = llm_output.get("token_usage") or llm_output.get("usage") or {}
        usage = {**token_usage, **usage}

        prompt_tokens = _number(
            usage.get("input_tokens", usage.get("prompt_tokens",
            usage.get("promptTokens", token_usage.get("prompt_tokens"))))
        )
        completion_tokens = _number(
            usage.get("output_tokens", usage.get("completion_tokens",
            usage.get("completionTokens", token_usage.get("completion_tokens"))))
        )
        total_tokens = _number(
            usage.get("total_tokens", usage.get("totalTokens",
            token_usage.get("total_tokens")))
        )
        if total_tokens is None and prompt_tokens is not None and completion_tokens is not None:
            total_tokens = prompt_tokens + completion_tokens

        # Providers may report a direct cost. Otherwise use optional configured rates.
        direct_cost = _number(
            usage.get("total_cost", usage.get("cost",
            usage.get("total_cost_usd", token_usage.get("total_cost"))))
        )
        input_rate = _number(os.getenv("OPENROUTER_INPUT_COST_PER_1M"))
        output_rate = _number(os.getenv("OPENROUTER_OUTPUT_COST_PER_1M"))
        input_cost = _number(usage.get("prompt_cost", usage.get("input_cost")))
        output_cost = _number(usage.get("completion_cost", usage.get("output_cost")))

        if input_cost is None and prompt_tokens is not None and input_rate is not None:
            input_cost = prompt_tokens * input_rate / 1_000_000
        if output_cost is None and completion_tokens is not None and output_rate is not None:
            output_cost = completion_tokens * output_rate / 1_000_000
        total_cost = direct_cost
        if total_cost is None and input_cost is not None and output_cost is not None:
            total_cost = input_cost + output_cost

        extra = {
            "usage_source": "provider_response" if token_usage or usage else "unavailable",
            "model_name": self.model_name,
            "input_tokens": prompt_tokens,
            "output_tokens": completion_tokens,
            "total_tokens": total_tokens,
            "input_cost_usd": input_cost,
            "output_cost_usd": output_cost,
            "total_cost_usd": total_cost,
        }
        try:
            if self.client is not None:
                update = {"run_id": run_id, "extra": {"usage_cost": extra}}
                if prompt_tokens is not None:
                    update["prompt_tokens"] = int(prompt_tokens)
                if completion_tokens is not None:
                    update["completion_tokens"] = int(completion_tokens)
                if total_tokens is not None:
                    update["total_tokens"] = int(total_tokens)
                if input_cost is not None:
                    update["prompt_cost"] = input_cost
                if output_cost is not None:
                    update["completion_cost"] = output_cost
                if total_cost is not None:
                    update["total_cost"] = total_cost
                self.client.update_run(**update)
        except Exception:
            # Do not fail a clinical/digital-twin request because telemetry failed.
            pass
