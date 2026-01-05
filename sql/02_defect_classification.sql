-- Simplified text classification using pattern matching (no Cortex required)
CREATE OR REPLACE TABLE TEXT_DEFECTS AS
SELECT
    NOTE_ID,
    ROOM_ID,
    CASE
        WHEN LOWER(TEXT) LIKE '%damp%' OR LOWER(TEXT) LIKE '%moisture%' OR LOWER(TEXT) LIKE '%water%' THEN 'damp'
        WHEN LOWER(TEXT) LIKE '%crack%' OR LOWER(TEXT) LIKE '%fracture%' THEN 'crack'
        WHEN LOWER(TEXT) LIKE '%wiring%' OR LOWER(TEXT) LIKE '%electrical%' OR LOWER(TEXT) LIKE '%wire%' THEN 'exposed wiring'
        WHEN LOWER(TEXT) LIKE '%finishing%' OR LOWER(TEXT) LIKE '%paint%' THEN 'poor finishing'
        WHEN LOWER(TEXT) LIKE '%structural%' OR LOWER(TEXT) LIKE '%beam%' OR LOWER(TEXT) LIKE '%foundation%' THEN 'structural risk'
        ELSE 'safe'
    END AS DEFECT,
    0.85 AS CONFIDENCE
FROM INSPECTION_NOTE;
