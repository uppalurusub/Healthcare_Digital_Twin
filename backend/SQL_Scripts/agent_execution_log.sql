CREATE TABLE agent_execution_log (

    execution_id VARCHAR(100) PRIMARY KEY,

    agent_name VARCHAR(100),

    request_json JSON,

    response_json JSON,

    execution_time DECIMAL(10,3),

    status VARCHAR(30),

    created_at DATETIME
);