from sqlalchemy import create_engine
import os
import pandas as pd
import random
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

def query(gender="M", marital_status="S", education="College", year=random.randint(1998, 2002), limit=10):
    query = f"""
        select i_item_id, 
                avg(ss_quantity) agg1,
                avg(ss_list_price) agg2,
                avg(ss_coupon_amt) agg3,
                avg(ss_sales_price) agg4 
        from store_sales, customer_demographics, date_dim, item, promotion
        where ss_sold_date_sk = d_date_sk and
            ss_item_sk = i_item_sk and
            ss_cdemo_sk = cd_demo_sk and
            ss_promo_sk = p_promo_sk and
            cd_gender = '{gender}' and 
            cd_marital_status = '{marital_status}' and
            cd_education_status = '{education}' and
            (p_channel_email = 'N' or p_channel_event = 'N') and
            d_year = {year} 
        group by i_item_id
        order by i_item_id
        limit {limit};
    """
    try:
        connection = engine.connect()
        # results = connection.execute('select current_version()').fetchone()
        # print(results[0])
        df = pd.read_sql(query, connection)
        return df
    finally:
        connection.close()
        engine.dispose()

def distinct_years():
    try:
        query = "select distinct d_year from date_dim"
        connection = engine.connect()
        df = pd.read_sql(query, connection)
        return df["d_year"].values.tolist()
    finally:
        connection.close()
        engine.dispose()

def distinct_marital_status():
    try:
        query = "select distinct cd_marital_status from customer_demographics"
        connection = engine.connect()
        df = pd.read_sql(query, connection)
        return df["cd_marital_status"].values.tolist()
    finally:
        connection.close()
        engine.dispose()

def distinct_education_status():
    try:
        query = "select distinct cd_education_status from customer_demographics"
        connection = engine.connect()
        df = pd.read_sql(query, connection)
        return df["cd_education_status"].values.tolist()
    finally:
        connection.close()
        engine.dispose()

def distinct_gender():
    try:
        query = "select distinct cd_gender from customer_demographics"
        connection = engine.connect()
        df = pd.read_sql(query, connection)
        return df["cd_gender"].values.tolist()
    finally:
        connection.close()
        engine.dispose()

print(distinct_years())
print(distinct_marital_status())
print(distinct_education_status())
print(distinct_gender())
