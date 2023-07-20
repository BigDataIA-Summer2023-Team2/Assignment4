import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

USERNAME=os.environ.get("username")
PASSWORD=os.environ.get("password")
ACCOUNT_IDENTIFIER=os.environ.get("accountname")

engine = create_engine(
    'snowflake://{user}:{password}@{account_identifier}/snowflake_sample_data/tpcds_sf10Tcl'.format(
        user=USERNAME,
        password=PASSWORD,
        account_identifier=ACCOUNT_IDENTIFIER,
    )
)

def run_query(query):
    try:
        connection = engine.connect()
        df = pd.read_sql(query, connection)
        return df
    finally:
        connection.close()
        engine.dispose()
