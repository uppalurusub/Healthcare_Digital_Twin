CREATE TABLE bed_occupancy (

    occupancy_id BIGINT AUTO_INCREMENT PRIMARY KEY,

    hospital_id VARCHAR(50),

    total_beds INT,

    occupied_beds INT,

    icu_beds INT,

    occupied_icu INT,

    occupancy_date DATE
);