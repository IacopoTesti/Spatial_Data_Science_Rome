### This block defines the linear transformation for ranks, min-max and z-scores normalization 
### formula: x_ij' = max{x_ij} - x_ij

# prints first 5 rows of our matrix
matrix.head()

# these rows define the linear trasformation of discordant columns for our phenomenon
# perc_ater, perc giovani, reddito
tras_perc_ater = matrix['perc_ater_tot_abitazioni'].max() - matrix[['perc_ater_tot_abitazioni']]
tras_perc_giovani = matrix['perc_giovani_tot_pop'].max() - matrix[['perc_giovani_tot_pop']]
tras_reddito = matrix['reddito_lordo_mese'].max() - matrix[['reddito_lordo_mese']]
tras_servizi = matrix['Densita_servizi_kmq'].max() - matrix[['Densita_servizi_kmq']]

# this block combines again the matrix, transformed columns and not transformed columns
# now the matrix has the same polarity of our phenomenon
from functools import reduce
df_all = [matrix[['zu']], tras_perc_ater, matrix[['prezzo_camere_mese']], tras_perc_giovani, tras_reddito, tras_servizi, matrix[['Tasso_disoccupazione']]]
matrix_trans_linear = reduce(lambda  left,right: pd.merge(left,right,how='outer', left_index=True, right_index=True), df_all)
print("This is the matrix where linear trasformation is applied")
matrix_trans_linear.head()
