CREATE TABLE forecast_result (

    forecast_id VARCHAR(100) PRIMARY KEY,

    entity_type VARCHAR(50),

    entity_id VARCHAR(50),

    forecast_days INT,

    forecast_json JSON,

    created_at DATETIME
);