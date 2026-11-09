"""
patient_prompt.py

Purpose:
    Prompt templates for Patient Digital Twin Agent

Author:
    Healthcare Digital Twin Platform
"""

from app.config.settings import settings
logger = settings.get_logger()

from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder


class PatientPrompt:
    """
    Builds prompt templates for Patient Digital Twin Agent.
    """

    def __init__(self):

        logger.info("Initializing PatientPrompt...")

    @staticmethod
    def get_system_prompt() -> str:
        """
        System Prompt
        """

        logger.debug("Loading Patient System Prompt")

        return """
You are an expert AI Healthcare Digital Twin Assistant.

Your responsibilities include:

1. Analyze patient demographics.
2. Analyze medical history.
3. Analyze laboratory results.
4. Analyze medications.
5. Identify clinical risks.
6. Predict disease progression.
7. Estimate hospitalization probability.
8. Predict readmission risk.
9. Recommend interventions.
10. Explain every recommendation.

Always:

• Think clinically.
• Use evidence-based reasoning.
• Mention uncertainty if applicable.
• Never fabricate patient information.
• Produce structured JSON output whenever possible.
"""

    @staticmethod
    def get_human_prompt() -> str:
        """
        Human Prompt
        """

        logger.debug("Loading Patient Human Prompt")

        return """
Patient Information

{patient_data}

Question

{question}
"""

    @classmethod
    def get_prompt(cls):

        logger.info("Creating Patient Chat Prompt")

        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    cls.get_system_prompt(),
                ),

                (
                    "human",
                    cls.get_human_prompt(),
                ),

                MessagesPlaceholder(
                    variable_name="agent_scratchpad"
                ),
            ]
        )

    @staticmethod
    def get_simulation_prompt() -> str:
        """
        Digital Twin Simulation Prompt
        """

        logger.debug("Loading Simulation Prompt")

        return """
You are simulating a Digital Twin for the following patient.

Patient

{patient_data}

Simulation Scenario

{scenario}

Duration

{days} days

Generate:

1. Expected disease progression
2. Expected vital signs
3. Medication effectiveness
4. Possible complications
5. Hospitalization probability
6. Mortality risk
7. Recommended interventions
"""

    @staticmethod
    def get_forecasting_prompt() -> str:
        """
        Forecast Prompt
        """

        logger.debug("Loading Forecast Prompt")

        return """
Forecast the patient's clinical condition.

Patient

{patient_data}

Forecast Duration

{forecast_days} days

Predict:

• Disease progression
• Blood pressure trend
• Heart rate trend
• Glucose trend
• Readmission probability
• ICU probability
• Mortality probability
"""

    @staticmethod
    def get_risk_analysis_prompt() -> str:
        """
        Risk Analysis Prompt
        """

        logger.debug("Loading Risk Analysis Prompt")

        return """
Analyze the following patient.

Patient

{patient_data}

Return:

• High Risk Diseases
• Clinical Risk Score
• Readmission Risk
• Mortality Risk
• Medication Risk
• Lifestyle Risk
• Overall Health Score
"""

    @staticmethod
    def get_recommendation_prompt() -> str:
        """
        Recommendation Prompt
        """

        logger.debug("Loading Recommendation Prompt")

        return """
Review the patient information.

Patient

{patient_data}

Provide recommendations for:

• Medication
• Lifestyle
• Diet
• Exercise
• Follow-up
• Additional Lab Tests
• Specialist Referral
• Preventive Care

Explain why each recommendation is important.
"""

    @staticmethod
    def get_json_output_prompt() -> str:
        """
        Structured JSON Output Prompt
        """

        logger.debug("Loading JSON Output Prompt")

        return """
Return ONLY valid JSON.

{
    "summary": "",
    "health_score": 0,
    "risk_score": 0,
    "readmission_probability": 0,
    "mortality_probability": 0,
    "predictions": [],
    "recommendations": [],
    "explanation": ""
}
"""