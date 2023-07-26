import streamlit as st
from utils.query_12 import query
from utils import generic
import datetime


@st.cache_data
def input_elements():
    categories = generic.distinct_categories()
    years = generic.distinct_years()
    dates = generic.distinct_dates()
    return categories, years, dates

if "authentication_status" not in st.session_state:
    st.session_state["authentication_status"] = False

st.set_page_config(
    page_title="Query12",
    page_icon="👋",
)

st.title("TPC DS Queries 12")

st.markdown(
    """
    Compute the revenue ratios across item classes: For each item in a list of given categories, during a 30 day time
    period, sold through the web channel compute the ratio of sales of that item to the sum of all of the sales in that
    item's class.
    """
)
if not st.session_state["authentication_status"]:
    st.warning('Access Denied! Please authenticate yourself on Home Page.', icon="⚠️")
else:
    categories, years, dates= input_elements()

    category1 = st.selectbox('Cateogry 1', categories)
    category2 = st.selectbox('Cateogry 2', categories)
    category3 = st.selectbox('Cateogry 3', categories)
    # year = st.number_input('Year', min_value=min(years), max_value=max(years))
    year = st.selectbox("Select Year", years)
                        # range(1990, datetime.now().year + 1))
    start_date = datetime.datetime(year, 1, 1)
    end_date = datetime.datetime(year, 12, 31)
    selected_start_date = st.slider("Select Start Date", start_date, end_date, value=start_date)
    # date = st.number_input('Date', min_value=min(dates), max_value=max(dates))
    limit = st.number_input('Limit result', min_value=5, max_value=100)

    if st.button("Aggregate"):
        with st.spinner(text="Fetching..."):
            df = query(
                category1=category1,
                category2=category2,
                category3=category3,  
                year=year, 
                date=selected_start_date,
                limit=10
            )
        st.write(df)
