
## Importação do Pandas e Carregamento do CSV
```python
import pandas as pd

# Carregar o CSV para um DataFrame
pro_meta_csv = '../Current_Pro_meta.csv'
df_pro_meta = pd.read_csv(pro_meta_csv)

all_hero_id = '../All_Heroes_ID.csv'
df_heroes_id = pd.read_csv(all_hero_id)


```

### `Pandas:` Estamos utilizando a biblioteca pandas, que é fundamental para a manipulação de dados em Python.

### `Leitura dos CSVs:` Carregamos os arquivos Current_Pro_meta.csv e All_Heroes_ID.csv para DataFrames df_pro_meta e df_heroes_id, respectivamente, facilitando a manipulação dos dados.

## Remoção de Colunas Desnecessárias
```python

# Remover colunas desnecessárias para a normalização e para adicionar performance_id e hero_id
cols_remover = ['Primary Attribute','Attack Type','Attack Range','Name', 'Roles']
df = df.drop(cols_remover, axis=1)


```

### `Remoção de Colunas:` Algumas colunas não são necessárias para a normalização ou para os IDs que vamos adicionar. Por isso, as colunas listadas em cols_remover são removidas do DataFrame.

## Normalização Estatística

```python
# Normalização estatística das colunas
# A normalização Min-Max ajusta os valores de uma coluna para que fiquem em uma escala entre 0 e 1.
col_normalizar = ['Total Pro wins', 'Times Picked', 'Times Banned', 'Win Rate']
for col in col_normalizar:
    if col in df.columns:
        df[col + ' normalized'] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

```
### `Normalização Min-Max:` Ajustamos os valores das colunas de desempenho para que fiquem entre 0 e 1. Isso é útil para comparações e análises.

### `Colunas Normalizadas:` As novas colunas normalizadas são adicionadas ao DataFrame com o sufixo normalized.

##  Adição de performance_id
```python
# Adicionar uma coluna 'performance_id' com valores sequenciais começando em 1
df['performance_id'] = range(1, len(df) + 1)

```
### `performance_id:` Adicionamos uma coluna performance_id com valores sequenciais para identificar cada linha de forma única.

## Mesclagem dos DataFrames
```python
# Mesclar os DataFrames com base no índice, assumindo que o índice representa o ID do herói
df_merged = pd.merge(df, df_heroes_id[['Hero ID']], left_index=True, right_index=True)


```
### `Mesclagem de DataFrames:` Mesclamos os DataFrames df e df_heroes_id com base no índice, que estamos assumindo representar o ID do herói. Isso nos permite combinar os dados de desempenho com os IDs dos heróis.

## Salvamento do DataFrame Mesclado e Normalizado
```python
# Salvar o DataFrame mesclado e normalizado
pro_meta_com_hero_id = './performance_com_hero_id.csv'
df_merged.to_csv(pro_meta_com_hero_id, index=False)

```

### `Salvamento do CSV:` Salvamos o DataFrame mesclado e normalizado em um novo arquivo CSV chamado performance_com_hero_id.csv.
