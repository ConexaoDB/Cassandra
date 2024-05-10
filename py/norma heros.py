import pandas as pd

# Carregar os CSVs para DataFrames
hero_stats_df = pd.read_csv('Current_Pro_meta.csv')
heroes_df = pd.read_csv('All_Heroes_ID.csv')

# Extrair as colunas 'Name' e 'Hero ID' e salvar em um único arquivo CSV
combined_df = pd.DataFrame({
    'Name': hero_stats_df['Name'],
    'Hero ID': heroes_df['Hero ID']
})

# Salvando em um csv
combined_df.to_csv('hero_name_hero_id.csv', index=False)
