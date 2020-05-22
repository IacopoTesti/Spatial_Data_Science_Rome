# import all libraries
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import math
import numpy as np
import statsmodels.api as sm

# read dataframe
matrix = pd.read_csv('matrice_finale_ok.csv')
# print out first 5 lines 
matrix.head()

# this line defines the descriptive statistics of our matrix
matrix_summary = matrix.describe()
# calculating variation coefficients for the matrix columns with all elementary indicators
matrix_summary.loc['coeff_var'] = matrix.std() / matrix.mean()
# calculating sums for the matrix columns with all elementary indicators
matrix_summary.loc['somme'] = matrix.sum()
# this rounds all numbers to 3 decimals
matrix_summary = matrix_summary.round(3)
matrix_summary

# boxplot for column perc_ater_tot_abitazioni
boxplot = matrix.boxplot(column="perc_ater_tot_abitazioni", grid=False, fontsize=15)

# boxplot for column prezzo camere mese
boxplot = matrix.boxplot(column="prezzo_camere_mese", grid=False, fontsize=15)

# boxplot for column perc_giovani_tot_pop
boxplot = matrix.boxplot(column="perc_giovani_tot_pop", grid=False, fontsize=15)

# boxplot for column reddito_lordo_mese
boxplot = matrix.boxplot(column="reddito_lordo_mese", grid=False, fontsize=15)

# boxplot for column Densita_servizi_kmq
boxplot = matrix.boxplot(column="Densita_servizi_kmq", grid=False, fontsize=15)

# boxplot for column Tasso_disoccupazione
boxplot = matrix.boxplot(column="Tasso_disoccupazione", grid=False, fontsize=15)

# this block defines the correlation matrix between all elementary indicators
print("This is the correlation matrix of all elementary indicators")
sns.set(style="ticks")
sns.pairplot(matrix)
