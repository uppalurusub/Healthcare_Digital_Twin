-- ============================================================
-- Table: patient_digital_twin
-- Description: Stores Patient Digital Twin snapshots
-- ============================================================

CREATE TABLE patient_digital_twin
(
    id BIGINT AUTO_INCREMENT PRIMARY KEY,

    twin_id VARCHAR(100) NOT NULL,
    patient_id VARCHAR(50) NOT NULL,

    twin_version INT NOT NULL DEFAULT 1,

    twin_status VARCHAR(30) DEFAULT 'ACTIVE',

    health_score DECIMAL(5,2),

    risk_score DECIMAL(5,2),

    confidence_score DECIMAL(5,2),

    prediction_summary TEXT,

    simulation_summary TEXT,

    recommendation_summary TEXT,

    twin_json JSON NOT NULL,

    embedding_document_id VARCHAR(100),

    ai_model VARCHAR(100),

    embedding_model VARCHAR(200),

    llm_model VARCHAR(100),

    created_by VARCHAR(100),

    request_id VARCHAR(100),

    organization VARCHAR(200),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    INDEX idx_patient(patient_id),

    INDEX idx_twin(twin_id),

    INDEX idx_version(patient_id, twin_version),

    INDEX idx_created(created_at),

    UNIQUE KEY uk_patient_version
    (
        patient_id,
        twin_version
    )
);