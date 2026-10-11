import streamlit as st
import pandas as pd
import plotly.express as px

# Passo a passo do projeto:
# Passo 1: Criar a tela do sistema

st.write("# Sistema de Vendas")

#Importando a tabela
tabela = pd.read_csv("./Aula4/vendas.csv")
st.sidebar.write("## Cadastrar Venda")

# Passo 2: Criar o formulário de cadastro
# Passo 3: Salvar a venda na base de dados
# Passo 4: Mostrar a base de dados na tela
# Passo 5: Criar o dashboard com os gráficos



