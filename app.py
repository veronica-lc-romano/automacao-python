import streamlit as st
import pandas as pd
import plotly.express as px

# Passo a passo do projeto:
# Passo 1: Criar a tela do sistema

st.write("# Sistema de Vendas")

#Importando a tabela
tabela = pd.read_csv("./Aula4/vendas.csv")

# Passo 2: Criar o formulário de cadastro
st.sidebar.write("## Cadastrar Venda")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("valor")
botao = st.sidebar.button("Cadastrar Venda")

# Passo 3: Salvar a venda na base de dados
if botao:
    nova_venda = [data, vendedor, produto, quantidade, valor]
    tabela.loc[len(tabela)] = nova_venda
    tabela.to_csv("vendas.csv", index=False)
    st.success("Venda Cadastrada com Sucesso!")
# Passo 4: Mostrar a base de dados na tela
# Passo 5: Criar o dashboard com os gráficos



