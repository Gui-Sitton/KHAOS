import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys
# Carregar o dataset do Titanic diretamente de uma URL

# Define o caminho relativo
file_path = os.path.join('..', 'Data', 'processed_data.csv')  # '..' sobe um nível de diretório

# Carrega os dados
df = pd.read_csv(file_path)



# Título
st.title("Análise de Sobrevivência do Titanic")

# Filtros
age_filter = st.sidebar.multiselect("Filtrar por grupo de idade", options=df['age_group'].unique(), default=df['age_group'].unique())
pclass_filter = st.sidebar.multiselect("Filtrar por classe", options=df['pclass'].unique(), default=df['pclass'].unique())

# Aplicar os filtros no dataframe
df_filtered = df[(df['age_group'].isin(age_filter)) & (df['pclass'].isin(pclass_filter))]

# Gráfico de densidade por idade
st.subheader("Distribuição de Idade por Sobrevivência")
fig, ax = plt.subplots()
sns.kdeplot(data=df_filtered[df_filtered['survived'] == 0]['age'], label='Não Sobreviveu', shade=True, ax=ax)
sns.kdeplot(data=df_filtered[df_filtered['survived'] == 1]['age'], label='Sobreviveu', shade=True, ax=ax)
plt.legend()
st.pyplot(fig)

# Gráfico de barras por Pclass
st.subheader("Sobrevivência por Classe (Pclass)")
fig, ax = plt.subplots()
sns.countplot(x='pclass', hue='survived', data=df_filtered, ax=ax)
st.pyplot(fig)

# Gráfico de sobrevivência por Fare Group
st.subheader("Sobrevivência por Faixa de Preço (Fare Group)")
fig, ax = plt.subplots()
sns.countplot(x='fare_group', hue='survived', data=df_filtered, ax=ax)
st.pyplot(fig)
