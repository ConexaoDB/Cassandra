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
