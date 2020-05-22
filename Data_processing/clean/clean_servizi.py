import pandas as pd
import numpy as np
from pandas import read_excel

# open csv
df = pd.read_csv("../data/servizi_zu.csv", delimiter=";", error_bad_lines=False)

df['Densita_servizi'] = df['Densita_servizi'].map('{:,.2f}'.format)

df.to_csv('../outcomes/servizi_agg.csv', index=False)

print("done")