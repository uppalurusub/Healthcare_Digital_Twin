use digital_twin;
CREATE TABLE patient_allergy (

    allergy_id BIGINT AUTO_INCREMENT PRIMARY KEY,

    patient_id VARCHAR(50),

    allergy_name VARCHAR(200),

    severity VARCHAR(30)
);