import pandas as pd
import matplotlib.pyplot as plt
import os, sys

def base_path():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

df = pd.read_csv(f"{base_path()}/datasets/cybersecurity.csv")

