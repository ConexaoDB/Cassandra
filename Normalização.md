
## Normalização Min-Max: Também conhecida como escala min-max, essa técnica redimensiona os dados para um intervalo específico (por exemplo, entre 0 e 1). A fórmula básica é:

![Fórmula de normalização](/formula_normalizacao.png)

## Pata realizar a normalização estatística das colunas 'Total Pro wins', 'Times Picked', 'Times Banned' e 'Win Rate':
### Importar bibliotecas:

import pandas as pd

# DataFrame de exemplo

data = {<br/>
    'Name': ['Abaddon', 'Alchemist', 'Ancient Apparition', 'Anti-Mage'],<br/>
    'Total Pro wins': [8, 15, 20, 30],<br/>
    'Times Picked': [24, 30, 25, 35],<br/>
    'Times Banned': [61, 45, 50, 40],<br/>
    'Win Rate': [33.33, 55.55, 66.66, 75.00]<br/>
}<br/>
df = pd.DataFrame(data)

## Normalização estatística:

Colunas a serem normalizadas<br/>
cols_to_normalize = ['Total Pro wins', 'Times Picked', 'Times Banned', 'Win Rate']<br/>

### Normalização min-max<br/>
for col in cols_to_normalize:<br/>
    df[col + '_normalized'] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())<br/>

## Exibir DataFrame resultante
print(df)

## Salvar o DataFrame normalizado

pro_meta = './pro_meta.csv'<br/>
df.to_csv(pro_meta, index=False)<br/>


## Importar arquivo CSV para o Docker:
### Copie o arquivo CSV que deseja importar para o container do Docker onde o Cassandra está sendo executado. Você pode fazer isso usando o comando $ $ $ docker cp do terminal.

$ docker cp hero_stats.csv conexaodb:/caminho/no/container/hero_stats.csv<br/>

# Entrar no container do Docker:<br/>
## Use o comando docker exec para entrar no container onde o Cassandra está sendo executado.<br/>

$ docker exec -it conexaodb cqlsh<br/>

# Criar um keyspace :
## Se você ainda não tiver um keyspace, pode criar um usando o seguinte comando:

$ CREATE KEYSPACE IF NOT EXISTS dota WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};<br/>
# Usar o keyspace:<br/>
## Use o keyspace que você acabou de criar para as operações seguintes.<br/>

$ USE dota;
# Criar a tabela:
## Crie a tabela com as colunas desejadas. Se precisar, adapte o exemplo abaixo ao seu caso.

$ CREATE TABLE IF NOT EXISTS hero_stats (<br/>
    id int PRIMARY KEY,<br/>
    attack_range int,<br/>
    attack_type text,<br/>
    name text,<br/>
    niche_hero boolean,<br/>
    primary_attribute text,<br/>
    times_banned int,<br/>
    times_banned_normalized float,<br/>
    times_picked int,<br/>
    times_picked_normalized float,<br/>
    total_pro_wins int,<br/>
    total_pro_wins_normalized float,<br/>
    win_rate float,<br/>
    win_rate_normalized float<br/>
);

# Importar os dados do CSV para a tabela:
## Com a tabela criada, você pode importar os dados do arquivo CSV usando o comando COPY.

$ COPY hero_stats (id, Name, Primary_Attribute, Attack_Type, Attack_Range, Total_Pro_Wins, Times_Picked, Times_Banned, Win_Rate, Niche_Hero, Total_Pro_Wins_Normalized, Times_Picked_Normalized, Times_Banned_Normalized, Win_Rate_Normalized) FROM '/herostats.csv' WITH DELIMITER=',' AND HEADER=TRUE;

