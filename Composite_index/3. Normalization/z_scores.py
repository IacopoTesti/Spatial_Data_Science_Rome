### This block defines the z-scores normalization 

# let's use the matrix linearly transformed as starting point
matrix_trans_linear.head()

# creating variables needed for the formula abovementioned
x_sigma = matrix_trans_linear.drop('zu', axis=1).std()
x_media = matrix_trans_linear.drop('zu', axis=1).mean()
x = matrix_trans_linear.drop('zu', axis=1)

# the z-scores normalization is applied to all columns 
z = (x - x_media) / x_sigma

# insert again the zu column
df_z = matrix[['zu']].merge(z, left_index=True, right_index=True)
df_z = df_z.round(3)
print("This is the normalized matrix with z-scores")
df_z.head()
