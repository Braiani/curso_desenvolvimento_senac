import pandas as pd
import os, sys

def get_path():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

def create_folder():
    if not os.path.exists(f"{get_path()}/datasets_exercises"):
        os.makedirs(f"{get_path()}/datasets_exercises")
        print(f"Pasta criada: {get_path()}/datasets_exercises")
    else:
        print(f"A pasta já existe: {get_path()}/datasets_exercises")

def save(data: pd.DataFrame, filename: str):
    newDf = pd.DataFrame()
    if ".csv" not in filename:
        filename += ".csv"
    create_folder()
    newDf = data
    newDf.to_csv(f"{get_path()}/datasets_exercises/{filename}")


df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df.set_index('PassengerId', inplace=True)

save(
    df.query('Age < 10 and Survived ==1'),
    '01_under10_survived.csv'
)
save(
    df.query('Sex == "female" and Survived == 1'),
    '02_woman_survived'
)
save(
    df.query('Sex == "male" and Survived == 1'),
    '03_man_survived'
)
save(
    df.query('Age > 50 and Survived == 1'),
    '04_olds_survived'
)
save(
    df.query('Age < 12 and Sex == "female" and Survived == 1'),
    '05_under_12_female_survived.csv'
)
