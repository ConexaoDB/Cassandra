# Apresentação

Nesta apresentação, vamos abordar a criação de um arquivo CSV que relaciona os papéis (roles) dos heróis de Dota 2 com seus IDs.

## Passos para Criação do Arquivo CSV

### Carregar os CSVs para DataFrames

```python
import pandas as pd

# Carregar os CSVs para DataFrames
hero_stats_df = pd.read_csv('Current_Pro_meta.csv')
heroes_df = pd.read_csv('All_Heroes_ID.csv')

## Extrair as colunas 'Roles' e 'Hero ID' e salvar em um único arquivo CSV
combined_df = pd.DataFrame({
    'role_id': hero_stats_df['Roles'],
    'hero_id': heroes_df['Hero ID']
})

# Salvando em um CSV
combined_df.to_csv('hero_roles.csv', index=False)

## Copiar CSV para o Docker do Cassandra
$ docker exec -it conexaodb cqlsh


$ USE dota;

$ CREATE TABLE IF NOT EXISTS role (
    role_id INT PRIMARY KEY,
    role TEXT
);

## Importar os Dados do CSV para a Tabela

$ COPY roles (role_id, role) FROM '/hero_id_roles.csv' WITH DELIMITER=',' AND HEADER=TRUE;
