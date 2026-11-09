CREATE TABLE digital_twin_hospital (

    twin_id VARCHAR(100) PRIMARY KEY,

    hospital_id VARCHAR(50),

    twin_json JSON,

    created_at DATETIME
);