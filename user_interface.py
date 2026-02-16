import streamlit as st
import pandas as pd
import numpy as np
import matrix_logic as ml

#Khoi tao
if "not_transposed" not in st.session_state:
    st.session_state.is_transposed = False
if "not_determinant" not in st.session_state:
    st.session_state.determinant = False

#Callbacks
def to_transpose():
    st.session_state.not_transposed = True
def to_determinant():
    st.session_state.not_determinant = True

#Tieu de
with st.container(border = True):
    st.title("Analyze Matrice")

#Nhap ma tran
matrix_shape = st.columns(2)
rows = matrix_shape[0].number_input("Nhap so hang:", min_value = 1, step = 1)
cols = matrix_shape[1].number_input("Nhap so cot:", min_value = 1, step = 1)
df_empty = pd.DataFrame(np.zeros((rows, cols)))
editable_df = st.data_editor(df_empty)

#Ket qua
st.button("Transpose", on_click = to_transpose)
if st.session_state.get("not_transposed"):
    resulted_matrix = ml.transpose_matrix(editable_df)
    st.dataframe(resulted_matrix.astype(int))

st.button("Determinant", on_click = to_determinant )
if st.session_state.get("not_determinant"):
    result = ml.determinant(editable_df)
    if type(result) == str:
        st.write(result)
    else:
        st.write(round(result,5))
