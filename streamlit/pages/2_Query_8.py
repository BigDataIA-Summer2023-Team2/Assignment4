import streamlit as st
from utils.query_8 import query
from utils import generic


@st.cache_data
def input_elements():
    genders = generic.distinct_gender()
    years = generic.distinct_years()
    qoys = generic.distinct_qoys()
    zips = generic.distinct_zips()
    return years, qoys, zips

st.set_page_config(
    page_title="Query 8",
    page_icon="👋",
)

st.title("TPC DS Queries Snoflake")

st.markdown(
    """
    Compute the net profit of stores located in 400 Metropolitan areas with more than 10 preferred customers.
    """
)
years, qoys, zips = input_elements()

year = st.number_input('Year', min_value=min(years), max_value=max(years))
qoy = st.number_input('QOY', min_value=min(qoys), max_value=max(qoys))
zips = st.multiselect('ZIP codes', zips)
limit = st.number_input('Limit result', min_value=5, max_value=100)

if st.button("Aggregate"):
    with st.spinner(text="Fetching..."):
        df = query(
            year=year,
            qoy = qoy, 
            ZIP=zips, 
            limit=limit
        )
    st.write(df)
