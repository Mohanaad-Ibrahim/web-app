import streamlit as st 
import pandas as pd 
from src.services.db import DatabaseManager

database_manager = DatabaseManager()


st.title("sign up page ")
username = st.text_input("enter your username ")
password = st.text_input("enter your password ")
user_box , password_box = st.columns(2)
user_box.write(username)
password_box.write(password)
