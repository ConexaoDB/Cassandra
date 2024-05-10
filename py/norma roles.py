import pandas as pd

# Carregar os CSVs para DataFrames
hero_stats_df = pd.read_csv('Current_Pro_meta.csv')
heroes_df = pd.read_csv('All_Heroes_ID.csv')

# Extrair as colunas 'Roles' e 'hero_id' e salvar em um único arquivo CSV
combined_df = pd.DataFrame({
    'role_id': hero_stats_df['Roles'],
    'hero_id': heroes_df['Hero ID']
})
# Salvando juntos em um csv
combined_df.to_csv('hero_roles.csv', index=False)
