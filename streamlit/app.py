
import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine




# Robust config getter: sectioned secrets, flat secrets, or env var
def get_config_value(key: str, env_key: str) -> str:
    # st.secrets["snowflake"][key]
    if "snowflake" in st.secrets and key in st.secrets["snowflake"]:
        return st.secrets["snowflake"][key]
    # st.secrets[key]
    if key in st.secrets:
        return st.secrets[key]
    # Environment variable
    return os.getenv(env_key, "")



# Get Snowflake credentials
user = get_config_value("snowflake_user", "SNOWFLAKE_USER")
password = get_config_value("snowflake_password", "SNOWFLAKE_PASSWORD")
account = get_config_value("snowflake_account", "SNOWFLAKE_ACCOUNT")
warehouse = get_config_value("snowflake_warehouse", "SNOWFLAKE_WAREHOUSE")
database = get_config_value("snowflake_database", "SNOWFLAKE_DATABASE")
schema = get_config_value("snowflake_schema", "SNOWFLAKE_SCHEMA")

# Create SQLAlchemy engine for Snowflake
engine = create_engine(
    f"snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}"
)




st.title("🏠 AI Housing Inspection Dashboard")

# Fetch property IDs
property_ids = pd.read_sql("SELECT PROPERTY_ID FROM PROPERTY", engine)
property_id = st.selectbox("Select Property", property_ids["PROPERTY_ID"])

# Fetch summary
summary_query = "SELECT SUMMARY FROM PROPERTY_SUMMARY WHERE PROPERTY_ID = %s"
summary = pd.read_sql(summary_query, engine, params=[property_id])
st.subheader("Inspection Summary")
if not summary.empty:
    st.write(summary.loc[0, "SUMMARY"])
else:
    st.write("No summary available.")

# Fetch room-wise risk
risk_query = "SELECT * FROM ROOM_RISK_LEVEL WHERE PROPERTY_ID = %s"
risk = pd.read_sql(risk_query, engine, params=[property_id])
st.subheader("Room-wise Risk")
st.dataframe(risk)
