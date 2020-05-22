import pandas as pd
import numpy as np
from pandas import read_excel

# open csv
df = pd.read_csv("../data/matrice_finale_N.csv", delimiter=";", error_bad_lines=False)

df['Densita_servizi_kmq'] = df['Densita_servizi_kmq'].map('{:,.2f}'.format)
df['perc_ater_tot_abitazioni'] = df['perc_ater_tot_abitazioni'].map('{:,.1f}'.format)
df['perc_giovani_tot_pop'] = df['perc_giovani_tot_pop'].map('{:,.1f}'.format)
df['reddito_lordo_mese'] = df['reddito_lordo_mese'].map('{:,.1f}'.format)
df['Tasso_disoccupazione'] = df['Tasso_disoccupazione'].map('{:,.2f}'.format)


df.to_csv('../outcomes/matrice_finale_ok.csv', index=False)

print("done")