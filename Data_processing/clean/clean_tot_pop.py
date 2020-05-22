import pandas as pd
import numpy as np
from pandas import read_excel

# read excel file and sheet
my_sheet = 'sheet_2'
file_name = '../data/pop_giovani_zu.xlsx'
df_pop = read_excel(file_name, sheet_name=my_sheet, dtype=str)

# read excel file and sheet
my_sheet = '2018'
file_name = '../data/tot_pop_zu_2018.xlsx'
df_tot_zu = read_excel(file_name, sheet_name=my_sheet, dtype=str)

# extract just the column of the totals I need
df_tot_zu = df_tot_zu[['totale']]
# prints the data type of the dataframe
print(df_tot_zu.dtypes)

# convert it in float numbers
df_tot_zu = df_tot_zu.astype(float)

# drop all the ages columns to isolate the municipio and zu
df_pop_zu = df_pop.drop(df_pop.columns[[2,3,4,5,6,7,8,9,10,11,12,13,14,15]], axis = 1)

# convert all the age columns in numeric to calculate the totals later on
df_pop_num = df_pop[['age_16', 'age_17', 'age_18', 'age_19',
                 'age_20', 'age_21', 'age_22', 'age_23',
                 'age_24', 'age_25', 'age_26', 'age_27',
                 'age_28', 'age_29']].apply(pd.to_numeric, errors='coerce')

# merge the two dataframes created above by index
mergedDf = df_pop_zu.merge(df_pop_num, left_index=True, right_index=True)

# drop columns I do not need by number (we consider just from 18 to 29 years old)
zu_young_pop = mergedDf.drop(mergedDf.columns[[0,2,3]], axis = 1)

# print data type of dataframe
print(zu_young_pop.dtypes)

# print data type of dataframe
zu_young_pop = zu_young_pop.fillna(0)

# add alle the ages columns to calculate the totals
zu_young_pop['tot_young_pop_zu'] = zu_young_pop['age_18'] + zu_young_pop['age_19'] + zu_young_pop['age_20'] + zu_young_pop['age_21'] + zu_young_pop['age_22'] + zu_young_pop['age_23'] + zu_young_pop['age_24'] + zu_young_pop['age_25'] + zu_young_pop['age_26'] + zu_young_pop['age_27'] + zu_young_pop['age_28'] + zu_young_pop['age_29']

# merge df young people and df tot pop by zona urbanistica
df_complete = zu_young_pop.merge(df_tot_zu, left_index=True, right_index=True)

# print to check columns data type
print(df_complete.dtypes)

# drop columns I do not need from the dataframe
df_complete = df_complete.drop(df_complete.columns[[1,2,3,4,5,6,7,8,9,10,11,12]], axis = 1)

# calculate percentage of young population (18-29) each zona urbanistica
df_complete['per_young_tot_pop'] = (df_complete['tot_young_pop_zu']/df_complete['totale'])*100

# format the flat numbers and remove all zeros after the comma
df_complete['per_young_tot_pop'] = df_complete['per_young_tot_pop'].map('{:,.2f}'.format)

# export in csv
df_complete.to_csv('../outcomes/perc_young.csv', index=False)

print("done")


