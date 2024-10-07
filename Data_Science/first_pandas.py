import pandas as pd
import os, sys

def get_path():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

print(df.head())
print()
print(df.info())
print()

df.set_index('PassengerId', inplace=True)
print(df.head(10))
print()
print(df.columns)
print()

print(df.values)
print()
print(df.loc[1])
print()
print(df.loc[[1,20,300,400]])
print()
print(df.loc[[1,20,300,400], ['Name', 'Sex', 'Age', 'Survived']])
print()
print(df.loc[20:40:2])
print()
print(df.loc[40::-2, ['Name', 'Survived']])
print()
print(df.query('Age > 20 and Age < 26'))
print()
print(df.query('Age > 20 and Sex == "female"').head(20))
newDf = pd.DataFrame()
newDf = df.query('Age > 30 and Sex == "male"')
print()
try:
    df.to_csv(f"{get_path()}/dataset.csv", sep=';', index=False, encoding='utf-8-sig')
    newDf.to_csv(f"{get_path()}/dataset_mod.csv", sep=';', index=False, encoding='utf-8-sig')
    print('Dataset salvo com sucesso!')
except Exception as err:
    print(f"Um erro ocorreu: {err}")
