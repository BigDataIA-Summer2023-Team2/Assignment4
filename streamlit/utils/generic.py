import os
import streamlit as st
import random
import pandas as pd
from sqlalchemy import create_engine
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def connection():
    conn = st.experimental_connection('snowpark')
    return conn

@st.cache_data
def run_query(query):    
    conn = connection()
    df = conn.query(query, ttl=600)
    return df
    
@st.cache_data
def distinct_years():
    query = "select distinct d_year from date_dim"
    df = run_query(query)
    return df["D_YEAR"].values.tolist()

@st.cache_data
def distinct_dates():
    query = "select distinct d_date from date_dim"
    df = run_query(query)
    return df["D_DATE"].values.tolist()

@st.cache_data
def distinct_marital_status():
    query = "select distinct cd_marital_status from customer_demographics"
    df = run_query(query) 
    return df["CD_MARITAL_STATUS"].values.tolist()

@st.cache_data
def distinct_education_status():
    query = "select distinct cd_education_status from customer_demographics"
    df = run_query(query) 
    return df["CD_EDUCATION_STATUS"].values.tolist()

@st.cache_data  
def distinct_gender():
    query = "select distinct cd_gender from customer_demographics"
    df = run_query(query) 
    return df["CD_GENDER"].values.tolist()

@st.cache_data
def distinct_counties():
    query = "select distinct ca_county from customer_address"
    df = run_query(query) 
    return df["CA_COUNTY"].values.tolist()

@st.cache_data
def distinct_qoys():
    query = "select distinct d_qoy from date_dim"
    df = run_query(query) 
    return df["D_QOY"].values.tolist()

@st.cache_data
def distinct_zips():
    query = "select distinct ca_zip from customer_address"
    df = run_query(query) 
    return df["CA_ZIP"].values.tolist()

@st.cache_data
def distinct_categories():
    query = "select distinct i_category from item"
    df = run_query(query) 
    return df["I_CATEGORY"].values.tolist()

@st.cache_data
def generate_random_counties(fips_county):
    # Assuming fips_county is a list of unique county names
    num_counties = len(fips_county)
    COUNTY = [fips_county[random.randint(0, len(fips_county) - 1)] for _ in range(10)]
    return COUNTY

@st.cache_data
def distinct_months():
    query = "select distinct d_moy from date_dim"
    df = run_query(query) 
    return df["D_MOY"].values.tolist()
