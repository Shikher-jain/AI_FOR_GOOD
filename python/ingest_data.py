from snowflake_session import get_session
import pandas as pd
import os

session = get_session()
session.use_database("INSPECTION_DB")
session.use_schema("PUBLIC")

# Ensure the session is using the correct database and schema

base_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_csv_to_sf(filename, table):
    df = pd.read_csv(os.path.join(base_dir, filename))
    session.write_pandas(
        df,
        table_name=table,
        auto_create_table=True,
        overwrite=True
    )

load_csv_to_sf('property.csv', 'PROPERTY')
load_csv_to_sf('room.csv', 'ROOM')
load_csv_to_sf('inspection_note.csv', 'INSPECTION_NOTE')
load_csv_to_sf('image_metadata.csv', 'IMAGE_METADATA')
