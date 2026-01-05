from snowflake_session import get_session
import os

session = get_session()
session.use_database("INSPECTION_DB")
session.use_schema("PUBLIC")

sql_path = os.path.join(os.path.dirname(__file__), "..", "sql", "04_llm_summary.sql")
session.sql(open(sql_path).read()).collect()
print("Summary generation completed")
