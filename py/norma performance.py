import pandas as pd

# Carregar o CSV para um DataFrame
caminho_para_csv = '../Current_Pro_meta.csv'
df = pd.read_csv(caminho_para_csv)

# Remover colunas desnecessárias para a normalização e para adicionar performance_id e hero_id
cols_remover = ['Primary Attribute','Attack Type','Attack Range','Name', 'Roles']
df = df.drop(cols_remover, axis=1)

# Normalização estatística das colunas
# A normalização Min-Max ajusta os valores de uma coluna para que fiquem em uma escala entre 0 e 1.
col_normalizar = ['Total Pro wins', 'Times Picked', 'Times Banned', 'Win Rate']
for col in col_normalizar:
    if col in df.columns:
        df[col + ' normalized'] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

# Adicionar uma coluna 'performance_id' com valores sequenciais começando em 1
df['performance_id'] = range(1, len(df) + 1)

# Adicionar uma coluna 'hero_id' com valores fictícios para ilustrar como seria adicionado
df['hero_id'] = range(1, len(df) + 1)

# Salvar o DataFrame normalizado
pro_meta = './performance.csv'
df.to_csv(pro_meta, index=False)
