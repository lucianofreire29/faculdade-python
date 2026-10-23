import pandas as pd
import plotly.express as px


# Carregar o arquivo CSV
tabela = pd.read_csv('planilhas/ClientesBanco - ClientesBanco.csv', encoding='utf-8', sep=',')

# Exibir as primeiras linhas do DataFrame
print(tabela.head())


tabela = tabela.dropna()
print(tabela.dropna())
tabela.info()
print(tabela.describe())


