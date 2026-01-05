from snowflake.snowpark import Session
import os
from dotenv import load_dotenv

def get_session():
    load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
    config = {
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": os.getenv("SNOWFLAKE_USER"),
        "role": os.getenv("SNOWFLAKE_ROLE", "SYSADMIN"),
        "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH"),
        "database": os.getenv("SNOWFLAKE_DATABASE", "INSPECTION_DB"),
        "schema": os.getenv("SNOWFLAKE_SCHEMA", "PUBLIC")
    }
    authenticator = os.getenv("SNOWFLAKE_AUTHENTICATOR")
    if authenticator:
        config["authenticator"] = authenticator
    password = os.getenv("SNOWFLAKE_PASSWORD")
    if password and not authenticator:
        config["password"] = password
    return Session.builder.configs(config).create()
