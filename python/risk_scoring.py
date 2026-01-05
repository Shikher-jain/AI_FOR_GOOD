from snowflake_session import get_session

session = get_session()
session.use_database("INSPECTION_DB")
session.use_schema("PUBLIC")

session.sql("""
CREATE OR REPLACE TABLE ROOM_RISK_LEVEL AS
SELECT *,
CASE
    WHEN RISK_SCORE < 3 THEN 'LOW'
    WHEN RISK_SCORE < 7 THEN 'MEDIUM'
    ELSE 'HIGH'
END AS RISK_LEVEL
FROM (
    SELECT
        PROPERTY_ID,
        ROOM_ID,
        SUM(
            CASE DEFECT
                WHEN 'damp' THEN 3
                WHEN 'crack' THEN 4
                WHEN 'exposed wiring' THEN 5
                WHEN 'poor finishing' THEN 2
                WHEN 'structural risk' THEN 6
                ELSE 0
            END * CONFIDENCE
        ) AS RISK_SCORE
    FROM DEFECTS
    GROUP BY PROPERTY_ID, ROOM_ID
)
""").collect()
print("Risk scoring completed")
