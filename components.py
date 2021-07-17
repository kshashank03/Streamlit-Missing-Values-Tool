import pandas as pd
import streamlit as st


def file_uploading(upload):
    if upload is not None:
        data_import = pd.read_csv(upload)
    
        columns = list(data_import.columns)
        column_sidebar = st.sidebar.radio("Which column has missing data?", options= columns)
    
        return data_import, column_sidebar
    
    else:
        return None, None


def delete_rows(data_import, column_name):
    if data_import is not None:
        new_dataframe = data_import[data_import[column_name].notna()]
        
        return new_dataframe
    else:
        return None