import pandas as pd
import matplotlib.pyplot as plt
import os, sys

def get_path():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

df = pd.read_csv(f"{get_path()}/datasets/ipeadata.csv")

mounths = df.loc[0:,['Data']]
salaries = df.loc[0:, ['Salário mínimo real - R$ (do último mês) - Instituto de Pesquisa Econômica Aplicada - GAC12_SALMINRE12']]
plt.plot(mounths, salaries)
plt.plot((1,2,3), (5,6,7))
plt.grid(True)
plt.title(u"Salário Mínimo Real (Descontado a inflação) - 1940 x 2023")
plt.ylabel(u"Salário mínimo Real")
plt.xlabel("Ano")


plt.show()