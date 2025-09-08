import pandas as pd

df = pd.read_csv('Checking1.csv')
print(df.iloc[:, [0, 1, 4]].to_string())