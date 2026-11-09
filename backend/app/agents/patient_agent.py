"""
patient_agent.py

Enterprise Patient Digital Twin Agent
"""

from __future__ import annotations

from typing import List, Optional

from app.config.settings import settings
logger = settings.get_logger()

from langchain_classic.agents import (
    AgentExecutor,
    create_tool_calling_agent
)
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI

from app.prompts.patient_prompt import PatientPrompt


class PatientAgent:
    """
    Enterprise Patient Digital Twin Agent
    """

    def __init__(
        self,
        llm: ChatOpenAI,
        tools: Optional[List[BaseTool]] = None,
    ):

        logger.info("Initializing Patient Agent")

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
            handle_parsing_errors=True,
            return_intermediate_steps=True,
        )

        logger.success("Patient Agent Initialized")

    # =====================================================
    # Generic Analysis
    # =====================================================

    def analyze(
        self,
        patient_data: dict,
        question: str,
    ) -> dict:

        logger.info("Starting patient analysis")

        try:

            response = self.executor.invoke(
                {
                    "patient_data": patient_data,
                    "question": question,
                }
            )

            logger.success("Patient analysis completed")

            return response

        except Exception as ex:

            logger.exception(ex)
            raise

    # =====================================================
    # Clinical Summary
    # =====================================================

    def clinical_summary(
        self,
        patient_data: dict,
    ) -> dict:

        logger.info("Generating clinical summary")

        return self.analyze(
            patient_data,
            "Generate a comprehensive clinical summary."
        )

    # =====================================================
    # Disease Risk
    # =====================================================

    def disease_risk(
        self,
        patient_data: dict,
    ) -> dict:

        logger.info("Calculating disease risk")

        return self.analyze(
            patient_data,
            """
            Assess disease risks.

            Include:

            • Cardiovascular Risk
            • Diabetes Risk
            • Stroke Risk
            • Kidney Disease Risk
            • Overall Health Score
            """
        )

    # =====================================================
    # Readmission
    # =====================================================

    def readmission_risk(
        self,
        patient_data: dict,
    ) -> dict:

        logger.info("Estimating readmission risk")

        return self.analyze(
            patient_data,
            """
            Predict hospital readmission probability.

            Explain the reasoning and
            provide preventive recommendations.
            """
        )

    # =====================================================
    # Mortality
    # =====================================================

    def mortality_prediction(
        self,
        patient_data: dict,
    ) -> dict:

        logger.info("Predicting mortality risk")

        return self.analyze(
            patient_data,
            """
            Predict mortality probability.

            Include:

            • Confidence
            • Clinical Factors
            • Explanation
            """
        )

    # =====================================================
    # Medication Review
    # =====================================================

    def medication_review(
        self,
        patient_data: dict,
    ) -> dict:

        logger.info("Reviewing medications")

        return self.analyze(
            patient_data,
            """
            Review current medications.

            Detect:

            • Drug interactions
            • Contraindications
            • Missing medications
            • Safer alternatives
            """
        )

    # =====================================================
    # Lifestyle Recommendation
    # =====================================================

    def lifestyle_recommendations(
        self,
        patient_data: dict,
    ) -> dict:

        logger.info("Generating lifestyle recommendations")

        return self.analyze(
            patient_data,
            """
            Recommend:

            • Diet
            • Exercise
            • Sleep
            • Smoking Cessation
            • Alcohol Reduction
            • Preventive Care
            """
        )

    # =====================================================
    # Follow-up Plan
    # =====================================================

    def followup_plan(
        self,
        patient_data: dict,
    ) -> dict:

        logger.info("Generating follow-up plan")

        return self.analyze(
            patient_data,
            """
            Create a 30-day follow-up plan.

            Include:

            • Investigations
            • Monitoring
            • Medication
            • Consultations
            """
        )

    # =====================================================
    # What-if Simulation
    # =====================================================

    def what_if(
        self,
        patient_data: dict,
        scenario: str,
    ) -> dict:

        logger.info(
            "Running What-If Simulation: {}",
            scenario,
        )

        return self.analyze(
            patient_data,
            f"""
            Perform a What-If analysis.

            Scenario:

            {scenario}

            Predict the outcome,
            associated risks,
            and recommended actions.
            """
        )

    # =====================================================
    # Forecast
    # =====================================================

    def forecast(
        self,
        patient_data: dict,
        days: int = 30,
    ) -> dict:

        logger.info(
            "Forecasting next {} days",
            days,
        )

        return self.analyze(
            patient_data,
            f"""
            Forecast patient health
            for the next {days} days.

            Predict:

            • Disease progression
            • Readmission
            • Mortality
            • Medication effectiveness
            """
        )

    # =====================================================
    # Explain Prediction
    # =====================================================

    def explain(
        self,
        patient_data: dict,
    ) -> dict:

        logger.info("Generating explainability report")

        return self.analyze(
            patient_data,
            """
            Explain every prediction.

            Include:

            • Clinical reasoning
            • Risk factors
            • Confidence
            • Recommendations
            """
        )