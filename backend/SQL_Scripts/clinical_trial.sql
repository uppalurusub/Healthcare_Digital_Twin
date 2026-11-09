CREATE TABLE clinical_trial (

    trial_id VARCHAR(50) PRIMARY KEY,

    protocol_number VARCHAR(100),

    phase VARCHAR(20),

    sponsor VARCHAR(200),

    target_enrollment INT,

    current_enrollment INT,

    status VARCHAR(30)
);