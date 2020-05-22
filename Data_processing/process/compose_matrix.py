import pandas as pd
import numpy as np

# open csv
df_matrice = pd.read_csv("../data/matrice.csv", delimiter=";", error_bad_lines=False)

# divide reddito column by 12 months
df_matrice['reddito_lordo_mese'] = df_matrice['reddito']/12

# drop reddito column
df_matrice = df_matrice.drop(df_matrice.columns[[2]], axis = 1)

# format the reddito lordo mese column to delete all the useless zeros
df_matrice['reddito_lordo_mese'] = df_matrice['reddito_lordo_mese'].map('{:,.2f}'.format)

# rename two columns
df_matrice.rename(columns={'per_young_tot_pop':'perc_giovani_tot_pop'}, inplace=True)
df_matrice.rename(columns={'perc_ATER_tot_abitazioni':'perc_ater_tot_abitazioni'}, inplace=True)

# export in csv
df_matrice.to_csv('../outcomes/matrice_agg.csv', index=False)

print("done")