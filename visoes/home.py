import streamlit as st


def app():
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
