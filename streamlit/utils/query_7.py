from sqlalchemy import create_engine
import os
import pandas as pd
import random
from utils.generic import run_query
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
    return run_query(query)
