#creating a matrix containing all composite indices calculated with different methodologies for each ZU
from functools import reduce
df_index_all = [matrix[['zu']],df_r_index['index_min-max'],df_z_index['index_z-scores'],df_MPI_index["mpi_index"]]
matrix_index_all = reduce(lambda  left,right: pd.merge(left,right,how='outer', left_index=True, right_index=True), df_index_all)
summary_index_all = matrix_index_all.describe()
summary_index_all.round(2)

#Creating histograms for each composite idicex
zu_array = df_z_index['zu'].to_numpy()
z_index = df_z_index['index_z-scores'].to_numpy()
mpi_index = df_MPI_index["mpi_index"].to_numpy()
mpi_level = df_MPI_index["mpi_index"].to_numpy()
minmax_index = df_r['index_min-max'].to_numpy()
n_bins = 10
plt.figure(figsize=(10,5), dpi=100)
plt.subplot(131)
plt.hist(minmax_index,bins = n_bins, label = "index_mimax")
plt.title("Composite index Min-Max")

plt.subplot(132)
plt.hist(z_index,bins = n_bins)
plt.title("Composite Index Z-score")

plt.subplot(133)
plt.hist(mpi_index,bins = n_bins)
plt.title("Composite index MPI")

plt.savefig('histogram_of_indexes.png')
