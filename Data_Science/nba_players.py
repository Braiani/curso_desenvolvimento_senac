import pandas as pd
import matplotlib.pyplot as plt
import os, sys

def get_path():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

df_nba = pd.read_csv(f"{get_path()}/datasets/all_seasons.csv")
df_salaries = pd.read_csv(f"{get_path()}/datasets/ipeadata.csv")

mounths = df_salaries.loc[0:,['Data']]
salaries = df_salaries.loc[0:, ['Salário mínimo real - R$ (do último mês) - Instituto de Pesquisa Econômica Aplicada - GAC12_SALMINRE12']]
player_height = df_nba.loc[:11145, ["player_height"]]
player_weight = df_nba.loc[:11145, ["player_weight"]]

plt.subplot(2,1,1)
plt.plot(mounths, salaries)
plt.grid(True)
plt.title(u"Salário Mínimo Real (Descontado a inflação) - 1940 x 2023")
plt.ylabel(u"Salário mínimo Real")
plt.xlabel("Ano")

plt.subplot(2,1,2)
plt.scatter(player_weight,player_height)
plt.ylabel("Peso")
plt.xlabel("Altura")
plt.title("Jogadores da NBA")


plt.show()