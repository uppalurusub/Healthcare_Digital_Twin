
use digital_twin;
CREATE TABLE laboratory_result (

    lab_result_id BIGINT AUTO_INCREMENT PRIMARY KEY,

    patient_id VARCHAR(50),

    test_name VARCHAR(200),

    result_value VARCHAR(100),

    normal_range VARCHAR(100),

    result_date DATETIME
);