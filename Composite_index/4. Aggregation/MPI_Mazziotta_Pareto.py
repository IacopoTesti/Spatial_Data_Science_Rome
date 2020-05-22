### This block defines the aggregation for normalization with MPI (Mazziotta Pareto Index)
#### aggregation MPI is used (similar to geometric mean because the arithmetic mean is corrected by a penalty function)

# all variables needed for the formula abovementioned are defined

# mean of the z elements of the standardized matrix
z_media = df_MPI.mean(axis=1)
# standard deviation of elements z of standardized matrix
z_sigma = df_MPI.std(axis=1)
# compute cv
cv = z_sigma / z_media

# calculating index MPI using positive sign (because our phenomenon is negative)
MPI_agg = z_media + z_sigma*cv

# transform the MPI index from series to dataframe
MPI_agg = MPI_agg.to_frame(name='mpi_index')

df_MPI_index = df_MPI.merge(MPI_agg, left_index=True, right_index=True)
df_MPI_index = df_MPI_index.round(3)
print("This is the matrix with the composite index computed with MPI normalization and MPI aggregation")
# export csv
df_MPI_index.to_csv('df_mpi_index.csv')
# prints first rows
df_MPI_index.head()
