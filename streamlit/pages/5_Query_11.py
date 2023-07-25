import streamlit as st
from utils.query_11 import query
from utils import generic


@st.cache_data
def input_elements():
    years = generic.distinct_years()
    return years

if "authentication_status" not in st.session_state:
    st.session_state["authentication_status"] = False
    
st.set_page_config(
    page_title="Query11",
    page_icon="👋",
)

st.title("TPC DS Queries 11")

st.markdown(
    """
    Find customers whose increase in spending was large over the web than in stores this year compared to last
    year.
    """
)
if not st.session_state["authentication_status"]:
    st.warning('Access Denied! Please authenticate yourself on Home Page.', icon="⚠️")
else:
    years = input_elements()
    selone = ["t_s_secyear.customer_preferred_cust_flag",
                                "t_s_secyear.customer_birth_country",
                                "t_s_secyear.customer_login",
                                "t_s_secyear.customer_email_address"]
    year = st.number_input('Year', min_value=min(years), max_value=max(years))
    SELECTONE = st.selectbox('SELCTONE', selone )
    limit = st.number_input('Limit result', min_value=5, max_value=100)

    if st.button("Aggregate"):
        with st.spinner(text="Fetching..."):
            df = query(
                selectone=SELECTONE, 
                year=year, 
                limit=10)
        st.write(df)
