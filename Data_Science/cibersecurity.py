import pandas as pd
import matplotlib.pyplot as plt
import os, sys, re

def linha_com_data(linha):
    return bool(re.match(r'^\d{4}-\d{2}-\d{2}', linha))

def tratar_arquivo():
    with open(f"{base_path()}/datasets/cybersecurity_attacks.csv", 'r') as arquivo:
        linhas = arquivo.readlines()
        primeira_linha = linhas[0]
        primeira_linha = linhas[0].replace(' ', '_')

        linhas_filtradas = []

        for linha in linhas:
            if linha_com_data(linha):
                linhas_filtradas.append(linha)

    with open(f"{base_path()}/datasets/cybersecurity.csv", 'w') as arquivo_saida:
        arquivo_saida.write(primeira_linha)
        arquivo_saida.writelines(linhas_filtradas)

def base_path():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

def plotar_pizza(label, values, row, column, index, title = ''):
    plt.subplot(row, column, index)
    plt.pie(values, labels=label, autopct='%.1f%%', pctdistance=0.6)
    plt.title(title)

def plotar_barra(label, values, row, column, index, title = ''):
    plt.subplot(row, column, index)
    plt.bar(label, values)
    plt.title(title)

def preparar_dados(dados: dict):
    valores = []
    labels = []

    for chave, valor in dados.items():
        valores.append(float(valor))
        labels.append(chave)
    
    return valores,labels


# tratar_arquivo()

df = pd.read_csv(f"{base_path()}/datasets/cybersecurity.csv")

dataset = df.loc[0:]

protocolos = {}
packet_length = {
    '< 200': 0,
    '200 > 400': 0,
    '400 > 600': 0,
    '600 > 800': 0,
    '800 > 1000': 0,
    '> 1000': 0,
}
traffic_type = {}
attack_type = {}
severity_level = {}

for interacao in dataset.get('Protocol'):
    if interacao in protocolos:
        protocolos[interacao] += 1
    else:
        protocolos[interacao] = 1

for interacao in dataset.get('Packet_Length'):
    if interacao < 200:
        packet_length['< 200'] += 1
    elif interacao < 400:
        packet_length['200 > 400'] += 1
    elif interacao < 600:
        packet_length['400 > 600'] += 1
    elif interacao < 800:
        packet_length['600 > 800'] += 1
    elif interacao < 1000:
        packet_length['800 > 1000'] += 1
    else:
        packet_length['> 1000'] += 1

for interacao in dataset.get('Traffic_Type'):
    if interacao in traffic_type:
        traffic_type[interacao] += 1
    else:
        traffic_type[interacao] = 1

for interacao in dataset.get('Attack_Type'):
    if interacao in attack_type:
        attack_type[interacao] += 1
    else:
        attack_type[interacao] = 1

for interacao in dataset.get('Severity_Level'):
    if not interacao:
        continue
    if interacao in severity_level:
        severity_level[interacao] += 1
    else:
        severity_level[interacao] = 1

valores, labels = preparar_dados(dados=protocolos)
plotar_pizza(label=labels, values=valores, row=3,column=2, index=1, title='Protocolos')

valores, labels = preparar_dados(dados=traffic_type)
plotar_pizza(label=labels, values=valores, row=3,column=2, index=2, title='Tipo de Tráfego')

valores, labels = preparar_dados(dados=attack_type)
plotar_pizza(label=labels, values=valores, row=3,column=2, index=3, title='Tipo de Ataque')

valores, labels = preparar_dados(dados=severity_level)
plotar_pizza(label=labels, values=valores, row=3,column=2, index=4, title='Gravidade do Ataque')


valores, labels = preparar_dados(dados=packet_length)
plotar_barra(label=labels, values=valores, row=3,column=2, index=5, title='Tamanho dos pacotes')

plt.show()