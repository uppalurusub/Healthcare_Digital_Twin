"""
simulation_prompt.py

Purpose:
    Prompt templates for Healthcare Digital Twin Simulation Engine

Author:
    Healthcare Digital Twin Platform
"""

from app.config.settings import settings
logger = settings.get_logger()

from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder


class SimulationPrompt:
    """
    Prompt Builder for Digital Twin Simulation
    """

    def __init__(self):
        logger.info("Initializing SimulationPrompt...")

    # ==========================================================
    # System Prompt
    # ==========================================================

    @staticmethod
    def get_system_prompt() -> str:
        logger.debug("Loading Simulation System Prompt")

        return """
You are an AI-powered Healthcare Digital Twin Simulation Expert.

Your responsibilities are:

1. Simulate patient disease progression.
2. Simulate medication effectiveness.
3. Predict clinical outcomes.
4. Estimate hospitalization probability.
5. Forecast ICU admission risk.
6. Simulate resource utilization.
7. Analyze treatment alternatives.
8. Explain every prediction.
9. Never fabricate clinical facts.
10. Mention uncertainty when appropriate.

Always provide medically meaningful reasoning.
"""

    # ==========================================================
    # Human Prompt
    # ==========================================================

    @staticmethod
    def get_human_prompt() -> str:
        logger.debug("Loading Simulation Human Prompt")

        return """
Patient Information

{patient_data}

Simulation Scenario

{scenario}

Simulation Duration

{simulation_days} days
"""

    # ==========================================================
    # Chat Prompt
    # ==========================================================

    @classmethod
    def get_prompt(cls) -> ChatPromptTemplate:
        logger.info("Creating Simulation ChatPromptTemplate")

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

    # ==========================================================
    # Disease Progression
    # ==========================================================

    @staticmethod
    def disease_progression_prompt() -> str:
        logger.debug("Loading Disease Progression Prompt")

        return """
Simulate disease progression.

Patient

{patient_data}

Duration

{simulation_days} days

Return

• Current Stage
• Expected Stage
• Disease Progression
• Confidence Score
• Clinical Explanation
"""

    # ==========================================================
    # Medication Simulation
    # ==========================================================

    @staticmethod
    def medication_simulation_prompt() -> str:
        logger.debug("Loading Medication Simulation Prompt")

        return """
Evaluate medication effectiveness.

Patient

{patient_data}

Current Medications

{medications}

Simulate

• Medication Response
• Expected Improvement
• Side Effects
• Drug Interactions
• Medication Adherence
"""

    # ==========================================================
    # Vital Signs Simulation
    # ==========================================================

    @staticmethod
    def vital_signs_prompt() -> str:
        logger.debug("Loading Vital Signs Simulation Prompt")

        return """
Predict future vital signs.

Patient

{patient_data}

Predict

• Blood Pressure
• Heart Rate
• Respiratory Rate
• Oxygen Saturation
• Temperature

Duration

{simulation_days} days
"""

    # ==========================================================
    # Readmission Simulation
    # ==========================================================

    @staticmethod
    def readmission_prompt() -> str:
        logger.debug("Loading Readmission Simulation Prompt")

        return """
Estimate hospital readmission.

Patient

{patient_data}

Return

• Readmission Probability
• Reasons
• Risk Factors
• Preventive Measures
"""

    # ==========================================================
    # Mortality Simulation
    # ==========================================================

    @staticmethod
    def mortality_prompt() -> str:
        logger.debug("Loading Mortality Prompt")

        return """
Estimate mortality risk.

Patient

{patient_data}

Return

• Mortality Probability
• Clinical Risk Factors
• Explanation
"""

    # ==========================================================
    # What-If Analysis
    # ==========================================================

    @staticmethod
    def what_if_prompt() -> str:
        logger.debug("Loading What-If Analysis Prompt")

        return """
Perform a What-If simulation.

Patient

{patient_data}

Scenario

{scenario}

Examples

• Medication Changed
• Weight Reduced
• Blood Pressure Controlled
• Smoking Stopped
• Diabetes Controlled

Return

• Current State
• Simulated State
• Expected Improvement
• Risks
• Recommendations
"""

    # ==========================================================
    # Resource Utilization
    # ==========================================================

    @staticmethod
    def hospital_resource_prompt() -> str:
        logger.debug("Loading Hospital Resource Prompt")

        return """
Hospital Digital Twin

Hospital Information

{hospital_data}

Predict

• Bed Occupancy
• ICU Occupancy
• Staff Requirement
• Equipment Usage
• Emergency Demand

Duration

{simulation_days} days
"""

    # ==========================================================
    # Clinical Trial Simulation
    # ==========================================================

    @staticmethod
    def clinical_trial_prompt() -> str:
        logger.debug("Loading Clinical Trial Simulation Prompt")

        return """
Clinical Trial Digital Twin

Trial Data

{trial_data}

Predict

• Enrollment
• Dropout Rate
• Completion Rate
• Safety Events
• Protocol Deviations

Simulation Duration

{simulation_days} days
"""

    # ==========================================================
    # Forecast Prompt
    # ==========================================================

    @staticmethod
    def forecasting_prompt() -> str:
        logger.debug("Loading Forecast Prompt")

        return """
Forecast patient outcomes.

Patient

{patient_data}

Forecast Period

{forecast_days} days

Predict

• Disease Progression
• Readmission
• Mortality
• Medication Response
• ICU Requirement
"""

    # ==========================================================
    # JSON Output
    # ==========================================================

    @staticmethod
    def json_output_prompt() -> str:
        logger.debug("Loading JSON Output Prompt")

        return """
Return ONLY valid JSON.

{
  "simulation_summary": "",
  "current_state": {},
  "predicted_state": {},
  "risk_score": 0,
  "hospitalization_probability": 0,
  "icu_probability": 0,
  "mortality_probability": 0,
  "recommendations": [],
  "confidence_score": 0,
  "explanation": ""
}
"""