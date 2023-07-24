import streamlit as st
from utils.query_7 import query
from utils import generic


@st.cache_data
def input_elements():
    genders = generic.distinct_gender()
    years = generic.distinct_years()
    marital_statuses = generic.distinct_marital_status()
    education_statuses = generic.distinct_education_status()
    return genders, years, marital_statuses, education_statuses

st.set_page_config(
    page_title="Home Page",
    page_icon="👋",
)

st.title("TPC DS Queries Snoflake")

st.markdown(
    """
    Compute the average quantity, list price, discount, and sales price for promotional items sold in stores where the
    promotion is not offered by mail or a special event. Restrict the results to a specific gender, marital and
    educational status.
    """
)
genders, years, marital_statuses, education_statuses = input_elements()

gender = st.selectbox('Gender', genders)
marital_status = st.selectbox('Marital Status', marital_statuses)
education = st.selectbox('Education', education_statuses)
year = st.number_input('Year', min_value=min(years), max_value=max(years))
limit = st.number_input('Limit result', min_value=5, max_value=100)

if st.button("Aggregate"):
    with st.spinner(text="Fetching..."):
        df = query(
            gender=gender, 
            marital_status=marital_status, 
            education=education, 
            year=year, 
            limit=10
        )
    st.write(df)
