import random
from utils.generic import run_query
from datetime import datetime,timedelta

def convert_to_yyyy_mm_dd(date):
    # Check if the input date is already a datetime object
    if isinstance(date, datetime):
        formatted_date = date.strftime("%Y-%m-%d")
        return formatted_date
    else:
        try:
            # Parse the input date using the datetime.strptime function
            parsed_date = datetime.strptime(date, "%Y-%m-%d")
            
            # Format the parsed date back to the desired format
            formatted_date = parsed_date.strftime("%Y-%m-%d")
            
            return formatted_date
        except ValueError:
            # Handle the case when the input date is not in the expected format
            return None

def add30days(date):
    # Check if the input date is already a datetime object
    # sdate= convert_to_yyyy_mm_dd(date)
    add30= date + timedelta(days=30)
    edate=convert_to_yyyy_mm_dd(add30)
    return edate


def generate_random_date():
    # Generate a random year between 1900 and 2100
    year = random.randint(1900, 2100)

    # Generate a random month between 1 and 12
    month = random.randint(1, 12)

    # Generate a random day between 1 and 28/30/31, depending on the month and year
    if month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    elif month == 2:
        # Handle February and leap years
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    else:
        day = random.randint(1, 31)

    # Create the date string in "yyyy-mm-dd" format
    date_string = f"{year:04d}-{month:02d}-{day:02d}"

    return date_string


def query(category1="Sports", category2="Books", category3="Home", year=random.randint(1998, 2002), date=generate_random_date(), limit=10):
    categories=[category1,category2,category3]
    query = f"""
        SELECT i_item_id,
            i_item_desc,
            i_category,
            i_class,
            i_current_price,
            sum(ws_ext_sales_price) AS itemrevenue,
            sum(ws_ext_sales_price)*100.0000/sum(sum(ws_ext_sales_price)) OVER (PARTITION BY i_class) AS revenueratio
        FROM web_sales,
            item,
            date_dim
        WHERE ws_item_sk = i_item_sk
            AND i_category IN {tuple(categories)}
            AND ws_sold_date_sk = d_date_sk
            AND d_date BETWEEN cast('{convert_to_yyyy_mm_dd(date)}' as date) AND cast('{add30days(date)}' as date)
        GROUP BY i_item_id,
            i_item_desc,
            i_category,
            i_class,
            i_current_price
        ORDER BY i_category,
            i_class,
            i_item_id,
            i_item_desc,
            revenueratio
        LIMIT {limit};
    """
    return run_query(query)