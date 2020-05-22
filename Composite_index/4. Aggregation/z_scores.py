### This block defines the aggregation for normalization with z-scores
#### the simple arithmetic mean is used because some values of the normalized matrix with min-max are negative

# compute the arithmetic mean of all elementary indicators normalized with z-scores
df_z['index_z-scores'] = df_z.mean(axis=1)
df_z_index = df_z.round(3)
print("This is the matrix with the composite index with z-scores normalization and aggregation with arithmetic mean")
df_z_index.head()
