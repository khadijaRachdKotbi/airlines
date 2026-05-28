-- 03_analysis_satisfaction.sql
-- Requêtes d'analyse de satisfaction

-- 1. Satisfaction moyenne par type de voyage
SELECT
    traveller_type,
    travel_class,
    COUNT(*) as nb_reviews,
    AVG(seat_comfort_score) as avg_seat,
    AVG(food_drink_score) as avg_food,
    AVG(wifi_score) as avg_wifi,
    SUM(CASE WHEN satisfaction_status = 'Satisfied' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as satisfaction_pct
FROM FACT_REVIEW fr
GROUP BY traveller_type, travel_class
ORDER BY satisfaction_pct DESC;

-- 2. Impact des retards sur satisfaction
SELECT
    CASE
        WHEN arrival_delay < 0 THEN 'Early'
        WHEN arrival_delay <= 15 THEN 'On Time'
        WHEN arrival_delay <= 60 THEN 'Minor Delay'
        ELSE 'Major Delay'
    END as delay_category,
    COUNT(*) as nb_reviews,
    SUM(CASE WHEN satisfaction_status = 'Satisfied' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as satisfaction_pct,
    AVG(seat_comfort_score) as avg_comfort,
    AVG(onboard_service_score) as avg_service
FROM FACT_REVIEW
GROUP BY CASE
    WHEN arrival_delay < 0 THEN 'Early'
    WHEN arrival_delay <= 15 THEN 'On Time'
    WHEN arrival_delay <= 60 THEN 'Minor Delay'
    ELSE 'Major Delay'
END;

-- 3. Évolution temporelle de satisfaction
SELECT
    dt.year,
    dt.quarter,
    COUNT(*) as nb_reviews,
    AVG(fr.departure_arrival_conv_score) as avg_convenience,
    AVG(fr.food_drink_score) as avg_food,
    AVG(fr.wifi_score) as avg_wifi,
    SUM(CASE WHEN fr.satisfaction_status = 'Satisfied' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as satisfaction_pct
FROM FACT_REVIEW fr
JOIN DIM_TIME dt ON fr.time_sk = dt.time_sk
GROUP BY dt.year, dt.quarter
ORDER BY dt.year, dt.quarter;