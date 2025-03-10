import streamlit as st
import pandas as pd
import plotly.express as px

from utils.helper_functions import create_price_type

DATA_PATH = "dataset/zomato_curated.csv"


def app():
    st.write("# 🗺️ Informações por País")
    st.markdown("""---""")

    df = pd.read_csv(DATA_PATH)
    # st.dataframe(df)
    st.markdown(" ## Estatísticas Gerais")

    selected_countries = st.sidebar.multiselect(
        "Escolha os países para visualizar as informações",
        options=df['country_name'].unique().tolist(),
        # default=["India", "Brazil"]
    )
    filtered_df = df[df['country_name'].isin(selected_countries)]
    st.write("### **Informações dos Países Filtrados**")
    st.dataframe(filtered_df)

    filtered_df['price_type'] = filtered_df['price_range'].apply(
        create_price_type)

    # Número de cidades por país
    cities_count = filtered_df.groupby("country_name")[
        "city"].nunique().reset_index()
    cities_count.columns = ["country_name", "city"]

    fig = px.bar(cities_count, x="country_name", y="city", color_discrete_sequence=["#FF3131"],
                 title="Distribuição de Cidades por País",
                 labels={"country_name": "País",
                         "city": "Quantidade de Cidades"},
                 width=1000, height=600)
    fig.update_xaxes(categoryorder='total descending')
    fig.update_traces(texttemplate='%{y}', textposition='inside')
    fig.update_layout(yaxis_title="Quantidade de Cidades")
    st.plotly_chart(fig)

    # Número de restaurantes por país
    restaurants_count = filtered_df.groupby(
        "country_name")["restaurant_id"].nunique().reset_index()
    restaurants_count.columns = ["country_name", "restaurant_id"]

    fig = px.bar(restaurants_count, x="country_name", y="restaurant_id", color_discrete_sequence=["#FF3131"],
                 title="Distribuição de Restaurantes por País",
                 labels={"country_name": "País",
                         "restaurant_id": "Quantidade de Restaurantes"},
                 width=1000, height=600)
    fig.update_xaxes(categoryorder='total descending')
    fig.update_traces(texttemplate='%{y}', textposition='inside')
    fig.update_layout(yaxis_title="Quantidade de Restaurantes")
    st.plotly_chart(fig)

    # Número de restaurantes por tipo de preço - gourmet
    gourmet_df = filtered_df.loc[filtered_df["price_type"] == "gourmet"]
    gourmet_counts = gourmet_df.groupby(
        "country_name")["restaurant_id"].nunique().reset_index()
    gourmet_counts = gourmet_counts.sort_values(
        "restaurant_id", ascending=False)

    fig = px.bar(
        gourmet_counts,
        x="restaurant_id",
        y="country_name",
        orientation="h",
        labels={
            "country_name": "País",
            "restaurant_id": "Quantidade de Restaurantes Gourmet"},
        title="Distribuição de Restaurantes Gourmet por País",
        color_discrete_sequence=["#FF3131"]
    )
    fig.update_traces(texttemplate='%{x}', textposition='inside')

    st.plotly_chart(fig)

    # país que possui a maior quantidade de tipos de culinária distintos?
    cuisines_count = filtered_df.groupby("country_name")[
        "cuisines"].nunique().reset_index()
    country_cuisines_counts = cuisines_count.sort_values(
        "cuisines", ascending=False)
    country_cuisines_counts.columns = ["country_name", "cuisines"]

    fig = px.bar(country_cuisines_counts, x="country_name", y="cuisines", color_discrete_sequence=["#FF3131"],
                 title="Distribuição de Tipos de Culinária por País",
                 labels={"country_name": "País",
                         "cuisines": "Quantidade de Tipos de Culinária"},
                 width=1000, height=600)
    fig.update_xaxes(categoryorder='total descending')
    fig.update_traces(texttemplate='%{y}', textposition='inside')
    fig.update_layout(yaxis_title="Quantidade de Tipos de Culinária")
    st.plotly_chart(fig)
