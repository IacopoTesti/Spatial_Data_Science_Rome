# read all csv to which we subracted the columns one by one 
df_r_noater = pd.read_csv('matrice_minmax_noater.csv', delimiter=";")
df_r_nocamere = pd.read_csv('matrice_minmax_nocamere.csv', delimiter=";")
df_r_nopop = pd.read_csv('matrice_minmax_nopop.csv', delimiter=";")
df_r_noreddito = pd.read_csv('matrice_minmax_noreddito.csv', delimiter=";")
df_r_noservizi = pd.read_csv('matrice_minmax_noservizi.csv', delimiter=";")
df_r_nodisoccupazione = pd.read_csv('matrice_minmax_nodisoccupazione.csv', delimiter=";")

# function that calculates the MPI aggregation for the dataframe inserted 
def aggregazione_minmax (df):
    minmax_media_agg = df.iloc[:, [1,2,3,4,5]].mean(axis=1)
    minmax_agg_rob = minmax_media_agg.to_frame(name='a')
    return minmax_agg_rob
    
# composite index without alloggi ater
df_r_noater_agg = aggregazione_minmax (df_r_noater)
df_r_noater_agg = df_r_noater_agg.rename(columns={"a": "r_noater"})

# composite index without prezzi camere
df_r_nocamere_agg = aggregazione_minmax (df_r_nocamere)
df_r_nocamere_agg = df_r_nocamere_agg.rename(columns={"a": "r_nocamere"})

# composite index without popolazione
df_r_nopop_agg = aggregazione_minmax (df_r_nopop)
df_r_nopop_agg = df_r_nopop_agg.rename(columns={"a": "r_nopop"})

# composite index without reddito
df_r_noreddito_agg = aggregazione_minmax (df_r_noreddito)
df_r_noreddito_agg = df_r_noreddito_agg.rename(columns={"a": "r_noreddito"})

# composite index without servizi
df_r_noservizi_agg = aggregazione_minmax (df_r_noservizi)
df_r_noservizi_agg = df_r_noservizi_agg.rename(columns={"a": "r_noservizi"})

# composite index without disoccupazione
df_r_nodisoccupazione_agg = aggregazione_minmax (df_r_nodisoccupazione)
df_r_nodisoccupazione_agg = df_r_nodisoccupazione_agg.rename(columns={"a": "r_nodisoccupazione"})

# complete composite index 
df_completo_minmax = df_r_index.rename(columns={"index_min-max": "index_min_max"})
df_completo_minmax = df_completo_minmax[['index_min_max']]

# complete dataframe with all composite indices
df_indici_min_max = pd.concat([df_r_noater_agg['r_noater'], df_r_nocamere_agg['r_nocamere'], df_r_nopop_agg['r_nopop'], df_r_noreddito_agg['r_noreddito'], df_r_noservizi_agg['r_noservizi'], df_r_nodisoccupazione_agg['r_nodisoccupazione'], df_completo_minmax['index_min_max']], axis=1, sort=False)
df_indici_min_max.head()

# show correlation between complete composite index and composite indices without elementary indicators
f, axes = plt.subplots(2, 3, figsize=(20, 10), sharex=True)
sns.despine(left=True)

# regression I
sns.regplot(x="index_min_max", y="r_noater", data=df_indici_min_max, ax=axes[0, 0])
model_I = sm.OLS.from_formula("index_min_max ~ r_noater" ,data=df_indici_min_max)
results_I = model_I.fit()
R2_I = ["R-squared", results_I.rsquared.round(3)]
ax_I = axes[0, 0]
ax_I.set_title(R2_I, size = 20 )

# regression II
sns.regplot(x="index_min_max", y="r_nocamere", data=df_indici_min_max, ax=axes[0, 1])
model_II = sm.OLS.from_formula("index_min_max ~ r_nocamere" ,data=df_indici_min_max)
results_II = model_II.fit()
R2_II = ["R-squared", results_II.rsquared.round(3)]
ax_II = axes[0, 1]
ax_II.set_title(R2_II, size = 20 )

# regression III
sns.regplot(x="index_min_max", y="r_nopop", data=df_indici_min_max, ax=axes[0, 2])
model_III = sm.OLS.from_formula("index_min_max ~ r_nopop" ,data=df_indici_min_max)
results_III = model_III.fit()
R2_III = ["R-squared", results_III.rsquared.round(3)]
ax_III = axes[0, 2]
ax_III.set_title(R2_III, size = 20 )

# regression IV 
sns.regplot(x="index_min_max", y="r_noreddito", data=df_indici_min_max, ax=axes[1, 0])
model_IV = sm.OLS.from_formula("index_min_max ~ r_noreddito" ,data=df_indici_min_max)
results_IV = model_IV.fit()
R2_IV = ["R-squared", results_IV.rsquared.round(3)]
ax_IV = axes[1, 0]
ax_IV.set_title(R2_IV, size = 20 )

# regression V
sns.regplot(x="index_min_max", y="r_noservizi", data=df_indici_min_max, ax=axes[1, 1])
model_V = sm.OLS.from_formula("index_min_max ~ r_noservizi" ,data=df_indici_min_max)
results_V = model_V.fit()
R2_V = ["R-squared", results_V.rsquared.round(3)]
ax_V = axes[1, 1]
ax_V.set_title(R2_V, size = 20 )

# regression VI
sns.regplot(x="index_min_max", y="r_nodisoccupazione", data=df_indici_min_max, ax=axes[1, 2])
model_VI = sm.OLS.from_formula("index_min_max ~ r_nodisoccupazione" ,data=df_indici_min_max)
results_VI = model_VI.fit()
R2_VI = ["R-squared", results_VI.rsquared.round(3)]
ax_VI = axes[1, 2]
ax_VI.set_title(R2_VI, size = 20 )

# defines the dimensions of x and y labels
sns.set_context("paper", rc={"axes.labelsize":16})
plt.tight_layout()
