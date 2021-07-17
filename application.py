import streamlit as st
import components as comp
import pandas as pd

st.set_page_config(layout="wide", page_title="Missing Columnizer")

sidebar_title = st.sidebar.title("Missing Value Evaluation")
upload = st.sidebar.file_uploader(label="⏫ Upload your file here ⏫")

data_import, column_sidebar = comp.file_uploading(upload)

left, right = st.beta_columns(2)

left_title = left.title("Method Implementer")
right_title = right.title("Method Evaluation")

# left_delete = left.subheader("Row Deletion Method")
with left.beta_expander(label="Delete Row Method"):
    left_delete_dataframe = st.write(comp.delete_rows(data_import, column_sidebar))


with left.beta_expander(label="Mean Imputation Method"):
    left_mean_replace = st.subheader("Mean Imputation Method")

with left.beta_expander(label="Median Imputation Method"):
    left_median_replace = st.subheader("Median Imputation Method")

with left.beta_expander(label="Linear Regression Method"):
    left_linear_regression = st.subheader("Linear Regression Method")







