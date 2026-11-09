CREATE TABLE digital_twin_trial (

    twin_id VARCHAR(100) PRIMARY KEY,

    trial_id VARCHAR(50),

    twin_json JSON,

    created_at DATETIME
);