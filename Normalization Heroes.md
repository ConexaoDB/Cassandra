# Nesta apresentação, vamos abordar a importação de dados de heróis de Dota 2 para o Docker e o Cassandra.

## Passos para Importação de Dados

### Carregar os CSVs para DataFrames

```python
import pandas as pd

# Carregar os CSVs para DataFrames
hero_stats_df = pd.read_csv('Current_Pro_meta.csv')
heroes_df = pd.read_csv('All_Heroes_ID.csv')

# Extrair as colunas 'Name' e 'Hero ID' e salvar em um único arquivo CSV
combined_df = pd.DataFrame({
    'Name': hero_stats_df['Name'],
    'Hero ID': heroes_df['Hero ID']
})

# Salvando em um CSV
combined_df.to_csv('heroes.csv', index=False)
```

## Copiar o arquivo CSV para o container do Docker
```
$ docker cp herois.csv conexaodb:/herois.csv
```

## Entrar no container do Docker e usar o keyspace
```
$ docker exec -it conexaodb cqlsh

$ USE dota;
```

## Criar a tabela no Cassandra
```
$ CREATE TABLE dota.heroes (
    hero_id INT PRIMARY KEY,
    attack_range INT,
    attack_type TEXT,
    name TEXT,
    primary_attribute TEXT
);
```
## Dicionário de dados

hero_id: Identificador único do herói (chave primária).<br/>
Tipo: Inteiro.<br/>
Descrição: Identificador único do herói.<br/>

attack_range: Alcance do ataque do herói.<br/>
Tipo: Inteiro.<br/>
Descrição: A distância máxima em que o herói pode atacar um inimigo.<br/>

attack_type: Tipo de ataque do herói (corpo a corpo ou à distância).<br/>
Tipo: Texto.<br/>
Descrição: Indica se o herói ataca corpo a corpo ou à distância.<br/>

name: Nome do herói.<br/>
Tipo: Texto.<br/>
Descrição: O nome do herói.<br/>

primary_attribute: Atributo primário do herói (força, agilidade ou inteligência).<br/>
Tipo: Texto.<br/>
Descrição: O atributo primário do herói, que influencia seu crescimento de estatísticas e seu papel no jogo.<br/>

## Importar os dados do CSV para a tabela

```
$ COPY dota.heroes (hero_id, name, primary_attribute, attack_type, attack_range) FROM 'herois.csv' WITH DELIMITER=',' AND HEADER=TRUE;
```