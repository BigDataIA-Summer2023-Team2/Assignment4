import random
from utils.generic import run_query
import streamlit as st

row_count = 2000000  

#RC = [random.uniform(1, row_count / 5) for _ in range(5)]
RC = [round(random.uniform(1, row_count / 5)) for _ in range(5)]

@st.cache_data
def query(aggcthen, aggcelse= "ss_net_paid", limit=5):
    query = f"""
        select case when (select count(*) 
                  from store_sales 
                  where ss_quantity between 1 and 20) > {int(RC[0])}
            then (select avg({aggcthen}) 
                  from store_sales 
                  where ss_quantity between 1 and 20) 
            else (select avg({aggcelse})
                  from store_sales
                  where ss_quantity between 1 and 20) end bucket1 ,
       case when (select count(*)
                  from store_sales
                  where ss_quantity between 21 and 40) > {int(RC[1])}
            then (select avg({aggcthen})
                  from store_sales
                  where ss_quantity between 21 and 40) 
            else (select avg({aggcelse})
                  from store_sales
                  where ss_quantity between 21 and 40) end bucket2,
       case when (select count(*)
                  from store_sales
                  where ss_quantity between 41 and 60) > {int(RC[2])}
            then (select avg({aggcthen})
                  from store_sales
                  where ss_quantity between 41 and 60)
            else (select avg({aggcelse})
                  from store_sales
                  where ss_quantity between 41 and 60) end bucket3,
       case when (select count(*)
                  from store_sales
                  where ss_quantity between 61 and 80) > {int(RC[3])}
            then (select avg({aggcelse})
                  from store_sales
                  where ss_quantity between 61 and 80)
            else (select avg({aggcelse})
                  from store_sales
                  where ss_quantity between 61 and 80) end bucket4,
       case when (select count(*)
                  from store_sales
                  where ss_quantity between 81 and 100) > {int(RC[4])}
            then (select avg({aggcthen})
                  from store_sales
                  where ss_quantity between 81 and 100)
            else (select avg({aggcelse})
                  from store_sales
                  where ss_quantity between 81 and 100) end bucket5
from reason
where r_reason_sk = 1
limit {limit};
    """
    return run_query(query)
