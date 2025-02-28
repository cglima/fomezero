import streamlit as st
import streamlit_antd_components as sac


# Configuração da página
st.set_page_config(
    page_title="Projeto Fome Zero",
    page_icon="🍽",
    layout="wide",
)

st.title("Projeto Fome Zero")

st.sidebar.title("Menu")
menu_options = ["Main Page", "Countries", "Cities", "Cuisines"]
choice = st.sidebar.selectbox("Selecione uma opção", menu_options)
