CREATE TABLE trial_enrollment (

    enrollment_id BIGINT AUTO_INCREMENT PRIMARY KEY,

    trial_id VARCHAR(50),

    patient_id VARCHAR(50),

    enrollment_date DATE,

    status VARCHAR(30)
);