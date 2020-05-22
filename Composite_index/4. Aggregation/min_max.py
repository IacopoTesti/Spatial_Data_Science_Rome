### This block defines the aggregation for normalization with relative indices
#### the simple arithmetic mean is used because some values of the normalized matrix with min-max are zero

# compute the arithmetic mean of all elementary indicators normalized with relative indeces (min-max)
# this line adds the column of the composite index by computing the arithmetic mean of all other columns
df_r['index_min-max'] = df_r.mean(axis=1)
df_r_index = df_r.round(3)
print("This is the matrix with the composite index with min-max normalization and aggregation with arithmetic mean")
df_r_index.head()

