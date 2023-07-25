import streamlit as st
import streamlit_authenticator as stauth
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

import yaml
from yaml.loader import SafeLoader
with open('credentials.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

# Run the app
# streamlit run main.py
