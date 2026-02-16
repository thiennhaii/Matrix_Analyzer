import streamlit as st
import pandas as pd
import numpy as np
import matrix_logic as ml

#Khoi tao
if "not_transposed" not in st.session_state:
    st.session_state.is_transposed = False
if "not_determinant" not in st.session_state:
    st.session_state.determinant = False
if "not_rank" not in st.session_state:
    st.session_state.not_rank = False
if "not_inversed" not in st.session_state:
    st.session_state.not_inversed = False
if "not_qr" not in st.session_state:
    st.session_state.not_qr = False
if "not_cheoHoa" not in st.session_state:
    st.session_state.not_cheoHoa = False
if "not_svd" not in st.session_state:
    st.session_state.svd = False

#Callbacks
def to_transpose():
    st.session_state.not_transposed = True
def to_determinant():
    st.session_state.not_determinant = True
def to_rank():
    st.session_state.not_rank = True
def to_inverse():
    st.session_state.not_inversed = True
def to_qr():
    st.session_state.not_qr = True
def to_cheoHoa():
    st.session_state.not_cheoHoa = True
def to_svd():
    st.session_state.not_svd = True

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
    transposed_matrix = ml.transpose_matrix(editable_df)
    st.dataframe(transposed_matrix.astype(int))

st.button("Determinant", on_click = to_determinant )
if st.session_state.get("not_determinant"):
    deter = ml.determinant(editable_df)
    if type(deter) == str:
        st.write(deter)
    else:
        st.write(round(deter,5))

st.button("Rank", on_click = to_rank)
if st.session_state.get("not_rank"):
    matrix_rank = ml.rank(editable_df)
    st.write(matrix_rank.astype(int))

st.button("Inverse Matrix", on_click = to_inverse)
if st.session_state.get("not_inversed"):
    inversed_matrix = ml.inverse(editable_df)
    if type(inversed_matrix) != str:
        st.dataframe(inversed_matrix)
    else:
        st.write(inversed_matrix)

st.button("QR Factorization", on_click = to_qr)
if st.session_state.get("not_qr"):
    Q, R = ml.qr_factorization(editable_df)
    st.write("Q:")
    st.dataframe(Q)
    st.write("R:")
    st.dataframe(R)

st.button("Cheo Hoa", on_click = to_cheoHoa)
if st.session_state.get("not_cheoHoa"):
    if editable_df.shape[0] != editable_df.shape[1]:
        st.write("Khong la ma tran vuong")
    else:
        P, D, P_inverse = ml.cheo_hoa(editable_df)
        st.write("P:")
        st.dataframe(P)
        st.write("D:")
        st.dataframe(D)
        st.write("P^-1:")
        st.dataframe(P_inverse)

st.button("SVD", on_click = to_svd)
if st.session_state.get("not_svd"):
    U, S, Vt = ml.svd(editable_df)
    st.write("U:")
    st.dataframe(U)
    st.write("S:")
    st.dataframe(np.diag(S))
    st.write("Vt:")
    st.dataframe(Vt)