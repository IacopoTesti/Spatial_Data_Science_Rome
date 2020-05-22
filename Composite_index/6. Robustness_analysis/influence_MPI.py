# read all csv to which we subracted the columns one by one 
df_mpi_noater = pd.read_csv('mpi_noater.csv', delimiter=";")
df_mpi_nocamere = pd.read_csv('mpi_nocamere.csv', delimiter=";")
df_mpi_nopop = pd.read_csv('mpi_nopop.csv', delimiter=";")
df_mpi_noreddito = pd.read_csv('mpi_noreddito.csv', delimiter=";")
df_mpi_noservizi = pd.read_csv('mpi_noservizi.csv', delimiter=";")
df_mpi_nodisoccupazione = pd.read_csv('mpi_nodisoccupazione.csv', delimiter=";")

# function that calculates the MPI aggregation for the dataframe inserted 
def aggregazione (df):
    z_media_agg = df.iloc[:, [1,2,3,4,5]].mean(axis=1)
    z_sigma_agg = df.iloc[:, [1,2,3,4,5]].std(axis=1)
    cv_agg = z_sigma_agg / z_media_agg
    MPI_agg_rob = z_media_agg + z_sigma_agg*cv_agg
    MPI_agg_rob = MPI_agg_rob.to_frame(name='a')
    return MPI_agg_rob
    
# computing aggragetion for all matrices where the elementary indicators were subtracted one by one
# composite index without alloggi ater
df_noater = aggregazione (df_mpi_noater)
df_noater = df_noater.rename(columns={"a": "mpi_noater"})

# composite index without prezzi camere
df_nocamere = aggregazione (df_mpi_nocamere)
df_nocamere = df_nocamere.rename(columns={"a": "mpi_nocamere"})

# composite index without popolazione
df_nopop = aggregazione (df_mpi_nopop)
df_nopop = df_nopop.rename(columns={"a": "mpi_nopop"})

# composite index without reddito
df_noreddito = aggregazione (df_mpi_noreddito)
df_noreddito = df_noreddito.rename(columns={"a": "mpi_noreddito"})

# composite index without servizi
df_noservizi = aggregazione (df_mpi_noservizi)
df_noservizi = df_noservizi.rename(columns={"a": "mpi_noservizi"})

# composite index without disoccupazione
df_nodisoc = aggregazione (df_mpi_nodisoccupazione)
df_nodisoc = df_nodisoc.rename(columns={"a": "mpi_nodisoccupazione"})

# complete composite index
df_completo = df_MPI_index[['mpi_index']]

# complete dataframe with all composite indices 
df_indici = pd.concat([df_noater['mpi_noater'], df_nocamere['mpi_nocamere'], df_nopop['mpi_nopop'], df_noreddito['mpi_noreddito'], df_noservizi['mpi_noservizi'], df_nodisoc['mpi_nodisoccupazione'], df_completo['mpi_index']], axis=1, sort=False)
df_indici.head()

# show correlation between complete composite index and composite indices without elementaru indicators
f, axes = plt.subplots(2, 3, figsize=(20, 10), sharex=True)
sns.despine(left=True)

# regression 1 
sns.regplot(x="mpi_index", y="mpi_noater", data=df_indici, ax=axes[0, 0])
# line that defines the regression model
model_1 = sm.OLS.from_formula("mpi_index ~ mpi_noater" ,data=df_indici)
# variable that stores all results of regression
results_1 = model_1.fit()
# variable with results of R-squared
R2_1 = ["R-squared", results_1.rsquared.round(3)]
ax_1=axes[0, 0]
ax_1.set_title(R2_1, size = 20 )

# regression 2
sns.regplot(x="mpi_index", y="mpi_nocamere",data=df_indici, ax=axes[0, 1])
model_2 = sm.OLS.from_formula("mpi_index ~ mpi_nocamere" ,data=df_indici)
results_2 = model_2.fit()
R2_2 = ["R-squared", results_2.rsquared.round(3)]
ax_2=axes[0, 1]
ax_2.set_title(R2_2, size = 20 )

# regression 3
sns.regplot(x="mpi_index", y="mpi_nopop", data=df_indici, ax=axes[0, 2])
model_3 = sm.OLS.from_formula("mpi_index ~ mpi_nopop" ,data=df_indici)
results_3 = model_3.fit()
R2_3 = ["R-squared", results_3.rsquared.round(3)]
ax_3=axes[0, 2]
ax_3.set_title(R2_3, size = 20 )

# regression 4
sns.regplot(x="mpi_index", y="mpi_noreddito", data=df_indici, ax=axes[1, 0])
model_4 = sm.OLS.from_formula("mpi_index ~ mpi_noreddito" ,data=df_indici)
results_4 = model_4.fit()
R2_4 = ["R-squared", results_4.rsquared.round(3)]
ax_4 =axes[1, 0]
ax_4.set_title(R2_4, size = 20 )

# regression 5
sns.regplot(x="mpi_index", y="mpi_noservizi", data=df_indici, ax=axes[1, 1])
model_5 = sm.OLS.from_formula("mpi_index ~ mpi_noservizi" ,data=df_indici)
results_5 = model_5.fit()
R2_5 = ["R-squared", results_5.rsquared.round(3)]
ax_5 =axes[1, 1]
ax_5.set_title(R2_5, size = 20 )

# regression 6
sns.regplot(x="mpi_index", y="mpi_nodisoccupazione", data=df_indici, ax=axes[1, 2])
model_6 = sm.OLS.from_formula("mpi_index ~ mpi_nodisoccupazione" ,data=df_indici)
results_6 = model_6.fit()
R2_6 = ["R-squared", results_6.rsquared.round(3)]
ax_6 =axes[1, 2]
ax_6.set_title(R2_6, size = 20 )

# defines the dimensions of x and y labels
sns.set_context("paper", rc={"axes.labelsize":16})
plt.tight_layout()
