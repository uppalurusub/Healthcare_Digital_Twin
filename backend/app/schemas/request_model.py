"""
request_model.py

Pydantic request models for Healthcare Digital Twin Platform
"""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


# ============================================================
# Common Metadata
# ============================================================

class Metadata(BaseModel):
    request_id: Optional[str] = None
    user_id: Optional[str] = None
    organization: Optional[str] = None
    timestamp: Optional[str] = None


# ============================================================
# Patient Digital Twin
# ============================================================

class PatientTwinRequest(BaseModel):
    patient_id: str = Field(..., description="Unique Patient ID")

    age: int
    gender: str

    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None
    bmi: Optional[float] = None

    blood_pressure: Optional[str] = None
    heart_rate: Optional[int] = None
    respiratory_rate: Optional[int] = None
    spo2: Optional[float] = None
    temperature: Optional[float] = None

    diagnoses: List[str] = []
    medications: List[str] = []
    allergies: List[str] = []

    laboratory_results: Dict[str, Any] = {}

    smoking_status: Optional[str] = None
    alcohol_use: Optional[str] = None

    medical_history: Dict[str, Any] = {}

    metadata: Optional[Metadata] = None


# ============================================================
# Clinical Trial Twin
# ============================================================

class ClinicalTrialTwinRequest(BaseModel):
    trial_id: str

    protocol_id: Optional[str] = None
    sponsor: Optional[str] = None

    phase: Optional[str] = None

    indication: Optional[str] = None

    enrollment_target: Optional[int] = None
    enrolled_subjects: Optional[int] = None

    dropout_rate: Optional[float] = None

    sites: List[str] = []

    countries: List[str] = []

    metadata: Optional[Metadata] = None


# ============================================================
# Hospital Twin
# ============================================================

class HospitalTwinRequest(BaseModel):
    hospital_id: str

    hospital_name: str

    total_beds: int

    icu_beds: int

    occupied_beds: int

    doctors: int

    nurses: int

    ventilators: Optional[int] = 0

    occupancy_rate: Optional[float] = None

    departments: List[str] = []

    metadata: Optional[Metadata] = None


# ============================================================
# Simulation Request
# ============================================================

class SimulationRequest(BaseModel):
    twin_type: str = Field(
        ...,
        description="patient | clinical_trial | hospital"
    )

    entity_id: str

    scenario: str = Field(
        ...,
        description="Simulation scenario"
    )

    simulation_days: int = 30

    parameters: Dict[str, Any] = {}


# ============================================================
# Forecast Request
# ============================================================

class ForecastRequest(BaseModel):
    twin_type: str

    entity_id: str

    forecast_days: int = 30

    target_variable: str

    input_features: Dict[str, Any] = {}


# ============================================================
# Prediction Request
# ============================================================

class PredictionRequest(BaseModel):
    twin_type: str

    entity_id: str

    prediction_type: str

    features: Dict[str, Any]


# ============================================================
# Optimization Request
# ============================================================

class OptimizationRequest(BaseModel):
    twin_type: str

    entity_id: str

    objective: str

    constraints: Dict[str, Any] = {}


# ============================================================
# Explainability Request
# ============================================================

class ExplainRequest(BaseModel):
    twin_type: str

    entity_id: str

    prediction_id: Optional[str] = None


# ============================================================
# Comparison Request
# ============================================================

class CompareTwinRequest(BaseModel):
    twin_type: str

    entity_ids: List[str]


# ============================================================
# Generic Agent Request
# ============================================================

class AgentRequest(BaseModel):
    twin_type: str

    entity_id: Optional[str] = None

    question: str

    context: Optional[str] = None

    tools: Optional[List[str]] = []


# ============================================================
# What-If Analysis Request
# ============================================================

class WhatIfRequest(BaseModel):
    twin_type: str

    entity_id: str

    changes: Dict[str, Any]

    duration_days: int = 30


# ============================================================
# Batch Processing
# ============================================================

class BatchTwinRequest(BaseModel):
    twin_type: str

    entities: List[Dict[str, Any]]