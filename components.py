from altair.vegalite.v4.api import value
import pandas as pd
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import base64


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

def linear_regression_rows(data_import, prediction_columns, column_name):
    if len(prediction_columns) > 0:
        # new_data_import = data_import.copy()
        new_dataframe = data_import.copy()
        missing_data = new_dataframe[new_dataframe[column_name].isna()]
        non_missing_data = new_dataframe[new_dataframe[column_name].notna()]

        # Training a model
        y = non_missing_data[column_name]
        X = non_missing_data[prediction_columns]

        reg = LinearRegression().fit(X, y)
        reg.score(X, y)

        # Predict missing values
        X_missing = missing_data[prediction_columns]
        values_to_fill = reg.predict(X_missing)
        values_to_fill = list(values_to_fill)

        # Replacing the missing values with our predictions
        indicies = list(missing_data.index)
        for i in range(0, len(indicies)):
            new_dataframe.loc[indicies[i], column_name] = values_to_fill[i]

        return new_dataframe
    
    else:
        return None


def methodology_report(data_import, delete_dataframe, mean_dataframe, median_dataframe, lin_reg_dataframe, column_name):
    if data_import is not None:
    
        original_mean = str(round(data_import[column_name].mean(), 4))
        
        # delete_mean = delete_dataframe[column_name].mean()
        mean_mean = str(round(mean_dataframe[column_name].mean(), 4))
        median_mean = str(round(median_dataframe[column_name].mean(), 4))
        lin_reg_mean = str(round(lin_reg_dataframe[column_name].mean(), 4))

        summary_original_output = f"The original mean was {original_mean}"
        summary_mean_output = f"The mean using mean imputation is {mean_mean}"
        summary_median_output = f"The mean using median imputation is {median_mean}"
        summary_lin_reg_output = f"The mean using linear regression on selected columns is {lin_reg_mean}"

        return summary_original_output, summary_mean_output, summary_median_output, summary_lin_reg_output

    else:
        None


