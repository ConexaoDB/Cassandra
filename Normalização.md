# Importar arquivo CSV para o Docker:
## Copie o arquivo CSV que deseja importar para o container do Docker onde o Cassandra está sendo executado. Você pode fazer isso usando o comando $ $ $ docker cp do terminal.

$ docker cp hero_stats.csv conexaodb:/caminho/no/container/hero_stats.csv

# Entrar no container do Docker:
## Use o comando docker exec para entrar no container onde o Cassandra está sendo executado.

$ docker exec -it NOME_DO_CONTAINER cqlsh

# Criar um keyspace :
## Se você ainda não tiver um keyspace, pode criar um usando o seguinte comando:
sql

$ CREATE KEYSPACE IF NOT EXISTS dota WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
# Usar o keyspace:
## Use o keyspace que você acabou de criar (ou o que já existe) para as operações seguintes.

$ USE dota;
# Criar a tabela:
## Crie a tabela com as colunas desejadas. Se precisar, adapte o exemplo abaixo ao seu caso.

$ CREATE TABLE IF NOT EXISTS nome_da_tabela (
    id int PRIMARY KEY,
    attack_range int,
    attack_type text,
    name text,
    niche_hero boolean,
    primary_attribute text,
    times_banned int,
    times_banned_normalized float,
    times_picked int,
    times_picked_normalized float,
    total_pro_wins int,
    total_pro_wins_normalized float,
    win_rate float,
    win_rate_normalized float
);

# Importar os dados do CSV para a tabela:
## Com a tabela criada, você pode importar os dados do arquivo CSV usando o comando COPY.

$ COPY hero_stats (id, attack_range, attack_type, name, niche_hero, primary_attribute, times_banned, times_banned_normalized, times_picked, times_picked_normalized, total_pro_wins, total_pro_wins_normalized, win_rate, win_rate_normalized) FROM '/caminho/no/container/arquivo.csv' WITH DELIMITER=',' AND HEADER=TRUE;
