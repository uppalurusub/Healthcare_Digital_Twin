use digital_twin;

CREATE TABLE patient (
    patient_id VARCHAR(50) PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    gender VARCHAR(20),
    age INT,
    date_of_birth DATE,
    phone VARCHAR(20),
    email VARCHAR(100),
    created_at DATETIME,
    updated_at DATETIME
);