"""
hospital_prompt.py

Enterprise Hospital Digital Twin Prompt

Features
--------
✓ Hospital Digital Twin
✓ Capacity Planning
✓ Workforce Planning
✓ Resource Optimization
✓ Emergency Simulation
✓ Financial Forecasting
✓ Explainable AI
"""

from app.config.settings import settings
logger = settings.get_logger()

from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder


class HospitalPrompt:
    """
    Hospital Digital Twin Prompt Builder
    """

    def __init__(self):

        logger.info("Initializing Hospital Prompt")

    # ==========================================================
    # System Prompt
    # ==========================================================

    @staticmethod
    def get_system_prompt() -> str:

        logger.debug("Loading System Prompt")

        return """
You are an Enterprise AI Hospital Digital Twin Assistant.

Your expertise includes:

• Hospital Operations
• Capacity Planning
• Bed Occupancy
• ICU Planning
• Emergency Planning
• Workforce Optimization
• Resource Utilization
• Financial Planning
• Predictive Analytics
• Explainable AI

Always:

• Think step by step.
• Be evidence based.
• Explain every prediction.
• Never fabricate hospital information.
• Mention uncertainty when appropriate.
"""

    # ==========================================================
    # Human Prompt
    # ==========================================================

    @staticmethod
    def get_human_prompt() -> str:

        logger.debug("Loading Human Prompt")

        return """
Hospital Information

{hospital_data}

Question

{question}
"""

    # ==========================================================
    # Chat Prompt
    # ==========================================================

    @classmethod
    def get_prompt(cls):

        logger.info(
            "Creating Hospital Chat Prompt"
        )

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
    # Hospital Summary
    # ==========================================================

    @staticmethod
    def summary_prompt() -> str:

        logger.debug(
            "Loading Hospital Summary Prompt"
        )

        return """
Analyze the hospital.

Provide

• Executive Summary
• Hospital Profile
• Strengths
• Weaknesses
• Opportunities
• Recommendations
"""

    # ==========================================================
    # Capacity Planning
    # ==========================================================

    @staticmethod
    def capacity_prompt() -> str:

        logger.debug(
            "Loading Capacity Planning Prompt"
        )

        return """
Develop a hospital capacity plan.

Include

• General Beds
• ICU Beds
• Emergency Beds
• Operation Theatres
• Future Capacity
"""

    # ==========================================================
    # Bed Occupancy
    # ==========================================================

    @staticmethod
    def occupancy_prompt() -> str:

        logger.debug(
            "Loading Occupancy Prompt"
        )

        return """
Forecast hospital occupancy.

Predict

• Bed Occupancy
• ICU Occupancy
• Seasonal Trends
• High Demand Periods
"""

    # ==========================================================
    # Workforce Planning
    # ==========================================================

    @staticmethod
    def workforce_prompt() -> str:

        logger.debug(
            "Loading Workforce Prompt"
        )

        return """
Optimize workforce.

Include

• Doctors
• Nurses
• Specialists
• Support Staff

Recommend staffing levels.
"""

    # ==========================================================
    # Resource Optimization
    # ==========================================================

    @staticmethod
    def resource_prompt() -> str:

        logger.debug(
            "Loading Resource Prompt"
        )

        return """
Optimize hospital resources.

Analyze

• Equipment
• ICU
• Beds
• Laboratory
• Pharmacy
• Radiology
"""

    # ==========================================================
    # Patient Flow
    # ==========================================================

    @staticmethod
    def patient_flow_prompt() -> str:

        logger.debug(
            "Loading Patient Flow Prompt"
        )

        return """
Analyze patient flow.

Include

• Admissions
• Transfers
• Waiting Time
• Discharges
• Bottlenecks
"""

    # ==========================================================
    # Financial Forecast
    # ==========================================================

    @staticmethod
    def financial_prompt() -> str:

        logger.debug(
            "Loading Financial Prompt"
        )

        return """
Forecast hospital finances.

Include

• Revenue
• Cost
• Profit
• Budget
• Operational Expenses
"""

    # ==========================================================
    # Emergency Simulation
    # ==========================================================

    @staticmethod
    def emergency_prompt() -> str:

        logger.debug(
            "Loading Emergency Prompt"
        )

        return """
Run emergency simulation.

Scenario

{scenario}

Predict

• Bed Demand
• ICU Demand
• Staff Requirement
• Equipment Requirement
"""

    # ==========================================================
    # What-if Analysis
    # ==========================================================

    @staticmethod
    def what_if_prompt() -> str:

        logger.debug(
            "Loading What-if Prompt"
        )

        return """
Perform What-if Analysis.

Scenario

{scenario}

Return

• Current State
• Simulated State
• Operational Impact
• Financial Impact
• Recommendations
"""

    # ==========================================================
    # Explainability
    # ==========================================================

    @staticmethod
    def explain_prompt() -> str:

        logger.debug(
            "Loading Explainability Prompt"
        )

        return """
Explain every prediction.

Include

• Reasoning
• Important Factors
• Confidence
• Recommendations
"""

    # ==========================================================
    # JSON Output
    # ==========================================================

    @staticmethod
    def json_prompt() -> str:

        logger.debug(
            "Loading JSON Prompt"
        )

        return """
Return ONLY valid JSON.

{
    "summary": "",
    "bed_occupancy": 0,
    "icu_occupancy": 0,
    "resource_utilization": 0,
    "financial_score": 0,
    "capacity_score": 0,
    "recommendations": [],
    "confidence": 0,
    "explanation": ""
}
"""