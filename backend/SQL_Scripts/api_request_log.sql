use digital_twin;

CREATE TABLE api_request_log (

    request_id VARCHAR(100) PRIMARY KEY,

    endpoint VARCHAR(200),

    request_json JSON,

    response_json JSON,

    execution_time DECIMAL(10,3),

    created_at DATETIME
);