import pandas as pd
import inflection

COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}

# Mapeamento dos códigos de cor para nomes
COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "yellow",
    "FFBA00": "orange",
    "CBCBC8": "gray",
    "FF7800": "darkorange",
}


def rename_columns(dataframe):
    df = dataframe.copy()
    def title(x): return inflection.titleize(x)
    def snakecase(x): return inflection.underscore(x)
    def spaces(x): return x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df


def country_name(country_id):
    return COUNTRIES.get(country_id, 'Unknown Country')


def color_name(color_code):
    return COLORS.get(color_code, "blue")


def create_price_type(price_range):
    match price_range:
        case 1:
            return "cheap"
        case 2:
            return "normal"
        case 3:
            return "expensive"
        case _:
            return "gourmet"
