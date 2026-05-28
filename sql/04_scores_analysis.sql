-- 04_scores_analysis.sql
-- Moyenne des scores de service

SELECT
    AVG(departure_arrival_conv_score) as avg_departure_arrival_conv,
    AVG(online_booking_score) as avg_online_booking,
    AVG(checkin_service_score) as avg_checkin,
    AVG(online_boarding_score) as avg_online_boarding,
    AVG(gate_location_score) as avg_gate,
    AVG(onboard_service_score) as avg_onboard,
    AVG(seat_comfort_score) as avg_seat,
    AVG(legroom_score) as avg_legroom,
    AVG(cleanliness_score) as avg_cleanliness,
    AVG(food_drink_score) as avg_food,
    AVG(inflight_service_score) as avg_inflight_service,
    AVG(wifi_score) as avg_wifi,
    AVG(entertainment_score) as avg_entertainment,
    AVG(baggage_score) as avg_baggage
FROM FACT_REVIEW;