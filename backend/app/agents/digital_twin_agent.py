"""
digital_twin_agent.py

Enterprise Healthcare Digital Twin Agent

Features
--------
✓ LangChain v0.3+
✓ Agentic AI
✓ Tool Calling
✓ RAG
✓ Chroma Integration
✓ Loguru Logging
✓ Structured Output
"""

from typing import List, Optional

from app.config.settings import settings
logger = settings.get_logger()

from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI

from app.prompts.patient_prompt import PatientPrompt


class DigitalTwinAgent:
    """
    Enterprise Healthcare Digital Twin Agent
    """

    def __init__(
        self,
        llm: ChatOpenAI,
        tools: Optional[List[BaseTool]] = None,
    ):

        logger.info("Initializing Digital Twin Agent")

        self.llm = llm
        self.tools = tools or []

        logger.info(
            "Loaded {} tool(s)",
            len(self.tools),
        )

        self.prompt = PatientPrompt.get_prompt()

        self.agent = create_tool_calling_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=self.prompt,
        )

        self.executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True,
            return_intermediate_steps=True,
            handle_parsing_errors=True,
        )

        logger.success("Digital Twin Agent Initialized")

    # ==========================================================
    # Patient Analysis
    # ==========================================================

    def analyze_patient(
        self,
        patient_data: dict,
        question: str,
    ):

        logger.info("Analyzing Patient")

        try:

            response = self.executor.invoke(
                {
                    "patient_data": patient_data,
                    "question": question,
                }
            )

            logger.success("Patient Analysis Completed")

            return response

        except Exception as ex:

            logger.exception(ex)
            raise

    # ==========================================================
    # Generic Chat
    # ==========================================================

    def chat(
        self,
        question: str,
    ):

        logger.info("Agent Chat Started")

        try:

            response = self.llm.invoke(
                [
                    HumanMessage(content=question)
                ]
            )

            logger.success("Chat Completed")

            return response.content

        except Exception as ex:

            logger.exception(ex)
            raise

    # ==========================================================
    # Simulation
    # ==========================================================

    def simulate(
        self,
        patient_data: dict,
        scenario: str,
        days: int = 30,
    ):

        logger.info("Running Simulation")

        try:

            response = self.executor.invoke(
                {
                    "patient_data": patient_data,
                    "question": (
                        f"Simulate the following scenario for "
                        f"{days} days: {scenario}"
                    ),
                }
            )

            logger.success("Simulation Completed")

            return response

        except Exception as ex:

            logger.exception(ex)
            raise

    # ==========================================================
    # Forecast
    # ==========================================================

    def forecast(
        self,
        patient_data: dict,
        forecast_days: int,
    ):

        logger.info("Running Forecast")

        try:

            response = self.executor.invoke(
                {
                    "patient_data": patient_data,
                    "question": (
                        f"Forecast patient outcome for "
                        f"{forecast_days} days."
                    ),
                }
            )

            logger.success("Forecast Completed")

            return response

        except Exception as ex:

            logger.exception(ex)
            raise

    # ==========================================================
    # Risk Analysis
    # ==========================================================

    def risk_analysis(
        self,
        patient_data: dict,
    ):

        logger.info("Running Risk Analysis")

        try:

            response = self.executor.invoke(
                {
                    "patient_data": patient_data,
                    "question": (
                        "Perform complete clinical risk analysis."
                    ),
                }
            )

            logger.success("Risk Analysis Completed")

            return response

        except Exception as ex:

            logger.exception(ex)
            raise

    # ==========================================================
    # Recommendations
    # ==========================================================

    def recommend(
        self,
        patient_data: dict,
    ):

        logger.info("Generating Recommendations")

        try:

            response = self.executor.invoke(
                {
                    "patient_data": patient_data,
                    "question": (
                        "Provide evidence-based treatment "
                        "recommendations."
                    ),
                }
            )

            logger.success("Recommendations Generated")

            return response

        except Exception as ex:

            logger.exception(ex)
            raise

    # ==========================================================
    # RAG Question Answering
    # ==========================================================

    def ask_with_context(
        self,
        question: str,
        retrieved_context: str,
    ):

        logger.info("Running RAG Question Answering")

        prompt = f"""
Context

{retrieved_context}

Question

{question}
"""

        try:

            response = self.llm.invoke(
                [
                    HumanMessage(content=prompt)
                ]
            )

            logger.success("RAG Completed")

            return response.content

        except Exception as ex:

            logger.exception(ex)
            raise