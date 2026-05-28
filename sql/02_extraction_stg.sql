-- 02_extraction_stg.sql
-- Extraction des tables de staging pour enrichissement

-- Extraction airlines_reviews (avis textuels)
SELECT
    Title,
    Name,
    Review_Date,
    Airline,
    Verified,
    Reviews,
    Type_of_Traveller,
    Month_Flown,
    Route,
    Class,
    Seat_Comfort,
    Staff_Service,
    Food_Beverages,
    Inflight_Entertainment,
    Value_For_Money,
    Overall_Rating,
    Recommended
FROM airlines_reviews;

-- Extraction customer_emotions (données images - pour CV)
SELECT
    id,
    emotion,
    image_name
FROM customer_emotions
WHERE emotion IN ('happy', 'sad', 'angry', 'neutral', 'surprise');