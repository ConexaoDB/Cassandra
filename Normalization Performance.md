# Nesta apresentação, vamos abordar a importação de dados de heróis de Dota 2 para o Docker e o Cassandra.

## Passos para Importação de Dados

### Usando a biblioteca pandas
```python
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
```


## Entrar no container do Docker e usar o keyspace


$ docker exec -it conexaodb cqlsh

$ USE dota;



## Criar a tabela no Cassandra

$ CREATE TABLE dota.heroes (
    hero_id INT PRIMARY KEY,<br/>
    attack_range INT,<br/>
    attack_type TEXT,<br/>
    name TEXT,<br/>
    primary_attribute TEXT<br/>
);
 

 ### Dicionário de dados

- **hero_id** (INT):
  - Identificador único do herói (chave primária).
  - Tipo: Inteiro

- **attack_range** (INT):
  - Alcance do ataque do herói.
  - Tipo: Inteiro
  - Descrição: A distância máxima em que o herói pode atacar um inimigo.

- **attack_type** (TEXT):
  - Tipo de ataque do herói (corpo a corpo ou à distância).
  - Tipo: Texto
  - Descrição: Indica se o herói ataca corpo a corpo ou à distância.

- **name** (TEXT):
  - Nome do herói.
  - Tipo: Texto
  - Descrição: O nome do herói.

- **primary_attribute** (TEXT):
  - Atributo primário do herói (força, agilidade ou inteligência).
  - Tipo: Texto
  - Descrição: O atributo primário do herói, que influencia seu crescimento de estatísticas e seu papel no jogo.


## Importar os dados do CSV para a tabela


$ COPY dota.heroes (hero_id, name, primary_attribute, attack_type, attack_range) FROM 'herois.csv' WITH DELIMITER=',' AND HEADER=TRUE;

```
