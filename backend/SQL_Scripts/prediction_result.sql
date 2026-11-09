CREATE TABLE prediction_result (

    prediction_id VARCHAR(100) PRIMARY KEY,

    entity_type VARCHAR(50),

    entity_id VARCHAR(50),

    prediction_json JSON,

    confidence DECIMAL(5,2),

    created_at DATETIME
);