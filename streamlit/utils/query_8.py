from utils.generic import run_query
import random

def query(year=2000, 
          qoy = random.randint(1,2), 
          ZIP=[random.randint(10000,99999) for i in range(400)], 
          limit=10):
    query = f"""
    select s_store_name, sum(ss_net_profit)
    from store_sales, date_dim, store,
        (select ca_zip
            from (
            SELECT substr(ca_zip,1,5) ca_zip
            FROM customer_address
            WHERE substr(ca_zip,1,5) IN {tuple(ZIP)}
        intersect
        select ca_zip
        from (SELECT substr(ca_zip,1,5) ca_zip,count(*) cnt
                FROM customer_address, customer
                WHERE ca_address_sk = c_current_addr_sk and
                    c_preferred_cust_flag='Y'
                group by ca_zip
                having count(*) > 10)A1)A2) V1
    where ss_store_sk = s_store_sk
    and ss_sold_date_sk = d_date_sk
    and d_qoy = {qoy} and d_year = {year}
    and (substr(s_zip,1,2) = substr(V1.ca_zip,1,2))
    group by s_store_name
    order by s_store_name
    limit {limit};"""
    df = run_query(query)
    df.rename(columns = {"S_STORE_NAME": "Store Name", "SUM(SS_NET_PROFIT)": "Net profit"}, inplace=True)
    return df
