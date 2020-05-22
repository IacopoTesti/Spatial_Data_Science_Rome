import pandas as pd
import numpy as np

# open csv
df = pd.read_csv("../data/rooms_rent_zu.csv", error_bad_lines=False)

# drop columns I do not need
df_2 = df.drop(df.columns[[0, 1, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 20, 21]], axis = 1)

# order the dataframe by the column municipio
df_2 = df_2.sort_values(by='municipio')

# drop columns I do not need for grouping by zona urbanistica
df_3 = df_2.drop(df_2.columns[[0, 1, 2]], axis = 1)

# drop nan values and outliers
df_3 = df_3.dropna()

# drop outliers for prices less than 50 euros
df_3 = df_3[df_3.room_price > 50]

# group the dataframe by the columns mentioned
df_4 = df_3.groupby(['ZU', 'CODZU']).mean().reset_index()

# order the rows by municipio
df_5 = df_4.sort_values(by='CODZU').reset_index()

# drop first column
df_6 = df_5.drop(df_5.columns[[0]], axis = 1)

# print dataframe type
print(df_6.dtypes)

# this transform the nan values in the room price column in zeros
# then convert all the numbers in integers
df_7 = df_6['room_price'].fillna(0).astype(int)

# print again dataframe type to check it out
print(df_6.dtypes)

# merge df6 and df7 dataframes
mergedDf = df_6.merge(df_7, left_index=True, right_index=True)

# print again dataframe type to check it out
print(mergedDf.dtypes)

# drop all th columns I do not need
df_final = mergedDf.drop(mergedDf.columns[[0, 2, 3]], axis = 1)

# export in csv
df_final.to_csv('../outcomes/local_rooms_ZU.csv', index=False)

print("done")

