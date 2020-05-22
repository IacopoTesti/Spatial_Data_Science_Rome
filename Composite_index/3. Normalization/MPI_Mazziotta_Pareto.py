### This block defines the MPI normalization (Mazziotta Pareto Index)

# let's use the matrix linearly transformed as starting point
# creating variables needed for the formula abovementioned 
x_sigma_z = matrix_trans_linear.drop('zu', axis=1).std()
x_media_z = matrix_trans_linear.drop('zu', axis=1).mean()
x = matrix_trans_linear.drop('zu', axis=1)
s = 10
m = 100

# the MPI normalization is applied to all columns 
MPI = ((x - x_media_z) / x_sigma_z)*s + m

# insert again the zu column
df_MPI = matrix[['zu']].merge(MPI, left_index=True, right_index=True)
df_MPI = df_MPI.round(3)
print("This is the normalized matrix with MPI (Mazziotta Pareto Index)")
df_MPI.head()
