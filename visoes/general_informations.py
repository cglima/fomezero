import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

DATA_PATH = "dataset/zomato_curated.csv"


def app():
    # st.write("# Informações Gerais")
    st.write(
        "## Descubra seu próximo restaurante favorito no melhor destino gastronômico!")
    st.write("Confira as marcas que compõem nossa plataforma e surpreenda-se!")
    st.markdown("""---""")

    df = pd.read_csv(DATA_PATH)
    rest_cadastrados = df['restaurant_id'].shape[0]
    paises_cadastrados = df.loc[:, 'country_code'].nunique()
    cidades_cadastradas = df.loc[:, 'city'].nunique()
    avaliacoes_na_plataforma = df.loc[:, 'votes'].sum()
    tipos_culinarias = df.loc[:, 'cuisines'].nunique()

    restaurants, countries, cities, ratings, cuisines = st.columns(5)
    restaurants.metric("Restaurantes", value=rest_cadastrados, border=True)
    countries.metric("Paises Cadastrados",
                     value=paises_cadastrados, border=True)
    cities.metric("Cidades Cadastradas",
                  value=cidades_cadastradas, border=True)
    ratings.metric("Avaliações na Plataforma",
                   value=avaliacoes_na_plataforma, border=True)
    cuisines.metric("Tipos de Culinárias", value=tipos_culinarias, border=True)

    # Filtros
    # st.write("## Filtros")

    countries = st.multiselect(
        "Escolha os países que deseja visualizar os restaurantes",
        df.loc[:, 'country_name'].unique().tolist(),
        default=["Brazil", "India", "England", "Canada", "Australia"])

    if __name__ == "__main__":
        app()
