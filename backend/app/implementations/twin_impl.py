"""
implementations/digital_twin_impl.py

Healthcare Digital Twin Implementation

Section 1
---------
✓ Imports
✓ Class Definition
✓ Constructor
✓ Dependency Injection
✓ LLM Initialization
✓ ChromaDB Initialization
✓ MySQL Initialization
✓ Agent Initialization
✓ Loguru Logging
"""

from __future__ import annotations

from typing import Optional
import os

from app.config.settings import settings
logger = settings.get_logger()

from langchain_openai import ChatOpenAI

from app.agents.digital_twin_agent import DigitalTwinAgent
from app.agents.patient_agent import PatientAgent
from app.agents.trial_agent import TrialAgent
from app.agents.hospital_agent import HospitalAgent

from app.database.chroma_db import ChromaDBManager
from app.database.mysql_db import MySQLDBManager

from app.implementations.simulation_engine import SimulationEngine
from app.implementations.prediction_engine import PredictionEngine

from app.schemas.request_model import (
    PatientTwinRequest,
)

from app.schemas.response_model import (
    PatientTwinResponse,
)

from langchain_openai import AzureOpenAIEmbeddings

from langchain_huggingface import HuggingFaceEmbeddings

class DigitalTwinImplementation:
    """
    Enterprise Healthcare Digital Twin Implementation
    """

    def __init__(
        self,
        llm: Optional[ChatOpenAI] = None,
        chroma_db: Optional[ChromaDBManager] = None,
        mysql_db: Optional[MySQLDBManager] = None,
    ) -> None:

        logger.info("=" * 80)
        logger.info("Initializing Healthcare Digital Twin Platform")
        logger.info("=" * 80)

        

        logger.info("Configuration loaded successfully")

        # =====================================================
        # LLM
        # =====================================================

        #self.llm = get_llm() or self._initialize_llm()
        self.llm = settings.get_model_client()

        # =====================================================
        # ChromaDB
        # =====================================================

        self.chroma_db = chroma_db or self._initialize_chroma()

        # =====================================================
        # MySQL
        # =====================================================

        self.mysql_db = mysql_db or self._initialize_mysql()

        # =====================================================
        # Engines
        # =====================================================

        logger.info("Initializing Simulation Engine")

        self.simulation_engine = SimulationEngine()

        logger.info("Initializing Prediction Engine")

        self.prediction_engine = PredictionEngine()

        # =====================================================
        # Agents
        # =====================================================

        logger.info("Initializing Digital Twin Agent")

        self.digital_twin_agent = DigitalTwinAgent(
            llm=self.llm,
            tools=[],
        )

        logger.info("Initializing Patient Agent")

        self.patient_agent = PatientAgent(
            llm=self.llm,
            tools=[],
        )

        logger.info("Initializing Trial Agent")

        self.trial_agent = TrialAgent(
            llm=self.llm,
            tools=[],
        )

        logger.info("Initializing Hospital Agent")

        self.hospital_agent = HospitalAgent(
            llm=self.llm,
            tools=[],
        )

        logger.success("Healthcare Digital Twin Platform Initialized")

    # ==========================================================
    # LLM
    # ==========================================================

    def _initialize_llm(self) -> ChatOpenAI:
        """
        Initialize the configured Large Language Model.
        """

        logger.info("Loading Large Language Model")

        llm = ChatOpenAI(
            model=self.settings.OPENAI_MODEL,
            api_key=self.settings.OPENAI_API_KEY,
            temperature=self.settings.LLM_TEMPERATURE,
            max_tokens=self.settings.LLM_MAX_TOKENS,
        )

        logger.success(
            "LLM initialized successfully ({})",
            self.settings.OPENAI_MODEL,
        )

        return llm

    # ==========================================================
    # ChromaDB
    # ==========================================================

    ###################################################################
    # Embeddings
    ###################################################################

    def _load_embeddings(self):

        #logger.info(f"Embedding Provider : {self.embedding_provider}")

        return HuggingFaceEmbeddings(
                model_name=os.getenv(
                    "HUGGINGFACE_MODEL",
                    "sentence-transformers/all-MiniLM-L6-v2"
                )
            )

    def _initialize_chroma(self) -> ChromaDBManager:
        """
        Initialize Chroma Vector Database.
        """

        logger.info("Connecting to ChromaDB")
        CHROMA_DIRECTORY = os.getenv("CHROMA_DIRECTORY")
        EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

        chroma = ChromaDBManager(
            persist_directory=CHROMA_DIRECTORY,
            collection_name=CHROMA_DIRECTORY,
            embedding_model=EMBEDDING_MODEL,
        )

        logger.success("ChromaDB initialized")

        return chroma

    # ==========================================================
    # MySQL
    # ==========================================================
    

    def _initialize_mysql(self) -> MySQLDBManager:
        """
        Initialize MySQL Database.
        """
        
        logger.info("Connecting to MySQL")

        mysql = MySQLDBManager(
            connection_string=settings.MYSQL_CONNECTION_STRING,
        )

        logger.success("MySQL initialized")

        return mysql
    
    # ==========================================================
    # Health Check
    # ==========================================================

    def health_check(self) -> dict:
        """
        Perform application dependency health check.
        """

        logger.info("=" * 80)
        logger.info("Running Healthcare Digital Twin Health Check")
        logger.info("=" * 80)

        health = {
            "application": "Healthy",
            "llm": False,
            "mysql": False,
            "chromadb": False,
            "simulation_engine": False,
            "prediction_engine": False,
        }

        # ---------------- LLM ----------------

        try:

            logger.info("Checking LLM...")

            self.llm.invoke("Say OK")

            health["llm"] = True

            logger.success("LLM Healthy")

        except Exception as ex:

            logger.exception(ex)

        # ---------------- MySQL ----------------

        try:

            logger.info("Checking MySQL...")

            health["mysql"] = self.mysql_db.health_check()

        except Exception as ex:

            logger.exception(ex)

        # ---------------- Chroma ----------------

        try:

            logger.info("Checking ChromaDB...")

            health["chromadb"] = self.chroma_db.health_check()

        except Exception as ex:

            logger.exception(ex)

        # ---------------- Engines ----------------

        health["simulation_engine"] = self.simulation_engine is not None
        health["prediction_engine"] = self.prediction_engine is not None

        logger.success("Health Check Completed")

        return health


    # ==========================================================
    # Retrieve Patient History
    # ==========================================================

    def _retrieve_patient_history(
        self,
        patient_id: str,
    ) -> list[dict]:
        """
        Retrieve patient history from MySQL.
        """

        logger.info(
            "Retrieving patient history : {}",
            patient_id,
        )

        query = """
            SELECT *
            FROM patient_history
            WHERE patient_id = :patient_id
            ORDER BY visit_date DESC
        """

        try:

            records = self.mysql_db.execute_query(
                query=query,
                params={
                    "patient_id": patient_id
                },
            )

            logger.success(
                "{} patient history records found",
                len(records),
            )

            return records

        except Exception as ex:

            logger.exception(ex)

            return []


    # ==========================================================
    # Retrieve Patient Documents
    # ==========================================================

    def _retrieve_patient_documents(
        self,
        patient_id: str,
        k: int = 5,
    ) -> str:
        """
        Retrieve relevant patient documents from ChromaDB.
        """

        logger.info(
            "Retrieving patient documents : {}",
            patient_id,
        )

        try:

            documents = self.chroma_db.metadata_search(
                query=f"Patient {patient_id}",
                metadata_filter={
                    "patient_id": patient_id
                },
                k=k,
            )

            logger.success(
                "{} relevant documents retrieved",
                len(documents),
            )

            return self._format_documents(documents)

        except Exception as ex:

            logger.exception(ex)

            return ""


    # ==========================================================
    # Format Documents
    # ==========================================================

    def _format_documents(
        self,
        documents,
    ) -> str:
        """
        Convert LangChain Documents into text context.
        """

        logger.info("Formatting retrieved documents")

        if not documents:

            logger.warning("No documents available")

            return ""

        context = []

        for index, document in enumerate(documents, start=1):

            context.append(
                f"""
    Document {index}

    {document.page_content}
    """
            )

        logger.success(
            "{} documents formatted",
            len(context),
        )

        return "\n".join(context)
    

    # ==========================================================
    # Build Patient Context
    # ==========================================================

    def _build_patient_context(
        self,
        request: PatientTwinRequest,
    ) -> str:
        """
        Build comprehensive patient context for the LLM.
        """

        logger.info(
            "Building patient context for {}",
            request.patient_id,
        )

        history = self._retrieve_patient_history(
            request.patient_id
        )

        documents = self._retrieve_patient_documents(
            request.patient_id
        )

        context = f"""
    ==================================================
    PATIENT PROFILE
    ==================================================

    Patient ID : {request.patient_id}
    Age        : {request.age}
    Gender     : {request.gender}

    Vitals
    ------
    Blood Pressure : {request.blood_pressure}
    Heart Rate     : {request.heart_rate}
    Temperature    : {request.temperature}
    SpO2           : {request.spo2}

    Diagnoses
    ---------
    {request.diagnoses}

    Medications
    -----------
    {request.medications}

    Allergies
    ---------
    {request.allergies}

    ==================================================
    PATIENT HISTORY
    ==================================================

    {self._safe_json(history)}

    ==================================================
    RETRIEVED CLINICAL DOCUMENTS
    ==================================================

    {documents}
    """

        logger.success("Patient context prepared")

        return context


    # ==========================================================
    # Save Digital Twin
    # ==========================================================

    def _save_patient_twin(
        self,
        twin_id: str,
        request: PatientTwinRequest,
        response: dict,
    ) -> None:
        """
        Persist Digital Twin in MySQL.
        """

        logger.info(
            "Saving Digital Twin : {}",
            twin_id,
        )

        query = """
        INSERT INTO patient_digital_twin
        (
            twin_id,
            patient_id,
            twin_json,
            created_at
        )
        VALUES
        (
            :twin_id,
            :patient_id,
            :twin_json,
            :created_at
        )
        """

        self.mysql_db.insert(
            query=query,
            params={
                "twin_id": twin_id,
                "patient_id": request.patient_id,
                "twin_json": self._safe_json(response),
                "created_at": self._current_timestamp(),
            },
        )

        logger.success("Digital Twin saved successfully")


    # ==========================================================
    # Generate Twin ID
    # ==========================================================

    def _generate_twin_id(self) -> str:
        """
        Generate a unique Digital Twin identifier.
        """

        from uuid import uuid4

        twin_id = f"TWIN-{uuid4().hex.upper()}"

        logger.debug(
            "Generated Twin ID : {}",
            twin_id,
        )

        return twin_id


    # ==========================================================
    # Current Timestamp
    # ==========================================================

    def _current_timestamp(self) -> str:
        """
        Current UTC timestamp.
        """

        from datetime import datetime, timezone

        timestamp = (
            datetime.now(timezone.utc)
            .replace(microsecond=0)
            .isoformat()
        )

        logger.debug(
            "Timestamp : {}",
            timestamp,
        )

        return timestamp


    # ==========================================================
    # Safe JSON Serializer
    # ==========================================================

    def _safe_json(
        self,
        value,
    ) -> str:
        """
        Safely serialize Python objects to JSON.
        """

        import json

        try:

            return json.dumps(
                value,
                indent=4,
                default=str,
                ensure_ascii=False,
            )

        except Exception as ex:

            logger.exception(ex)

            return "{}"


    # ==========================================================
    # Response Validator
    # ==========================================================

    def _validate_agent_response(
        self,
        response: dict,
    ) -> dict:
        """
        Ensure the agent response contains an output payload.
        """

        if not response:
            logger.warning("Empty agent response received")
            return {"output": ""}

        if "output" not in response:
            logger.warning("Missing 'output' in agent response")
            response["output"] = ""

        return response


    # ==========================================================
    # Log Execution Time
    # ==========================================================

    def _log_execution_time(
        self,
        operation: str,
        start_time,
    ) -> None:
        """
        Log execution duration.
        """

        from datetime import datetime

        elapsed = (
            datetime.now() - start_time
        ).total_seconds()

        logger.info(
            "{} completed in {:.2f} seconds",
            operation,
            elapsed,
        )

    # ==========================================================
    # Create Patient Digital Twin
    # ==========================================================

    async def create_patient_twin(
        self,
        request: PatientTwinRequest,
    ) -> PatientTwinResponse:
        """
        Create a Patient Digital Twin.

        Workflow
        --------
        1. Build patient context
        2. Invoke Patient Agent
        3. Perform Risk Analysis
        4. Forecast Patient Health
        5. Run Simulation
        6. Persist Digital Twin
        7. Return Response
        """

        from datetime import datetime

        start_time = datetime.now()

        logger.info("=" * 80)
        logger.info(
            "Creating Patient Digital Twin : {}",
            request.patient_id,
        )
        logger.info("=" * 80)

        try:

            # --------------------------------------------------
            # Generate Twin ID
            # --------------------------------------------------

            twin_id = self._generate_twin_id()

            logger.info(
                "Twin ID : {}",
                twin_id,
            )

            # --------------------------------------------------
            # Build Patient Context
            # --------------------------------------------------

            patient_context = self._build_patient_context(
                request
            )

            # --------------------------------------------------
            # Agent Analysis
            # --------------------------------------------------

            logger.info("Running Patient Agent")

            analysis = self.patient_agent.analyze(
                patient_data={
                    "patient_context": patient_context
                },
                question="""
    Create a comprehensive Patient Digital Twin.

    Provide

    • Clinical Summary
    • Overall Health
    • Key Findings
    • Recommendations
    """,
            )

            analysis = self._validate_agent_response(
                analysis
            )

            # --------------------------------------------------
            # Risk Analysis
            # --------------------------------------------------

            logger.info("Running Risk Analysis")

            risk = self.patient_agent.disease_risk(
                request.model_dump()
            )

            risk = self._validate_agent_response(
                risk
            )

            # --------------------------------------------------
            # Forecast
            # --------------------------------------------------

            logger.info("Running Forecast")

            forecast = self.patient_agent.forecast(
                request.model_dump(),
                days=30,
            )

            forecast = self._validate_agent_response(
                forecast
            )

            # --------------------------------------------------
            # Simulation
            # --------------------------------------------------

            logger.info("Running Simulation")

            simulation = self.simulation_engine.run(
                request.model_dump()
            )

            # --------------------------------------------------
            # Prediction Engine
            # --------------------------------------------------

            logger.info("Running Prediction Engine")

            prediction = self.prediction_engine.predict(
                request.model_dump()
            )

            # --------------------------------------------------
            # Digital Twin
            # --------------------------------------------------

            digital_twin = {
                "twin_id": twin_id,
                "patient": request.model_dump(),
                "analysis": analysis["output"],
                "risk_analysis": risk["output"],
                "forecast": forecast["output"],
                "simulation": simulation,
                "prediction": prediction,
            }

            # --------------------------------------------------
            # Persist
            # --------------------------------------------------

            self._save_patient_twin(
                twin_id=twin_id,
                request=request,
                response=digital_twin,
            )

            # --------------------------------------------------
            # Build Response
            # --------------------------------------------------

            response = PatientTwinResponse(
                success=True,
                message="Patient Digital Twin created successfully.",
                patient_id=request.patient_id,
                digital_twin=digital_twin,
                health_score=prediction.get(
                    "health_score",
                    0.0,
                ),
                risk_score=prediction.get(
                    "risk_score",
                    0.0,
                ),
                recommendations=prediction.get(
                    "recommendations",
                    [],
                ),
            )

            self._log_execution_time(
                "Create Patient Digital Twin",
                start_time,
            )

            logger.success(
                "Patient Digital Twin Created Successfully"
            )

            return response

        except Exception as ex:

            logger.exception(ex)

            self._log_execution_time(
                "Create Patient Digital Twin (Failed)",
                start_time,
            )

            return PatientTwinResponse(
                success=False,
                message=str(ex),
                patient_id=request.patient_id,
                digital_twin={},
                health_score=0.0,
                risk_score=0.0,
                recommendations=[],
            )