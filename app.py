import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
df = pd.read_excel('Output2.xlsx')  # Substitua pelo seu caminho de arquivo

# Título do aplicativo
st.title('Dashboard de Vendas')

# Dropdown para seleção de produtos com múltiplas opções
selected_products = st.multiselect('Selecione um ou mais Produtos', df['SKU'].unique())

# RadioButtons para seleção da métrica
selected_metric = st.radio('Selecione uma Métrica', ('Total Sales', 'Margem %'))

# Filtrar dados com base na seleção
filtered_df = df[df['SKU'].isin(selected_products)]

# Verificar se há produtos selecionados antes de criar o gráfico
if not filtered_df.empty:
    # Criar gráfico
    fig = px.bar(filtered_df, x='SKU', y=selected_metric, title=f'{selected_metric} para {", ".join(selected_products)}')
    st.plotly_chart(fig)
else:
    st.write("Selecione pelo menos um produto para visualizar os dados.")
