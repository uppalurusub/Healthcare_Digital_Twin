CREATE TABLE explainability (

    explanation_id VARCHAR(100) PRIMARY KEY,

    prediction_id VARCHAR(100),

    explanation JSON,

    created_at DATETIME
);