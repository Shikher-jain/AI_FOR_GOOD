from snowflake_session import get_session

if __name__ == "__main__":
    try:
        session = get_session()
        result = session.sql("SELECT CURRENT_VERSION() AS VERSION").collect()
        print(f"Snowflake connection successful! Version: {result[0]['VERSION']}")
    except Exception as e:
        print(f"Snowflake connection failed: {e}")
