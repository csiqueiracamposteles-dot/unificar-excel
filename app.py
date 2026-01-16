import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Unificar Excel", layout="centered")

st.title("Unificador de arquivos Excel")

uploaded_files = st.file_uploader(
    "Selecione todos os arquivos Excel",
    type=["xlsx", "xls"],
    accept_multiple_files=True
)

if uploaded_files:
    lista_dfs = []

    for file in uploaded_files:
        df = pd.read_excel(file)
        lista_dfs.append(df)

    df_final = pd.concat(lista_dfs, ignore_index=True)

    buffer = BytesIO()
    df_final.to_excel(buffer, index=False)
    buffer.seek(0)

    st.success("Arquivos unificados com sucesso!")

    st.download_button(
        label="Baixar Excel unificado",
        data=buffer,
        file_name="arquivo_unificado.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
