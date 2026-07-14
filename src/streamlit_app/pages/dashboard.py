import streamlit as st 
import pandas as pd 
from src.services.db import DatabaseManager

database_manager = DatabaseManager()


st.title("Dashboard")
num_rows = st.number_input("enter of num of rows")



