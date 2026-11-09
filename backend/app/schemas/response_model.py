"""
response_model.py

Pydantic Response Models
Healthcare Digital Twin Platform
"""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


# ==========================================================
# Common Response
# ==========================================================

class ResponseMetadata(BaseModel):
    request_id: Optional[str] = None
    timestamp: Optional[str] = None
    execution_time_ms: Optional[float] = None
    model_name: Optional[str] = None
    version: Optional[str] = None


class BaseResponse(BaseModel):
    success: bool = True
    message: str = "Request completed successfully."
    metadata: Optional[ResponseMetadata] = None


# ==========================================================
# Patient Digital Twin
# ==========================================================

class PatientTwinResponse(BaseResponse):
    patient_id: str

    digital_twin: Dict[str, Any]

    health_score: Optional[float] = None

    risk_score: Optional[float] = None

    recommendations: List[str] = []


# ==========================================================
# Clinical Trial Twin
# ==========================================================

class ClinicalTrialTwinResponse(BaseResponse):
    trial_id: str

    digital_twin: Dict[str, Any]

    enrollment_prediction: Optional[int] = None

    dropout_probability: Optional[float] = None

    recommendations: List[str] = []


# ==========================================================
# Hospital Twin
# ==========================================================

class HospitalTwinResponse(BaseResponse):
    hospital_id: str

    digital_twin: Dict[str, Any]

    occupancy_prediction: Optional[float] = None

    resource_utilization: Optional[float] = None

    recommendations: List[str] = []


# ==========================================================
# Simulation
# ==========================================================

class SimulationResponse(BaseResponse):
    simulation_id: str

    scenario: str

    duration_days: int

    simulation_results: Dict[str, Any]

    insights: List[str] = []


# ==========================================================
# Forecast
# ==========================================================

class ForecastResponse(BaseResponse):
    entity_id: str

    forecast_days: int

    target_variable: str

    forecast_values: List[Any]

    confidence_score: Optional[float] = None


# ==========================================================
# Prediction
# ==========================================================

class PredictionResponse(BaseResponse):
    entity_id: str

    prediction_type: str

    predicted_value: Any

    probability: Optional[float] = None

    confidence_score: Optional[float] = None

    explanation: Optional[str] = None


# ==========================================================
# Optimization
# ==========================================================

class OptimizationResponse(BaseResponse):
    entity_id: str

    objective: str

    optimized_parameters: Dict[str, Any]

    expected_improvement: Optional[float] = None


# ==========================================================
# Explainability
# ==========================================================

class ExplainResponse(BaseResponse):
    entity_id: str

    explanation: str

    feature_importance: Dict[str, float] = {}

    reasoning_steps: List[str] = []


# ==========================================================
# Compare Twins
# ==========================================================

class CompareTwinResponse(BaseResponse):
    comparison_results: Dict[str, Any]

    summary: str


# ==========================================================
# Agent Response
# ==========================================================

class AgentResponse(BaseResponse):
    answer: str

    reasoning: Optional[str] = None

    tools_used: List[str] = []

    sources: List[str] = []

    confidence_score: Optional[float] = None


# ==========================================================
# What-If Analysis
# ==========================================================

class WhatIfResponse(BaseResponse):
    scenario: str

    current_state: Dict[str, Any]

    simulated_state: Dict[str, Any]

    impact_analysis: Dict[str, Any]

    recommendations: List[str] = []


# ==========================================================
# Batch Processing
# ==========================================================

class BatchResponse(BaseResponse):
    total_records: int

    processed_records: int

    failed_records: int

    results: List[Dict[str, Any]]


# ==========================================================
# Error Response
# ==========================================================

class ErrorResponse(BaseModel):
    success: bool = False

    error_code: str

    error_message: str

    details: Optional[Any] = None


# ==========================================================
# Health Check
# ==========================================================

class HealthResponse(BaseModel):
    status: str = "Healthy"

    llm: str

    vector_database: str

    database: str

    simulation_engine: str

    prediction_engine: str