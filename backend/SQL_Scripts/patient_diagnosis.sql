use digital_twin;
CREATE TABLE patient_diagnosis (

    diagnosis_id BIGINT AUTO_INCREMENT PRIMARY KEY,

    patient_id VARCHAR(50),

    diagnosis_name VARCHAR(200),

    diagnosis_code VARCHAR(30),

    diagnosis_date DATE,

    status VARCHAR(50)
);