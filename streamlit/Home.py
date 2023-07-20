import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Home Page",
    page_icon="👋",
)

st.title("TPC DS Queries Snoflake")

st.markdown(
    """
    Application to integrate TPC-DS queries of snowflake with Streamlit
    """
)

# Run the app
# streamlit run main.py
