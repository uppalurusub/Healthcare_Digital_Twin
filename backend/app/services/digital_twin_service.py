"""
services/digital_twin_service.py

Enterprise Healthcare Digital Twin Service

Architecture
------------
Router
    │
    ▼
Service
    │
    ▼
Implementation
"""

from __future__ import annotations

from app.config.settings import settings
logger = settings.get_logger()

from app.implementations.twin_impl import (
    DigitalTwinImplementation,
)

from app.schemas.request_model import (
    PatientTwinRequest,
    ClinicalTrialTwinRequest,
    HospitalTwinRequest,
    SimulationRequest,
    ForecastRequest,
    PredictionRequest,
    OptimizationRequest,
    ExplainRequest,
    CompareTwinRequest,
)

from app.schemas.response_model import (
    PatientTwinResponse,
    ClinicalTrialTwinResponse,
    HospitalTwinResponse,
    SimulationResponse,
    ForecastResponse,
    PredictionResponse,
    OptimizationResponse,
    ExplainResponse,
    CompareTwinResponse,
)

import mlflow
from datetime import datetime
import time

mlflow.set_tracking_uri(
    "http://localhost:5000"
)

mlflow.set_experiment(
    "Healthcare_Digital_Twin_Interface"
)

class DigitalTwinService:
    """
    Enterprise Digital Twin Service
    """

    def __init__(self):

        logger.info(
            "Initializing Digital Twin Service"
        )

        self.impl = DigitalTwinImplementation()

        logger.success(
            "Digital Twin Service Initialized"
        )

    # ==========================================================
    # Health Check
    # ==========================================================

    async def health_check(self) -> dict:

        logger.info("Health Check Requested")

        try:

            return self.impl.health_check()

        except Exception as ex:

            logger.exception(ex)

            raise

    # ==========================================================
    # Patient Digital Twin
    # ==========================================================

    async def create_patient_twin(
        self,
        request: PatientTwinRequest,
    ) -> PatientTwinResponse:

        logger.info(
            "Service -> Create Patient Twin"
        )

        start_time = datetime.now()
        start_ts = time.time()

        try:

            with mlflow.start_run(
                run_name=
                f"Healthcare_Digitial_Twin_Create_Patient_Twin_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            ):
                # Log to MLflow
                mlflow.log_param(
                    "start_time",
                    start_time.strftime("%Y-%m-%d %H:%M:%S")
                )
                mlflow.log_param(
                    "input_text",
                    request
                )

                response = await self.impl.create_patient_twin(
                    request
                )
            
                mlflow.log_param(
                    "response",
                    response
                )

                mlflow.set_tag(
                    "source",
                    "FastAPI"
                )

                mlflow.set_tag(
                    "endpoint",
                    "digital-twin/patient"
                )



                end_time = datetime.now()
                end_ts = time.time()

                execution_time = end_ts - start_ts

                mlflow.log_param(
                    "end_time",
                    end_time.strftime("%Y-%m-%d %H:%M:%S")
                )

                mlflow.log_metric(
                    "execution_time_seconds",
                    round(execution_time, 4)
                )

                return response

        except Exception as ex:

            logger.exception(ex)

            raise

    # ==========================================================
    # Clinical Trial Digital Twin
    # ==========================================================

    async def create_trial_twin(
        self,
        request: ClinicalTrialTwinRequest,
    ) -> ClinicalTrialTwinResponse:

        logger.info(
            "Service -> Create Trial Twin"
        )

        start_time = datetime.now()
        start_ts = time.time()

        try:

            with mlflow.start_run(
                run_name=
                f"Healthcare_Digitial_Twin_Create_Trial_Twin_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            ):
                # Log to MLflow
                mlflow.log_param(
                    "start_time",
                    start_time.strftime("%Y-%m-%d %H:%M:%S")
                )
                mlflow.log_param(
                    "input_text",
                    request
                )

                response = await self.impl.create_trial_twin(
                    request
                )

                mlflow.log_param(
                    "response",
                    response
                )

                mlflow.set_tag(
                    "source",
                    "FastAPI"
                )

                mlflow.set_tag(
                    "endpoint",
                    "digital-twin/trial"
                )



                end_time = datetime.now()
                end_ts = time.time()

                execution_time = end_ts - start_ts

                mlflow.log_param(
                    "end_time",
                    end_time.strftime("%Y-%m-%d %H:%M:%S")
                )

                mlflow.log_metric(
                    "execution_time_seconds",
                    round(execution_time, 4)
                )

            return response

        except Exception as ex:

            logger.exception(ex)

            raise

    # ==========================================================
    # Hospital Digital Twin
    # ==========================================================

    async def create_hospital_twin(
        self,
        request: HospitalTwinRequest,
    ) -> HospitalTwinResponse:

        logger.info(
            "Service -> Create Hospital Twin"
        )

        start_time = datetime.now()
        start_ts = time.time()

        try:

            with mlflow.start_run(
                run_name=
                f"Healthcare_Digitial_Twin_Create_Hospital_Twin_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            ):
                # Log to MLflow
                mlflow.log_param(
                    "start_time",
                    start_time.strftime("%Y-%m-%d %H:%M:%S")
                )
                mlflow.log_param(
                    "input_text",
                    request
                )

                response = await self.impl.create_hospital_twin(
                    request
                )

                mlflow.log_param(
                    "response",
                    response
                )

                mlflow.set_tag(
                    "source",
                    "FastAPI"
                )

                mlflow.set_tag(
                    "endpoint",
                    "digital-twin/hospital"
                )



                end_time = datetime.now()
                end_ts = time.time()

                execution_time = end_ts - start_ts

                mlflow.log_param(
                    "end_time",
                    end_time.strftime("%Y-%m-%d %H:%M:%S")
                )

                mlflow.log_metric(
                    "execution_time_seconds",
                    round(execution_time, 4)
                )
             
            return response

        except Exception as ex:

            logger.exception(ex)

            raise

    # ==========================================================
    # Simulation
    # ==========================================================

    async def simulate(
        self,
        request: SimulationRequest,
    ) -> SimulationResponse:

        logger.info(
            "Service -> Simulation"
        )

        start_time = datetime.now()
        start_ts = time.time()
        try:
            with mlflow.start_run(
                run_name=
                f"Healthcare_Digitial_Twin_Create_Simulate_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            ):
                # Log to MLflow
                mlflow.log_param(
                    "start_time",
                    start_time.strftime("%Y-%m-%d %H:%M:%S")
                )
                mlflow.log_param(
                    "input_text",
                    request
                )

                response =  await self.impl.simulate(
                    request
                )
            
                mlflow.log_param(
                        "response",
                        response
                    )

                mlflow.set_tag(
                    "source",
                    "FastAPI"
                )

                mlflow.set_tag(
                    "endpoint",
                    "digital-twin/simulate"
                )

                end_time = datetime.now()
                end_ts = time.time()

                execution_time = end_ts - start_ts

                mlflow.log_param(
                    "end_time",
                    end_time.strftime("%Y-%m-%d %H:%M:%S")
                )

                mlflow.log_metric(
                    "execution_time_seconds",
                    round(execution_time, 4)
                )
            
            return response

        except Exception as ex:

            logger.exception(ex)

            raise

    # ==========================================================
    # Forecast
    # ==========================================================

    async def forecast(
        self,
        request: ForecastRequest,
    ) -> ForecastResponse:

        logger.info(
            "Service -> Forecast"
        )

        start_time = datetime.now()
        start_ts = time.time()

        try:

            with mlflow.start_run(
                run_name=
                f"Healthcare_Digitial_Twin_Forecast_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            ):
                # Log to MLflow
                mlflow.log_param(
                    "start_time",
                    start_time.strftime("%Y-%m-%d %H:%M:%S")
                )
                mlflow.log_param(
                    "input_text",
                    request
                )

                response = await self.impl.forecast(
                    request
                )

                mlflow.log_param(
                    "response",
                    response
                )

                mlflow.set_tag(
                    "source",
                    "FastAPI"
                )

                mlflow.set_tag(
                    "endpoint",
                    "digital-twin/forecast"
                )



                end_time = datetime.now()
                end_ts = time.time()

                execution_time = end_ts - start_ts

                mlflow.log_param(
                    "end_time",
                    end_time.strftime("%Y-%m-%d %H:%M:%S")
                )

                mlflow.log_metric(
                    "execution_time_seconds",
                    round(execution_time, 4)
                )
             
            return response

        except Exception as ex:

            logger.exception(ex)

            raise

    # ==========================================================
    # Prediction
    # ==========================================================

    async def predict(
        self,
        request: PredictionRequest,
    ) -> PredictionResponse:

        logger.info(
            "Service -> Prediction"
        )

        start_time = datetime.now()
        start_ts = time.time()

        try:
            with mlflow.start_run(
                run_name=
                f"Healthcare_Digitial_Twin_Predict_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            ):
                # Log to MLflow
                mlflow.log_param(
                    "start_time",
                    start_time.strftime("%Y-%m-%d %H:%M:%S")
                )
                mlflow.log_param(
                    "input_text",
                    request
                )

                response =  await self.impl.predict(
                    request
                )

                mlflow.log_param(
                    "response",
                    response
                )

                mlflow.set_tag(
                    "source",
                    "FastAPI"
                )

                mlflow.set_tag(
                    "endpoint",
                    "digital-twin/predict"
                )



                end_time = datetime.now()
                end_ts = time.time()

                execution_time = end_ts - start_ts

                mlflow.log_param(
                    "end_time",
                    end_time.strftime("%Y-%m-%d %H:%M:%S")
                )

                mlflow.log_metric(
                    "execution_time_seconds",
                    round(execution_time, 4)
                )
        
            return response

        except Exception as ex:

            logger.exception(ex)

            raise

    # ==========================================================
    # Optimization
    # ==========================================================

    async def optimize(
        self,
        request: OptimizationRequest,
    ) -> OptimizationResponse:

        logger.info(
            "Service -> Optimization"
        )

        start_time = datetime.now()
        start_ts = time.time()

        try:
            with mlflow.start_run(
                run_name=
                f"Healthcare_Digitial_Twin_Optimize_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            ):
                # Log to MLflow
                mlflow.log_param(
                    "start_time",
                    start_time.strftime("%Y-%m-%d %H:%M:%S")
                )
                mlflow.log_param(
                    "input_text",
                    request
                )

                response = await self.impl.optimize(
                    request
                )

                mlflow.log_param(
                    "response",
                    response
                )

                mlflow.set_tag(
                    "source",
                    "FastAPI"
                )

                mlflow.set_tag(
                    "endpoint",
                    "digital-twin/optimize"
                )



                end_time = datetime.now()
                end_ts = time.time()

                execution_time = end_ts - start_ts

                mlflow.log_param(
                    "end_time",
                    end_time.strftime("%Y-%m-%d %H:%M:%S")
                )

                mlflow.log_metric(
                    "execution_time_seconds",
                    round(execution_time, 4)
                )
             
            return response

        except Exception as ex:

            logger.exception(ex)

            raise

    # ==========================================================
    # Explainability
    # ==========================================================

    async def explain(
        self,
        request: ExplainRequest,
    ) -> ExplainResponse:

        logger.info(
            "Service -> Explainability"
        )

        start_time = datetime.now()
        start_ts = time.time()

        try:
            with mlflow.start_run(
                run_name=
                f"Healthcare_Digitial_Twin_Explain_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            ):
                # Log to MLflow
                mlflow.log_param(
                    "start_time",
                    start_time.strftime("%Y-%m-%d %H:%M:%S")
                )
                mlflow.log_param(
                    "input_text",
                    request
                )

                response = await self.impl.explain(
                    request
                )

                mlflow.log_param(
                    "response",
                    response
                )

                mlflow.set_tag(
                    "source",
                    "FastAPI"
                )

                mlflow.set_tag(
                    "endpoint",
                    "digital-twin/explain"
                )



                end_time = datetime.now()
                end_ts = time.time()

                execution_time = end_ts - start_ts

                mlflow.log_param(
                    "end_time",
                    end_time.strftime("%Y-%m-%d %H:%M:%S")
                )

                mlflow.log_metric(
                    "execution_time_seconds",
                    round(execution_time, 4)
                )

            return response

        except Exception as ex:

            logger.exception(ex)

            raise

    # ==========================================================
    # Compare Digital Twins
    # ==========================================================

    async def compare_twins(
        self,
        request: CompareTwinRequest,
    ) -> CompareTwinResponse:

        logger.info(
            "Service -> Compare Twins"
        )

        start_time = datetime.now()
        start_ts = time.time()

        try:
            with mlflow.start_run(
                run_name=
                f"Healthcare_Digitial_Twin_Compare_Twins_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            ):
                # Log to MLflow
                mlflow.log_param(
                    "start_time",
                    start_time.strftime("%Y-%m-%d %H:%M:%S")
                )
                mlflow.log_param(
                    "input_text",
                    request
                )

                response = await self.impl.compare_twins(
                    request
                )

                mlflow.log_param(
                    "response",
                    response
                )

                mlflow.set_tag(
                    "source",
                    "FastAPI"
                )

                mlflow.set_tag(
                    "endpoint",
                    "digital-twin/compare"
                )



                end_time = datetime.now()
                end_ts = time.time()

                execution_time = end_ts - start_ts

                mlflow.log_param(
                    "end_time",
                    end_time.strftime("%Y-%m-%d %H:%M:%S")
                )

                mlflow.log_metric(
                    "execution_time_seconds",
                    round(execution_time, 4)
                )


             
            return response

        except Exception as ex:

            logger.exception(ex)

            raise