import os

import streamlit as st
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv


def get_config_value(secret_key: str, env_key: str) -> str:
    """Prefer Streamlit secrets, fall back to .env/.environment variables."""
    if secret_key in st.secrets:
        return st.secrets[secret_key]
    return os.getenv(env_key)


def build_connection():
    env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
    load_dotenv(env_path)
    return snowflake.connector.connect(
        user=get_config_value("snowflake_user", "SNOWFLAKE_USER"),
        password=get_config_value("snowflake_password", "SNOWFLAKE_PASSWORD"),
        account=get_config_value("snowflake_account", "SNOWFLAKE_ACCOUNT"),
        warehouse=get_config_value("snowflake_warehouse", "SNOWFLAKE_WAREHOUSE"),
        database=get_config_value("snowflake_database", "SNOWFLAKE_DATABASE"),
        schema=get_config_value("snowflake_schema", "SNOWFLAKE_SCHEMA"),
    )


conn = build_connection()

st.title("🏠 AI Housing Inspection Dashboard")

# Fetch property IDs
property_ids = pd.read_sql("SELECT PROPERTY_ID FROM PROPERTY", conn)
property_id = st.selectbox("Select Property", property_ids["PROPERTY_ID"])

# Fetch summary
summary_query = "SELECT SUMMARY FROM PROPERTY_SUMMARY WHERE PROPERTY_ID = %s"
summary = pd.read_sql(summary_query, conn, params=[property_id])
st.subheader("Inspection Summary")
if not summary.empty:
    st.write(summary.loc[0, "SUMMARY"])
else:
    st.write("No summary available.")

# Fetch room-wise risk
risk_query = "SELECT * FROM ROOM_RISK_LEVEL WHERE PROPERTY_ID = %s"
risk = pd.read_sql(risk_query, conn, params=[property_id])
st.subheader("Room-wise Risk")
st.dataframe(risk)
