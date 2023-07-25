import streamlit as st
import string
from utils.query_10 import query  
from utils import generic


@st.cache_data
def input_elements():
   
    years = generic.distinct_years()
    months = generic.distinct_months()
    counties = generic.distinct_counties()
    return years, months, counties

st.set_page_config(
    page_title="Home Page",
    page_icon="👋",
)

st.title("TPC DS Queries Snoflake")

st.markdown(
    """
    """
)
if not st.session_state["authentication_status"]:
    st.warning('Access Denied! Please authenticate yourself on Home Page.', icon="⚠️")
else:
    years, months, counties = input_elements()


    year = st.number_input('Year', min_value=min(years), max_value=max(years))
    month = st.number_input('Month', min_value=min(months), max_value=max(months))
    county = st.multiselect('COUNTY', counties)
    limit = st.number_input('Limit result', min_value=5, max_value=100)

    if st.button("Aggregate"):
        with st.spinner(text="Fetching..."):
            df = query(
                year=year, 
                month = month,
                county = county,
                limit=10
            )
        st.write(df)
