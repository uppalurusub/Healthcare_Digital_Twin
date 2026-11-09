CREATE TABLE simulation_result (

    simulation_id VARCHAR(100) PRIMARY KEY,

    entity_type VARCHAR(50),

    entity_id VARCHAR(50),

    scenario VARCHAR(500),

    simulation_json JSON,

    created_at DATETIME
);