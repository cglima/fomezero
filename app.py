import streamlit as st
import streamlit_antd_components as sac


# Configuração da página
st.set_page_config(
    page_title="Projeto Fome Zero",
    page_icon="🍽",
    layout="wide",
)

st.sidebar.title("Projeto Fome Zero")
st.sidebar.image("images/cuisines.jpg", width=250)

menu_options = ["🏠 Home", "🧭 General Informations",
                "🗺️ Countries", "🏙️ Cities", "🍲 Cuisines"]
choice = st.sidebar.selectbox("", menu_options)
st.sidebar.markdown("""---""")

match choice:
    case "🏠 Home":
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

    case "🧭 General Informations":
        st.write("### Informações Gerais")
        st.markdown("""---""")

    case "🗺️ Countries":
        st.write("### Informações sobre os países")
        st.markdown("""---""")
    case "🏙️ Cities":
        st.write("### Informações sobre as cidades")
        st.markdown("""---""")
    case "🍲 Cuisines":
        st.write("### Informações sobre as cozinhas")
        st.markdown("""---""")

st.markdown("""---""")
st.write("Powered by Cassiana Lima Barreto")
