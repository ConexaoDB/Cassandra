# Configuração do PostgreSQL com Docker

Este guia fornece instruções simples sobre como configurar um ambiente PostgreSQL usando Docker e como preparar e importar datasets para análise.

## Pré-requisitos

- Docker instalado em sua máquina
- Datasets preparados no formato CSV

## Passo a Passo

### 1. Baixar a Imagem do PostgreSQL

$ docker pull postgres


### 2. Iniciar o Container do PostgreSQL

$ docker run --name conexaodbpg -e POSTGRES_PASSWORD=123 -d -p 5432:5432 postgres


### 3. Preparação dos Dados

Certifique-se de que os dados estão no formato CSV e que a estrutura (nomes de colunas, tipos de dados) é conhecida.

### 4. Copiar o Dataset para o Container

Substitua <caminho do arquivo> pelo caminho onde seu arquivo CSV está localizado.

- Todos os Heróis:

$ docker cp <caminho do arquivo>/all_heroes.csv conexaodbpg:/var/lib/postgresql/data/all_heroes.csv

csharp
Copiar código

- Estatísticas dos Heróis:

$ docker cp <caminho do arquivo>/stats_heroes.csv conexaodbpg:/var/lib/postgresql/data/stats_heroes.csv

bash
Copiar código

### 5. Acessar o PostgreSQL via PSQL

Para acessar o shell do PostgreSQL dentro do container, utilize:

$ docker exec -it conexaodbpg psql -U postgres


### 6. Criar o Banco de Dados

Dentro do PSQL, crie um banco de dados chamado dota:

$ CREATE DATABASE dota;

### 7. Conectar ao Banco de Dados

$ \c dota;

## Criar tabelas


### Tabela Hero Stats

CREATE TABLE hero_stats (
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



## Tabela Hero

CREATE TABLE hero (
    index SERIAL PRIMARY KEY,
    name TEXT,
    hero_id INT
);
