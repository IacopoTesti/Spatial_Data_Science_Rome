### This block defines the normalization for relative indices (min-max)
formula : r_ij = x_ij - minx_ij / max x_ij - min x_ij

dove min(${x_{ij}}$) e max(${x_{ij}}$) sono, rispettivamente, il minimo e il massimo dell' indicatore j

# the matrix linearly trasformed is used
matrix_trans_linear.head(3)

# the variables needed are created 
# drop is needed to eliminate the column zu
x_min = matrix_trans_linear.drop('zu', axis=1).min()
x_max = matrix_trans_linear.drop('zu', axis=1).max()
x = matrix_trans_linear.drop('zu', axis=1)

# normalization min-max is applied to all columns 
r = (x - x_min) / (x_max - x_min)

# inserting again the zu column to show the complete matrix linearly transformed
df_r = matrix[['zu']].merge(r, left_index=True, right_index=True)
df_r = df_r.round(3)
print("This is the normalized matrix with relative indices")
df_r.head()

