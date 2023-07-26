import streamlit as st
from utils.query_9 import query
from utils import generic

st.set_page_config(
    page_title="Query 9",
    page_icon="👋",
)

st.title("TPC DS Query 9")

st.markdown(
    """
   Categorize store sales transactions into 5 buckets according to the number of items sold. Each bucket contains
the average discount amount, sales price, list price, tax, net paid, paid price including tax, or net profit..
    """
)

#RC1, RC2, RC3, RC4, RC5= input_elements()
if not st.session_state["authentication_status"]:
    st.warning('Access Denied! Please authenticate yourself on Home Page.', icon="⚠️")
else:
 aggcthen = ["ss_ext_discount_amt","ss_ext_sales_price","ss_ext_list_price","ss_ext_tax"]
 aggcelse = ["ss_net_paid","ss_net_paid_inc_tax","ss_net_profit"]


 page_names = ['Aggcthen', 'Aggcelse'] 
 page = st.radio('Select one Aggregate',page_names)
 st.write ("return:", page)


if page == 'Aggcthen':
    st.subheader("Select one Aggregate")
    Aggcthen = st.selectbox('Aggthen', aggcthen )
    result1 = Aggcthen
    result2="ss_net_paid"

else:
     st.subheader("Select one")
     Aggcelse = st.selectbox('Aggelse', aggcelse )
     result2 = Aggcelse
     result1="ss_ext_discount_amt"

      
#RC1 = st.number_input("Enter an integer:", step=1)
#RC2 = st.number_input("Enter an integer:", step=2)
#RC3 = st.number_input("Enter an integer:", step=3)
#RC4 = st.number_input("Enter an integer:", step=4)
#RC5 = st.number_input("Enter an integer:", step=5)

limit = st.number_input('Limit result', min_value=5, max_value=100)

if st.button("Aggregate"):
        with st.spinner(text="Fetching..."):
            df = query(
                aggcthen=result1,
                aggcelse=result2,
                limit=limit
            )
        st.write(df)
