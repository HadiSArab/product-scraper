import pandas as pd
from unidecode import unidecode


df = pd.read_json('./divar.json')
df = df.T
print(df.columns)

df.to_csv('./divar.csv')