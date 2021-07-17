from scipy.sparse import data
import streamlit as st
import components as comp
import pandas as pd
import base64

st.set_page_config(layout="wide", page_title="Missing Columnizer")

sidebar_title = st.sidebar.title("Missing Value Evaluation")
upload = st.sidebar.file_uploader(label="⏫ Upload your file here ⏫")

data_import, column_sidebar = comp.file_uploading(upload)

left, right = st.beta_columns(2)

left_title = left.title("Method Implementer")
right_title = right.title("Method Evaluation")

# left_delete = left.subheader("Row Deletion Method")
with left.beta_expander(label="Delete Row Method"):
    left_delete_dataframe = st.dataframe(comp.delete_rows(data_import, column_sidebar))


with left.beta_expander(label="Mean Imputation Method"):
    left_mean_dataframe = comp.mean_rows(data_import, column_sidebar)
    st.dataframe(comp.mean_rows(data_import, column_sidebar))

with left.beta_expander(label="Median Imputation Method"):
    left_median_dataframe = comp.median_rows(data_import, column_sidebar)
    st.dataframe(comp.median_rows(data_import, column_sidebar))

with left.beta_expander(label="Linear Regression Method"):
    left_linear_regression = st.subheader("Linear Regression Method")
    left_linear_select_box = comp.linear_regression_variable_selector(data_import, column_sidebar)
    left_linear_dataframe = comp.linear_regression_rows(data_import, left_linear_select_box, column_sidebar)
    st.dataframe(comp.linear_regression_rows(data_import, left_linear_select_box, column_sidebar))


summary_blurb_one = right.subheader(comp.methodology_report(data_import, 
                                         left_delete_dataframe, 
                                         left_mean_dataframe,
                                         left_median_dataframe,
                                         left_linear_dataframe,
                                         column_sidebar)[0])

summary_blurb_two = right.subheader(comp.methodology_report(data_import, 
                                         left_delete_dataframe, 
                                         left_mean_dataframe,
                                         left_median_dataframe,
                                         left_linear_dataframe,
                                         column_sidebar)[1])

summary_blurb_three = right.subheader(comp.methodology_report(data_import, 
                                         left_delete_dataframe, 
                                         left_mean_dataframe,
                                         left_median_dataframe,
                                         left_linear_dataframe,
                                         column_sidebar)[2])

summary_blurb_four = right.subheader(comp.methodology_report(data_import, 
                                         left_delete_dataframe, 
                                         left_mean_dataframe,
                                         left_median_dataframe,
                                         left_linear_dataframe,
                                         column_sidebar)[3])


# delete_download=st.button('Download Delete Method File')
# if delete_download:
#     'Download Started!'
#     csv = left_delete_dataframe.to_csv(index=False)
#     b64 = base64.b64encode(csv.encode()).decode()  # some strings
#     linko= f'<a href="data:file/csv;base64,{b64}" download="myfilename.csv">Download csv file</a>'
#     st.markdown(linko, unsafe_allow_html=True)