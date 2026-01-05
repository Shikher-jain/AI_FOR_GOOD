-- Simplified summary generation without LLM
CREATE OR REPLACE TABLE PROPERTY_SUMMARY AS
SELECT
    PROPERTY_ID,
    CONCAT(
        'Inspection Report for Property ', PROPERTY_ID, ': ',
        'Total defects found: ', COUNT(*), '. ',
        'Defects include: ', LISTAGG(DISTINCT DEFECT, ', '), '. ',
        'Recommended action: ', 
        CASE 
            WHEN SUM(CASE WHEN DEFECT IN ('structural risk', 'exposed wiring') THEN 1 ELSE 0 END) > 0 
            THEN 'Immediate attention required for safety concerns.'
            ELSE 'Minor repairs recommended before occupancy.'
        END
    ) AS SUMMARY
FROM DEFECTS
GROUP BY PROPERTY_ID;
