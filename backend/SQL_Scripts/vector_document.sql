CREATE TABLE vector_document (

    document_id VARCHAR(100) PRIMARY KEY,

    patient_id VARCHAR(50),

    source VARCHAR(200),

    metadata JSON,

    created_at DATETIME
);