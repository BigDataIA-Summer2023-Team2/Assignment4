import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

USERNAME=os.environ.get("username")
PASSWORD=os.environ.get("password")
ACCOUNT_IDENTIFIER=os.environ.get("accountname")

def run_query(query):
    engine = create_engine(
        'snowflake://{user}:{password}@{account_identifier}/snowflake_sample_data/tpcds_sf10Tcl'.format(
            user=USERNAME,
            password=PASSWORD,
            account_identifier=ACCOUNT_IDENTIFIER,
        )
    )
    try:
        connection = engine.connect()
        df = pd.read_sql(query, connection)
        return df
    finally:
        connection.close()
        engine.dispose()

def distinct_years():
    query = "select distinct d_year from date_dim"
    df = run_query(query)
    return df["d_year"].values.tolist()

def distinct_marital_status():
    query = "select distinct cd_marital_status from customer_demographics"
    df = run_query(query) 
    return df["cd_marital_status"].values.tolist()

def distinct_education_status():
    query = "select distinct cd_education_status from customer_demographics"
    df = run_query(query) 
    return df["cd_education_status"].values.tolist()
    
def distinct_gender():
    query = "select distinct cd_gender from customer_demographics"
    df = run_query(query) 
    return df["cd_gender"].values.tolist()

def distinct_qoys():
    query = "select distinct d_qoy from date_dim"
    df = run_query(query) 
    return df["d_qoy"].values.tolist()

def distinct_zips():
    query = "select distinct ca_zip from customer_address"
    df = run_query(query) 
    return df["ca_zip"].values.tolist()
