"""
trial_agent.py

Enterprise Clinical Trial Digital Twin Agent
"""

from __future__ import annotations

from typing import List, Optional

from app.config.settings import settings
logger = settings.get_logger()

from langchain_classic.agents import (
    AgentExecutor,
    create_tool_calling_agent,
)
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI

from app.prompts.patient_prompt import PatientPrompt


class TrialAgent:
    """
    Enterprise Clinical Trial Digital Twin Agent
    """

    def __init__(
        self,
        llm: ChatOpenAI,
        tools: Optional[List[BaseTool]] = None,
    ) -> None:

        logger.info("Initializing Trial Agent")

        self.llm = llm
        self.tools = tools or []

        logger.info(
            "Loaded {} tool(s)",
            len(self.tools),
        )

        # Reuse the existing prompt structure.
        # You can later replace this with trial_prompt.py.
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
            handle_parsing_errors=True,
            return_intermediate_steps=True,
        )

        logger.success("Trial Agent Initialized")

    # =====================================================
    # Generic Analysis
    # =====================================================

    def analyze(
        self,
        trial_data: dict,
        question: str,
    ) -> dict:

        logger.info("Analyzing Clinical Trial")

        try:

            response = self.executor.invoke(
                {
                    "patient_data": trial_data,
                    "question": question,
                }
            )

            logger.success("Clinical Trial Analysis Completed")

            return response

        except Exception as ex:

            logger.exception(ex)
            raise

    # =====================================================
    # Trial Summary
    # =====================================================

    def summary(
        self,
        trial_data: dict,
    ) -> dict:

        logger.info("Generating Trial Summary")

        return self.analyze(
            trial_data,
            "Generate a comprehensive clinical trial summary."
        )

    # =====================================================
    # Enrollment Forecast
    # =====================================================

    def enrollment_forecast(
        self,
        trial_data: dict,
        forecast_days: int = 90,
    ) -> dict:

        logger.info(
            "Forecasting Enrollment for {} days",
            forecast_days,
        )

        return self.analyze(
            trial_data,
            f"""
Forecast subject enrollment
for the next {forecast_days} days.

Include

• Expected Enrollment
• Enrollment Trend
• Site Contribution
• Risk Factors
"""
        )

    # =====================================================
    # Dropout Prediction
    # =====================================================

    def dropout_prediction(
        self,
        trial_data: dict,
    ) -> dict:

        logger.info("Predicting Dropout Risk")

        return self.analyze(
            trial_data,
            """
Predict participant dropout.

Include

• Dropout Probability
• Contributing Factors
• High-Risk Sites
• Recommended Actions
"""
        )

    # =====================================================
    # Protocol Compliance
    # =====================================================

    def protocol_compliance(
        self,
        trial_data: dict,
    ) -> dict:

        logger.info("Analyzing Protocol Compliance")

        return self.analyze(
            trial_data,
            """
Evaluate protocol compliance.

Include

• Major Deviations
• Minor Deviations
• Compliance Score
• Corrective Actions
"""
        )

    # =====================================================
    # Safety Analysis
    # =====================================================

    def safety_analysis(
        self,
        trial_data: dict,
    ) -> dict:

        logger.info("Running Safety Analysis")

        return self.analyze(
            trial_data,
            """
Analyze trial safety.

Include

• Serious Adverse Events
• Adverse Events
• Safety Signals
• Risk Assessment
"""
        )

    # =====================================================
    # Site Performance
    # =====================================================

    def site_performance(
        self,
        trial_data: dict,
    ) -> dict:

        logger.info("Evaluating Site Performance")

        return self.analyze(
            trial_data,
            """
Evaluate all study sites.

Return

• Recruitment Score
• Monitoring Score
• Query Resolution
• Data Quality
• Overall Site Ranking
"""
        )

    # =====================================================
    # Budget Forecast
    # =====================================================

    def budget_forecast(
        self,
        trial_data: dict,
    ) -> dict:

        logger.info("Forecasting Trial Budget")

        return self.analyze(
            trial_data,
            """
Forecast trial budget.

Include

• Current Spend
• Forecast Spend
• Cost Drivers
• Budget Variance
"""
        )

    # =====================================================
    # What-If Simulation
    # =====================================================

    def what_if(
        self,
        trial_data: dict,
        scenario: str,
    ) -> dict:

        logger.info(
            "Running Trial What-If Simulation: {}",
            scenario,
        )

        return self.analyze(
            trial_data,
            f"""
Perform a Clinical Trial
What-If Simulation.

Scenario

{scenario}

Return

• Expected Impact
• Timeline
• Budget Impact
• Risks
• Recommendations
"""
        )

    # =====================================================
    # Optimization
    # =====================================================

    def optimize(
        self,
        trial_data: dict,
    ) -> dict:

        logger.info("Optimizing Clinical Trial")

        return self.analyze(
            trial_data,
            """
Optimize trial execution.

Recommend

• Enrollment Strategy
• Site Allocation
• Monitoring Strategy
• Budget Optimization
• Timeline Reduction
"""
        )

    # =====================================================
    # Explainability
    # =====================================================

    def explain(
        self,
        trial_data: dict,
    ) -> dict:

        logger.info("Generating Trial Explainability")

        return self.analyze(
            trial_data,
            """
Explain all predictions.

Include

• Clinical Reasoning
• Statistical Factors
• Confidence
• Recommendations
"""
        )