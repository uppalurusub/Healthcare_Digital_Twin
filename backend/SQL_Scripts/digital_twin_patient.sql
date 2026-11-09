CREATE TABLE digital_twin_patient (

    twin_id VARCHAR(100) PRIMARY KEY,

    patient_id VARCHAR(50),

    twin_version INT,

    twin_json JSON,

    health_score DECIMAL(5,2),

    risk_score DECIMAL(5,2),

    confidence DECIMAL(5,2),

    created_at DATETIME
);