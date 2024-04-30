# Cassandra

## **Baixar e rodar a imagem do Cassandra**

docker pull cassandra

## INICIAR DOCKER

docker run --name conexaodb -d cassandra:latest


Certifique-se de que o seu dataset está no formato correto (CSV, por exemplo) e que você entende a estrutura dos dados (nomes de colunas, tipos de dados, etc.).

## **Copiar o Dataset para o Contêiner**

### Todos os Heros

docker cp /home/hitallo/Documents/cassandra/dota2metas/archive/All_Heroes_ID.csv conexaodb:/All_Heroes_ID.csv

docker cp C:\Users\Louise\Documents\hitallo\archive\All_Heroes_ID.csv  conexaodb:/All_Heroes_ID.csv

### Metas

docker cp /home/hitallo/Documents/cassandra/dota2metas/archive/Current_Pro_meta.csv conexaodb:/Current_Pro_meta.csv

## **Acessar o Cassandra via CQLSH**

docker exec -it conexaodb cqlsh

## CRIAR A KEYSPACE(DATABASE)

CREATE KEYSPACE IF NOT EXISTS dota WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

