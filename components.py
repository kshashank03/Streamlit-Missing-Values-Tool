import pandas as pd
import streamlit as st
import numpy as np


def file_uploading(upload):
    if upload is not None:
        data_import = pd.read_csv(upload)
    
        columns = list(data_import.columns)
        for i in columns: # Only keep the numerical columns (can expand to categorical data later)
            if data_import[i].dtype != np.float64 or data_import[i].dtype != np.int64 == columns:
                columns.remove(i)

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

def mean_rows(data_import, column_name):
    if data_import is not None:
        new_dataframe = data_import.copy()
        new_dataframe[column_name].fillna(data_import[column_name].mean(), inplace=True)
        
        return new_dataframe
    else:
        return None

def median_rows(data_import, column_name):
    if data_import is not None:
        new_dataframe = data_import.copy()
        new_dataframe[column_name].fillna(data_import[column_name].median(), inplace=True)
        
        return new_dataframe
    else:
        return None


def linear_regression_variable_selector(data_import, column_name):
    if data_import is not None:
        column_options = [i if i!=column_name else '' for i in data_import.columns]
        lin_reg_select_box = st.multiselect(label="Choose Columns for Prediction", options=column_options)
        return lin_reg_select_box
    else:
        return None