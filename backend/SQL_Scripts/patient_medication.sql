use digital_twin;
CREATE TABLE patient_medication (

    medication_id BIGINT AUTO_INCREMENT PRIMARY KEY,

    patient_id VARCHAR(50),

    medication_name VARCHAR(200),

    dosage VARCHAR(100),

    frequency VARCHAR(100),

    start_date DATE,

    end_date DATE
);