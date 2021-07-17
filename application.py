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