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

# Gráficos para variáveis categóricas
st.subheader("Gráficos de Sobrevivência para Variáveis Categóricas")
cols_categoricas = ['pclass', 'embarked_c', 'embarked_q', 'embarked_s', 'age_group', 
                    'is_male', 'cabin_group', 'title', 'fare_group', 'is_alone', 
                    'sex_pclass_interaction']
for col in cols_categoricas:
    fig, ax = plt.subplots()
    sns.countplot(x=col, hue='survived', data=df_filtered, palette='viridis', ax=ax)
    plt.title(f'Sobrevivência por {col}')
    st.pyplot(fig)

# Gráficos para variáveis numéricas
st.subheader("Distribuição de Sobrevivência para Variáveis Numéricas")
cols_numericas = ['age', 'sibsp', 'parch', 'fare', 'family_size', 'ticket_length', 'ticket_qtd']
for col in cols_numericas:
    fig, ax = plt.subplots()
    sns.kdeplot(data=df_filtered[df_filtered['survived'] == 0][col], label='Não Sobreviveu', shade=True, ax=ax)
    sns.kdeplot(data=df_filtered[df_filtered['survived'] == 1][col], label='Sobreviveu', shade=True, ax=ax)
    plt.title(f'Distribuição de {col} por sobrevivência')
    plt.legend()
    st.pyplot(fig)

# Gráfico de sobrevivência por Fare Group
st.subheader("Sobrevivência por Faixa de Preço (Fare Group)")
fig, ax = plt.subplots()
sns.countplot(x='fare_group', hue='survived', data=df_filtered, ax=ax)
plt.title('Sobrevivência por Faixa de Preço')
st.pyplot(fig)

# Gráfico de densidade por idade
st.subheader("Distribuição de Idade por Sobrevivência")
fig, ax = plt.subplots()
sns.kdeplot(data=df_filtered[df_filtered['survived'] == 0]['age'], label='Não Sobreviveu', shade=True, ax=ax)
sns.kdeplot(data=df_filtered[df_filtered['survived'] == 1]['age'], label='Sobreviveu', shade=True, ax=ax)
plt.title('Distribuição de Idade por Sobrevivência')
plt.legend()
st.pyplot(fig)

# Gráfico de barras por Pclass
st.subheader("Sobrevivência por Classe (Pclass)")
fig, ax = plt.subplots()
sns.countplot(x='pclass', hue='survived', data=df_filtered, ax=ax)
plt.title('Sobrevivência por Classe (Pclass)')
st.pyplot(fig)


