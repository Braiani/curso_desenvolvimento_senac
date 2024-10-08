import pandas as pd
import matplotlib.pyplot as plt
import requests


def plotar_pizza(label, values, row, column, index):
    plt.subplot(row, column, index)
    plt.pie(values, labels=label, autopct='%.1f%%', pctdistance=0.77)

def plotar_barra(label, values, row, column, index):
    plt.subplot(row, column, index)
    plt.bar(label, values)


municipios = ['campo-grande', 'dourados', 'tres-lagoas', 'corumba', 'ponta-pora']
dfs = []

for municipio in municipios:
    origem = requests.get(f"https://cdn-apuracao.estadao.com.br/2024/apuracao/primeiro-turno/prefeito/ms/{municipio}.json").json()
    candidatos = origem["candidatos"]
    dfs.append(pd.DataFrame(candidatos))

origem_dados = requests.get("https://cdn-apuracao.estadao.com.br/2024/apuracao/primeiro-turno/vereador/ms/campo-grande.json").json()
prefeitos =  origem_dados['candidatos']

dfs.append(pd.DataFrame(prefeitos))

row = 6
column = 2
index = 1

for df in dfs:
    candidatos = df.loc[0:30, ['nome', 'votos']]
    plotar_pizza(candidatos['nome'], candidatos['votos'], row=row, column=column, index=index)
    index += 1

    plotar_barra(candidatos['nome'], candidatos['votos'], row=row, column=column, index=index)
    index += 1

plt.show()