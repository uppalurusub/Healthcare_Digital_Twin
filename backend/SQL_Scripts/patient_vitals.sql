use digital_twin;
CREATE TABLE patient_vitals (

    vital_id BIGINT AUTO_INCREMENT PRIMARY KEY,

    patient_id VARCHAR(50),

    height_cm DECIMAL(5,2),

    weight_kg DECIMAL(5,2),

    bmi DECIMAL(5,2),

    blood_pressure VARCHAR(20),

    heart_rate INT,

    respiratory_rate INT,

    spo2 DECIMAL(5,2),

    temperature DECIMAL(5,2),

    recorded_at DATETIME,

    FOREIGN KEY(patient_id)
        REFERENCES patient(patient_id)
);