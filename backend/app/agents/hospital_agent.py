"""
hospital_agent.py

Enterprise Hospital Digital Twin Agent

Features
--------
✓ LangChain v0.3+
✓ Agentic AI
✓ Tool Calling
✓ Hospital Digital Twin
✓ Resource Optimization
✓ Capacity Planning
✓ What-if Simulation
✓ Forecasting
✓ Loguru Logging
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

from app.prompts.hospital_prompt import HospitalPrompt


class HospitalAgent:
    """
    Hospital Digital Twin Agent
    """

    def __init__(
        self,
        llm: ChatOpenAI,
        tools: Optional[List[BaseTool]] = None,
    ) -> None:

        logger.info("Initializing Hospital Agent")

        self.llm = llm
        self.tools = tools or []

        logger.info(
            "Loaded {} tool(s)",
            len(self.tools),
        )

        self.prompt = HospitalPrompt.get_prompt()

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

        logger.success("Hospital Agent Initialized")

    # =====================================================
    # Generic Analysis
    # =====================================================

    def analyze(
        self,
        hospital_data: dict,
        question: str,
    ) -> dict:

        logger.info("Analyzing Hospital")

        try:

            response = self.executor.invoke(
                {
                    "hospital_data": hospital_data,
                    "question": question,
                }
            )

            logger.success("Hospital Analysis Completed")

            return response

        except Exception as ex:

            logger.exception(ex)
            raise

    # =====================================================
    # Hospital Summary
    # =====================================================

    def summary(
        self,
        hospital_data: dict,
    ) -> dict:

        logger.info("Generating Hospital Summary")

        return self.analyze(
            hospital_data,
            "Generate a complete hospital operational summary."
        )

    # =====================================================
    # Bed Occupancy Forecast
    # =====================================================

    def bed_forecast(
        self,
        hospital_data: dict,
        forecast_days: int = 30,
    ) -> dict:

        logger.info(
            "Forecasting Bed Occupancy for {} days",
            forecast_days,
        )

        return self.analyze(
            hospital_data,
            f"""
Forecast hospital bed occupancy
for the next {forecast_days} days.

Include

• General Beds
• ICU Beds
• Emergency Beds
• Occupancy Trend
• Peak Demand
"""
        )

    # =====================================================
    # Resource Optimization
    # =====================================================

    def optimize_resources(
        self,
        hospital_data: dict,
    ) -> dict:

        logger.info("Optimizing Hospital Resources")

        return self.analyze(
            hospital_data,
            """
Optimize hospital resources.

Include

• Staff Allocation
• ICU Allocation
• Equipment Utilization
• Operating Rooms
• Bed Allocation
"""
        )

    # =====================================================
    # Staff Planning
    # =====================================================

    def workforce_forecast(
        self,
        hospital_data: dict,
    ) -> dict:

        logger.info("Forecasting Workforce")

        return self.analyze(
            hospital_data,
            """
Forecast staffing requirements.

Include

• Doctors
• Nurses
• Technicians
• Support Staff

Recommend optimal staffing.
"""
        )

    # =====================================================
    # Patient Flow
    # =====================================================

    def patient_flow(
        self,
        hospital_data: dict,
    ) -> dict:

        logger.info("Analyzing Patient Flow")

        return self.analyze(
            hospital_data,
            """
Analyze patient flow.

Include

• Admissions
• Transfers
• Discharges
• Bottlenecks
• Waiting Time
"""
        )

    # =====================================================
    # Financial Forecast
    # =====================================================

    def financial_forecast(
        self,
        hospital_data: dict,
    ) -> dict:

        logger.info("Forecasting Hospital Financials")

        return self.analyze(
            hospital_data,
            """
Forecast hospital financial performance.

Include

• Revenue
• Expenses
• Profit
• Cost Savings
• Resource Costs
"""
        )

    # =====================================================
    # Risk Analysis
    # =====================================================

    def operational_risk(
        self,
        hospital_data: dict,
    ) -> dict:

        logger.info("Running Operational Risk Analysis")

        return self.analyze(
            hospital_data,
            """
Analyze operational risks.

Include

• Capacity Risk
• Staffing Risk
• Financial Risk
• Equipment Risk
• Compliance Risk
"""
        )

    # =====================================================
    # Emergency Simulation
    # =====================================================

    def emergency_simulation(
        self,
        hospital_data: dict,
        scenario: str,
    ) -> dict:

        logger.info(
            "Running Emergency Simulation: {}",
            scenario,
        )

        return self.analyze(
            hospital_data,
            f"""
Run Hospital What-if Simulation.

Scenario

{scenario}

Predict

• Bed Demand
• ICU Demand
• Staff Requirement
• Resource Utilization
• Recommendations
"""
        )

    # =====================================================
    # Capacity Planning
    # =====================================================

    def capacity_planning(
        self,
        hospital_data: dict,
    ) -> dict:

        logger.info("Planning Hospital Capacity")

        return self.analyze(
            hospital_data,
            """
Develop a capacity planning strategy.

Include

• Bed Expansion
• ICU Expansion
• Workforce Growth
• Infrastructure
"""
        )

    # =====================================================
    # Explainability
    # =====================================================

    def explain(
        self,
        hospital_data: dict,
    ) -> dict:

        logger.info("Generating Explainability Report")

        return self.analyze(
            hospital_data,
            """
Explain all predictions.

Include

• Reasoning
• Key Factors
• Confidence
• Recommendations
"""
        )