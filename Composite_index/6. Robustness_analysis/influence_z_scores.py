# read all csv to which we subracted the columns one by one 
df_z_noater = pd.read_csv('matrice_zscores_noater.csv', delimiter=";")
df_z_nocamere = pd.read_csv('matrice_zscores_nocamere.csv', delimiter=";")
df_z_nopop = pd.read_csv('matrice_zscores_nopop.csv', delimiter=";")
df_z_noreddito = pd.read_csv('matrice_zscores_noreddito.csv', delimiter=";")
df_z_noservizi = pd.read_csv('matrice_zscores_noservizi.csv', delimiter=";")
df_z_nodisoccupazione = pd.read_csv('matrice_zscores_nodisoccupazione.csv', delimiter=";")

# computing aggragetion for all matrices where the elementary indicators were subtracted one by one
# function that calculates the MPI aggregation for the dataframe inserted 
def aggregazione_zscores (df):
    zscores_media_agg = df.iloc[:, [1,2,3,4,5]].mean(axis=1)
    zscores_agg_rob = zscores_media_agg.to_frame(name='a')
    return zscores_agg_rob
    
# composite index without alloggi ater
df_z_noater_agg = aggregazione_zscores (df_z_noater)
df_z_noater_agg = df_z_noater_agg.rename(columns={"a": "z_noater"})

# composite index without prezzi camere
df_z_nocamere_agg = aggregazione_zscores (df_z_nocamere)
df_z_nocamere_agg = df_z_nocamere_agg.rename(columns={"a": "z_nocamere"})

# composite index without popolazione
df_z_nopop_agg = aggregazione_zscores (df_z_nopop)
df_z_nopop_agg = df_z_nopop_agg.rename(columns={"a": "z_nopop"})

# composite index without reddito
df_z_noreddito_agg = aggregazione_zscores (df_z_noreddito)
df_z_noreddito_agg = df_z_noreddito_agg.rename(columns={"a": "z_noreddito"})

# composite index without servizi
df_z_noservizi_agg = aggregazione_zscores (df_z_noservizi)
df_z_noservizi_agg = df_z_noservizi_agg.rename(columns={"a": "z_noservizi"})

# composite index without disoccupazione
df_z_nodisoccupazione_agg = aggregazione_zscores (df_z_nodisoccupazione)
df_z_nodisoccupazione_agg = df_z_nodisoccupazione_agg.rename(columns={"a": "z_nodisoccupazione"})

# complete composite index
df_completo_zscores = df_z_index.rename(columns={"index_z-scores": "index_z_scores"})
df_completo_zscores = df_completo_zscores[['index_z_scores']]

# complete dataframe with all composite indices
df_indici_zscores = pd.concat([df_z_noater_agg['z_noater'], df_z_nocamere_agg['z_nocamere'], df_z_nopop_agg['z_nopop'], df_z_noreddito_agg['z_noreddito'], df_z_noservizi_agg['z_noservizi'], df_z_nodisoccupazione_agg['z_nodisoccupazione'], df_completo_zscores['index_z_scores']], axis=1, sort=False)
df_indici_zscores.head()

# show correlation between complete composite index and composite indices without elementaru indicators
f, axes = plt.subplots(2, 3, figsize=(20, 10), sharex=True)
sns.despine(left=True)

# regression A
sns.regplot(x="index_z_scores", y="z_noater", data=df_indici_zscores, ax=axes[0, 0])
model_A = sm.OLS.from_formula("index_z_scores ~ z_noater" ,data=df_indici_zscores)
results_A = model_A.fit()
R2_A = ["R-squared", results_A.rsquared.round(3)]
ax_A = axes[0, 0]
ax_A.set_title(R2_A, size = 20 )

# regression B
sns.regplot(x="index_z_scores", y="z_nocamere", data=df_indici_zscores, ax=axes[0, 1])
model_B = sm.OLS.from_formula("index_z_scores ~ z_nocamere" ,data=df_indici_zscores)
results_B = model_B.fit()
R2_B = ["R-squared", results_B.rsquared.round(3)]
ax_B = axes[0, 1]
ax_B.set_title(R2_B, size = 20 )

# regression C
sns.regplot(x="index_z_scores", y="z_nopop", data=df_indici_zscores, ax=axes[0, 2])
model_C = sm.OLS.from_formula("index_z_scores ~ z_nopop" ,data=df_indici_zscores)
results_C = model_C.fit()
R2_C = ["R-squared", results_C.rsquared.round(3)]
ax_C = axes[0, 2]
ax_C.set_title(R2_C, size = 20 )

# regression D 
sns.regplot(x="index_z_scores", y="z_noreddito", data=df_indici_zscores, ax=axes[1, 0])
model_D = sm.OLS.from_formula("index_z_scores ~ z_noreddito" ,data=df_indici_zscores)
results_D = model_D.fit()
R2_D = ["R-squared", results_D.rsquared.round(3)]
ax_D = axes[1, 0]
ax_D.set_title(R2_D, size = 20 )

# regression E
sns.regplot(x="index_z_scores", y="z_noservizi", data=df_indici_zscores, ax=axes[1, 1])
model_E = sm.OLS.from_formula("index_z_scores ~ z_noservizi" ,data=df_indici_zscores)
results_E = model_E.fit()
R2_E = ["R-squared", results_E.rsquared.round(3)]
ax_E = axes[1, 1]
ax_E.set_title(R2_E, size = 20 )

# regression F
sns.regplot(x="index_z_scores", y="z_nodisoccupazione", data=df_indici_zscores, ax=axes[1, 2])
model_F = sm.OLS.from_formula("index_z_scores ~ z_nodisoccupazione" ,data=df_indici_zscores)
results_F = model_F.fit()
R2_F = ["R-squared", results_F.rsquared.round(3)]
ax_F = axes[1, 2]
ax_F.set_title(R2_F, size = 20 )

# defines the dimensions of x and y labels
sns.set_context("paper", rc={"axes.labelsize":16})
plt.tight_layout()
