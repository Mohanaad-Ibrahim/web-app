import streamlit as st 
import pandas as pd 
from services.db import DatabaseManager

database_manager = DatabaseManager()


st.title("Dashboard")
num_rows = int( st.number_input("enter of num of rows", step=1) )




