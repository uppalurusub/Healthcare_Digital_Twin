"""
simulation_engine.py

Enterprise Healthcare Digital Twin Simulation Engine

Features
--------
- Patient Simulation
- Clinical Trial Simulation
- Hospital Simulation
- What-If Analysis
- Monte Carlo Simulation (Simple)
- Resource Simulation
- Risk Simulation
- Loguru Logging
"""

from __future__ import annotations

import random
from datetime import datetime
from typing import Any, Dict

from app.config.settings import settings
logger = settings.get_logger()


class SimulationEngine:
    """
    Enterprise Simulation Engine
    """

    def __init__(self) -> None:

        logger.info("Initializing Simulation Engine")

        self.version = "1.0.0"

        logger.success(
            "Simulation Engine Version {}",
            self.version,
        )

    # =====================================================
    # Generic Simulation
    # =====================================================

    def run(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:

        logger.info("Running Generic Simulation")

        entity = data.get("entity_type", "patient").lower()

        if entity == "patient":
            return self.patient_simulation(data)

        if entity == "trial":
            return self.trial_simulation(data)

        if entity == "hospital":
            return self.hospital_simulation(data)

        logger.warning(
            "Unknown entity type '{}'",
            entity,
        )

        return {}

    # =====================================================
    # Patient Simulation
    # =====================================================

    def patient_simulation(
        self,
        patient: Dict[str, Any],
    ) -> Dict[str, Any]:

        logger.info("Patient Simulation Started")

        systolic = self._extract_systolic(
            patient.get("blood_pressure", "120/80")
        )

        risk = 0.20

        if systolic >= 140:
            risk += 0.30

        if patient.get("age", 0) >= 65:
            risk += 0.20

        result = {
            "simulation": "patient",
            "hospitalization_probability": round(risk, 2),
            "icu_probability": round(risk / 3, 2),
            "mortality_probability": round(risk / 8, 2),
            "health_score": max(
                0,
                round(100 - risk * 100),
            ),
            "timestamp": datetime.utcnow().isoformat(),
        }

        logger.success("Patient Simulation Completed")

        return result

    # =====================================================
    # Trial Simulation
    # =====================================================

    def trial_simulation(
        self,
        trial: Dict[str, Any],
    ) -> Dict[str, Any]:

        logger.info("Clinical Trial Simulation")

        enrolled = trial.get("current_enrollment", 0)

        target = trial.get("target_enrollment", 100)

        dropout = random.uniform(0.05, 0.15)

        completion = enrolled * (1 - dropout)

        return {
            "simulation": "trial",
            "dropout_rate": round(dropout, 3),
            "completion_prediction": int(completion),
            "enrollment_gap": max(
                0,
                target - enrolled,
            ),
        }

    # =====================================================
    # Hospital Simulation
    # =====================================================

    def hospital_simulation(
        self,
        hospital: Dict[str, Any],
    ) -> Dict[str, Any]:

        logger.info("Hospital Simulation")

        beds = hospital.get("beds", 0)

        occupied = hospital.get(
            "occupied_beds",
            0,
        )

        occupancy = 0

        if beds > 0:
            occupancy = occupied / beds

        return {
            "simulation": "hospital",
            "occupancy_rate": round(
                occupancy,
                2,
            ),
            "available_beds": beds - occupied,
            "resource_utilization": round(
                occupancy * 100,
                2,
            ),
        }

    # =====================================================
    # What-If Analysis
    # =====================================================

    def what_if(
        self,
        current: Dict[str, Any],
        changes: Dict[str, Any],
    ) -> Dict[str, Any]:

        logger.info("Running What-If Analysis")

        updated = current.copy()

        updated.update(changes)

        before = self.patient_simulation(current)

        after = self.patient_simulation(updated)

        return {
            "before": before,
            "after": after,
            "changes": changes,
        }

    # =====================================================
    # Monte Carlo Simulation
    # =====================================================

    def monte_carlo(
        self,
        probability: float,
        iterations: int = 1000,
    ) -> Dict[str, Any]:

        logger.info(
            "Monte Carlo Simulation ({} iterations)",
            iterations,
        )

        success = 0

        for _ in range(iterations):

            if random.random() <= probability:
                success += 1

        return {
            "iterations": iterations,
            "estimated_probability": round(
                success / iterations,
                4,
            ),
        }

    # =====================================================
    # Risk Simulation
    # =====================================================

    def risk_simulation(
        self,
        patient: Dict[str, Any],
    ) -> Dict[str, Any]:

        logger.info("Risk Simulation")

        score = random.randint(15, 95)

        category = "Low"

        if score >= 70:
            category = "High"

        elif score >= 40:
            category = "Medium"

        return {
            "risk_score": score,
            "risk_category": category,
        }

    # =====================================================
    # Helper
    # =====================================================

    @staticmethod
    def _extract_systolic(
        blood_pressure: str,
    ) -> int:

        try:

            return int(
                blood_pressure.split("/")[0]
            )

        except Exception:

            return 120