-- 01_extraction_dwh.sql
-- Extraction des tables du Data Warehouse pour ML/DL/LLM

-- Extraction FACT_REVIEW (données de satisfaction)
SELECT
    review_sk,
    client_sk,
    time_sk,
    customer_type,
    traveller_type,
    travel_class,
    flight_distance,
    departure_delay,
    arrival_delay,
    departure_arrival_conv_score,
    online_booking_score,
    checkin_service_score,
    online_boarding_score,
    gate_location_score,
    onboard_service_score,
    seat_comfort_score,
    legroom_score,
    cleanliness_score,
    food_drink_score,
    inflight_service_score,
    wifi_score,
    entertainment_score,
    baggage_score,
    satisfaction_status
FROM FACT_REVIEW;

-- Extraction DIM_CLIENT (profils clients)
SELECT
    client_sk,
    loyalty_number,
    country,
    province,
    city,
    gender,
    education,
    salary_band,
    marital_status,
    loyalty_card,
    clv,
    clv_quartile,
    is_churned,
    tenure_months
FROM DIM_CLIENT
WHERE is_current = 1;

-- Extraction DIM_TIME (dimensions temporelles)
SELECT
    time_sk,
    full_date,
    year,
    quarter,
    month_num,
    day_of_week,
    is_weekend
FROM DIM_TIME;