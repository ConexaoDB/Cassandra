import pandas as pd

# Carregar o CSV para um DataFrame
caminho_para_csv = '../Current_Pro_meta.csv'
df = pd.read_csv(caminho_para_csv)

# removendo coluna para normalização 
df = df.drop('Roles', axis=1)
# Normalização estatística das colunas
# a normalização Min-Max ajusta os valores de uma coluna para que fiquem em uma escala entre 0 e 1.
col_normalizar = ['Total Pro wins', 'Times Picked', 'Times Banned', 'Win Rate']
for col in col_normalizar:
    if col in df.columns:
        df[col + ' normalized'] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

# Salvar o DataFrame normalizado
pro_meta = './pro_meta.csv'
df.to_csv(pro_meta, index=False)
