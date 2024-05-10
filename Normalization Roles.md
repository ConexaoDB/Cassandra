## Para a criação da nova tabela vamos usar pandas

```python
import pandas as pd

## Carregar os CSVs:

Carregamos os arquivos CSV 'All_Heroes_ID.csv' e 'Current_Pro_meta.csv' em DataFrames chamados heroes_df e hero_stats_df.

## Selecionar colunas: 

Criamos um novo DataFrame selected_df com as colunas 'Hero ID' de heroes_df e 'Roles' de hero_stats_df.  

## Salvar em CSV: 

Salvamos o DataFrame selected_df no arquivo 'hero_id_roles.csv'
```

## Copiar CSV para dentro do docker do cassandra
```
$ docker cp /home/hitallo/faculdade/terca/filipe/CSV/hero_id_roles.csv conexaodb:/hero_id_roles.csv
```

## Entra no cqlsh para criar tabela:
```
$ docker exec -it conexaodb cqlsh

$ USE dota;

$ CREATE TABLE IF NOT EXISTS role (
    role_id INT PRIMARY KEY,
    role TEXT
);
```
## Dicionário de dados

role_id: Identificador único do papel do herói (chave primária).<br/>
Tipo: Inteiro.<br/>
Descrição: Identificador único do papel do herói.<br/>

role: Nome do papel do herói.<br/>
Tipo: Texto.<br/>
Descrição: O nome do papel ou função que o herói desempenha no jogo, como "Carry", "Support", "Offlaner", etc.<br/>


## Copy o CSV para a tabela
```
$ COPY roles (hero_id, roles) FROM '/hero_id_roles.csv' WITH DELIMITER=',' AND HEADER=TRUE;
```