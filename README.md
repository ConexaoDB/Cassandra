# Configuração do Cassandra com Docker

Este README fornece instruções sobre como configurar um ambiente Cassandra usando Docker e como preparar e importar datasets para análise.

## Pré-requisitos

- Docker instalado em sua máquina
- Datasets preparados no formato CSV

## Passo a Passo

### 1. Baixar a Imagem do Cassandra

Para baixar a imagem oficial do Cassandra do Docker Hub, execute o seguinte comando no terminal:

$ docker pull cassandra

 ### 2. Iniciar o Container do Cassandra
Execute o container do Cassandra com o nome conexaodb:

$ docker run --name conexaodb -d cassandra:latest

### 3. Preparação dos Dados
Antes de copiar os dados, certifique-se de que estão no formato CSV e que a estrutura (nomes de colunas, tipos de dados) é conhecida.

### 4. Copiar o Dataset para o Container
Substitua <caminho_do_seu_pc> pelo caminho onde seu arquivo CSV está localizado.

Todos os Heróis
$ docker cp <caminho_do_seu_pc>/All_Heroes_ID.csv conexaodb:/All_Heroes_ID.csv

Metas Atuais
$ docker cp <caminho_do_seu_pc>/Current_Pro_meta.csv conexaodb:/Current_Pro_meta.csv

### 5. Acessar o Cassandra via CQLSH
Para acessar o shell do Cassandra (CQLSH) dentro do container, utilize:

$ docker exec -it conexaodb cqlsh

### 6. Criar a Keyspace
Dentro do CQLSH, crie uma keyspace chamada dota com a seguinte configuração de replicação:

$ CREATE KEYSPACE IF NOT EXISTS dota WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 1};

### 7. Entrar na Keyspace

$ USE dota;

### 8. Criar as Tabelas

### Tabela de Heróis

$ CREATE TABLE IF NOT EXISTS all_heroes (
    id INT PRIMARY KEY,
    name TEXT,
    hero_id INT
);

### Tabela de Estatísticas dos Heróis

$ CREATE TABLE IF NOT EXISTS hero_stats (
    id INT PRIMARY KEY,
    name TEXT,
    primary_attribute TEXT,
    attack_type TEXT,
    attack_range INT,
    roles TEXT,
    total_pro_wins INT,
    times_picked INT,
    times_banned INT,
    win_rate FLOAT,
    niche_hero BOOLEAN
);

### 9. Carregar Dados:

### Carregar Dados na Tabela de Heróis

$ COPY all_heroes (id, name, hero_id)
FROM '/All_Heroes_ID.csv'
WITH HEADER = TRUE;

### Carregar Dados na Tabela de Estatísticas dos Heróis

$ COPY hero_stats (id, name, primary_attribute, attack_type, attack_range, roles, total_pro_wins, times_picked, times_banned, win_rate, niche_hero)
FROM '/Current_Pro_meta.csv'
WITH HEADER = TRUE;


### Consulta de Dados Básicos

###  All Heroes
$ SELECT * FROM all_heroes LIMIT 10;

### Hero Stats
$ SELECT * FROM hero_stats WHERE niche_hero = TRUE;

# Configuração do PostgreSQL com Docker

## Pré-requisitos

- Docker instalado em sua máquina.
- Datasets preparados no formato CSV.

## Passo a Passo

### 1. Baixar a Imagem do PostgreSQL

Para baixar a imagem oficial do PostgreSQL do Docker Hub, execute o seguinte comando no terminal:
$ docker pull postgres

### 2. Iniciar o Container do PostgreSQL

Execute o container do PostgreSQL com o nome conexaodbpg e senha configurada:
$ docker run --name conexaodbpg -e POSTGRES_PASSWORD=123 -d -p 5432:5432 postgres

### 3. Preparação dos Dados

Antes de copiar os dados, certifique-se de que estão no formato CSV e que a estrutura (nomes de colunas, tipos de dados) é conhecida.

### 4. Copiar o Dataset para o Container

Substitua <caminho_do_seu_pc> pelo caminho onde seu arquivo CSV está localizado.

- Todos os Heróis:
$ docker cp <caminho_do_seu_pc>/all_heroes.csv conexaodbpg:/var/lib/postgresql/data/all_heroes.csv

- Estatísticas dos Heróis:
$ docker cp <caminho_do_seu_pc>/stats_heroes.csv conexaodbpg:/var/lib/postgresql/data/stats_heroes.csv

### 5. Acessar o PostgreSQL via PSQL

Para acessar o shell do PostgreSQL dentro do container, utilize:
$ docker exec -it conexaodbpg psql -U postgres

### 6. Criar o Banco de Dados

Dentro do PSQL, crie um banco de dados chamado dota:
$ CREATE DATABASE dota;

### 7. Conectar ao Banco de Dados

$ \c dota;
