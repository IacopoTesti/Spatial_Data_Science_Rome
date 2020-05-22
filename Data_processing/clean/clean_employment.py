import pandas as pd
import numpy as np
from pandas import read_excel

# read excel file and sheet
my_sheet = 'ZU_formatted'
file_name = '../data/employment.xlsx'
df = read_excel(file_name, sheet_name=my_sheet)

df['Tasso di disoccupazione'] = df['Tasso di disoccupazione'].map('{:,.2f}'.format)

df.to_csv('../outcomes/disoccupazione_agg.csv', index=False)

print("done")