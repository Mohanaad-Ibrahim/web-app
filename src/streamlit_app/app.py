import os, sys
_here = os.path.dirname(os.path.abspath(__file__))  
_src  = os.path.abspath(os.path.join(_here, ".."));     sys.path.insert(0, _here);          sys.path.insert(0, _src) 
import streamlit as st 
import pandas as pd 
from services.db import DatabaseManager
# cd src && python -m streamlit run streamlit_app/app.py

database_manager = DatabaseManager()


st.title("sign up page ")
username = st.text_input("enter your username ")
password = st.text_input("enter your password ")
email = st.text_input("enter your email ")
user_box , password_box, email_box = st.columns(3)
user_box.write(username)
password_box.write(password)
email_box.write(email)


if st.button("submit"):
    database_manager.insert_into_users_table(username=username,password=password,email=email)
    st.success("data insert ssuccessfully ")