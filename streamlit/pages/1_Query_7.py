import streamlit as st
from utils.query_7 import query

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
    Qualification Substitution Parameters:
     YEAR.01=2000
     ES.01=College
     MS.01=S
     GEN.01=M
    """
)

gender = st.selectbox('Gender', ('M', 'F'))
marital_status = st.selectbox('Marital Status', ('S'))
education = st.selectbox('Education', ('College'))
year = st.number_input('Year', min_value=1998, max_value=2002)
limit = st.number_input('Limit result', min_value=5, max_value=100)

if st.button("Aggregate"):
    with st.spinner(text="Fetching..."):
        df = query()
    st.write(df)
