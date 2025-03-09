import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

from utils.helper_functions import color_name

DATA_PATH = "dataset/zomato_curated.csv"


def create_map(filtered_df, default_zoom=1, render_width=1024, render_height=768):

    # pré-processa a coluna 'rating_color' para criar a coluna 'color_name'
    if "rating_color" in filtered_df.columns:
        filtered_df['color_name'] = filtered_df['rating_color'].apply(
            color_name)
    else:
        filtered_df['color_name'] = "blue"

    if filtered_df.empty:
        avg_lat, avg_long = 0, 0
    else:
        avg_lat = filtered_df['latitude'].mean()
        avg_long = filtered_df['longitude'].mean()

    m = folium.Map(location=[avg_lat, avg_long], zoom_start=default_zoom)

    marker_cluster = MarkerCluster().add_to(m)

    # Itera sobre cada linha do DataFrame filtrado e adiciona um marcador com popup customizado
    for _, line in filtered_df.iterrows():
        name = line['restaurant_name']
        price_for_two = line['average_cost_for_two']
        cuisine = line['cuisines']
        currency = line['currency']
        rating = line['aggregate_rating']
        color = f'{line["color_name"]}'

        # Cria o conteúdo do popup
        html = (
            f"<p><strong>{name}</strong></p>"
            f"<p>Price: {price_for_two},00 ({currency}) para dois"
            f"<br />Type: {cuisine}"
            f"<br />Aggregate Rating: {rating}/5.0</p>"
        )

        popup = folium.Popup(folium.Html(html, script=True), max_width=500)

        folium.Marker(
            location=[line['latitude'], line['longitude']],
            popup=popup,
            tooltip=name,
            icon=folium.Icon(color=color, icon="home", prefix="fa")
        ).add_to(marker_cluster)

    # Exibe o mapa interativo no streamlit
    folium_static(m, width=render_width, height=render_height)


def app():
    st.write(
        "## Descubra seu próximo restaurante favorito no melhor destino gastronômico!")
    st.markdown(
        " #### Confira as marcas que compõem nossa plataforma e surpreenda-se!")
    st.markdown("""---""")
    # TODO: Criar uma função para carregar os dados e retornar as informações
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
    st.write("## Filtros")

    selected_countries = st.multiselect(
        "Escolha os países que deseja visualizar os restaurantes",
        df.loc[:, 'country_name'].unique().tolist(),
        default=["Brazil", "India", "England", "Canada", "Australia"]
    )

    filtered_df = df[df['country_name'].isin(selected_countries)]

    # avg_lat = filtered_df['latitude'].mean()
    # avg_long = filtered_df['longitude'].mean()
    create_map(filtered_df, default_zoom=1,
               render_width=1024, render_height=768)


if __name__ == "__main__":
    app()
