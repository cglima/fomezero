import streamlit as st
import streamlit_antd_components as sac
from PIL import Image


# Configuração da página
st.set_page_config(
    page_title="Projeto Fome Zero",
    page_icon="🍽",
    layout="wide",
)

st.title("Fome Zero! Comida para todos")
st.markdown("""---""")

image = Image.open("/home/cassiana/repos/fomezero/images/cuisines.jpg")
st.sidebar.image(image, width=250)

# st.sidebar.title("Menu")
menu_options = ["🧭 Home", "🗺️ Countries", "🏙️ Cities", "🍲 Cuisines"]
choice = st.sidebar.selectbox("Menu", menu_options)
st.sidebar.markdown("""---""")

match choice:
    case "🧭 Home":
        # st.header("Home")
        st.write("### Bem-vindo à página inicial")
        st.markdown("""---""")
        st.markdown(
            """
            ### Como utilizar este Dashboard?
            - Escolha uma opção no menu à esquerda
            - Em cada página, você encontrará informações sobre cada uma das Visões (Countries, Cities, Cuisines)
            - Você pode filtrar as informações usando os filtros disponíveis
            - Você pode clicar em um item para ver mais detalhes
            """)
    case "🗺️ Countries":
        # st.header("Countries")
        st.write("### Informações sobre os países")
        st.markdown("""---""")
    case "🏙️ Cities":
        # st.header("Cities")
        st.write("### Informações sobre as cidades")
        st.markdown("""---""")
    case "🍲 Cuisines":
        # st.header("Cuisines")
        st.write("### Informações sobre as cozinhas")
        st.markdown("""---""")


st.sidebar.markdown("### Powered by Cassiana Lima Barreto")
