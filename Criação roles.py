import pandas as pd

# Carregar os CSVs para DataFrames
heroes_df = pd.read_csv('../../All_Heroes_ID.csv')
hero_stats_df = pd.read_csv('../../Current_Pro_meta.csv')

# Selecionar apenas as colunas 'Roles'
selected_columns = {
    'Roles': hero_stats_df['Roles']
}

# Criar um novo DataFrame com as colunas selecionadas
selected_df = pd.DataFrame(selected_columns)

# Adicionar a coluna 'role_id' ao DataFrame
selected_df['role_id'] = range(len(selected_df))

# Salvar as colunas selecionadas em um novo CSV
selected_df.to_csv('role_id_roles.csv', index=False)
