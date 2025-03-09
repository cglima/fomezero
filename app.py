import streamlit as st


# Configuração da página
st.set_page_config(
    page_title="Projeto Fome Zero",
    page_icon="🍽",
    layout="wide",
)

st.sidebar.title("Projeto Fome Zero")
# st.sidebar.image("images/cuisines.jpg", width=250)
st.sidebar.markdown("""---""")
st.sidebar.write("## Menu de Navegação")
menu_options = ["🏠 Home", "🧭 General Informations",
                "🗺️ Countries", "🏙️ Cities", "🍲 Cuisines"]
choice = st.sidebar.selectbox("", menu_options)
st.sidebar.markdown("""---""")
st.sidebar.markdown("### Powered by Cassiana Lima Barreto")


match choice:
    case "🏠 Home":
        import visoes.home as home
        home.app()
    case "🧭 General Informations":
        import visoes.general_informations as general_informations
        general_informations.app()
    case "🗺️ Countries":
        import visoes.countries as countries
        countries.app()
    case "🏙️ Cities":
        import visoes.cities as cities
        cities.app()
    case "🍲 Cuisines":
        import visoes.cuisines as cuisines
        cuisines.app()

st.markdown("""---""")
st.write("Powered by Cassiana Lima Barreto")
