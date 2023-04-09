import pandas as pd
import streamlit as st

@st.cache
class GetData:
    def __init__(self):
        # self.df_url = "DL_Project/Data_csv/glamping_test.csv"
        self.df_url = "DL_Project/Data_csv/glamping_test_3000.csv"
        self.df = self.load_data()

    def load_data(self):
        try :  
            return pd.read_csv(self.df_url)
            
        except Exception as e : 
            return st.error(e)

    def create_data(self) : return self.df
