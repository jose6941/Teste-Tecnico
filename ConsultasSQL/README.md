## Consulta em banco de dados SQL

Consiste na criação de consultas entre tabelas de clientes e pedidos. Obtendo todos os clientes que realizaram pedidos acima de R$ 100, ordenados pelo nome e o total de pedidos realizados por cada cliente.  

### Passos principais
- Criar as tabelas de clientes e pedidos
- Fazer um SELECT que retorne todos os clientes que realizaram pedidos acima de R$ 100, ordenados pelo nome.  
- Fazer um SELECT que retorne o total de pedidos realizados por cada cliente.   

## Lógica do código

</br>

1. **Criação das tabelas:**

Cria as tabelas de clientes e pedidos com seus respectivos campos e chaves.

```bash

    CREATE TABLE clientes(
        id INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL
    );

```

```bash

    CREATE TABLE pedidos(
        id INT PRIMARY KEY AUTO_INCREMENT,
        id_cliente INT NOT NULL,
        data DATE NOT NULL,
        total DECIMAL(10,2) NOT NULL,
        FOREIGN KEY (id_clientes) REFERENCES clientes(id)
    );
    
```

</br>

2. **Consulta dos clientes que fizeram algum pedido:**

Neste código há um SELECT para todos os clientes que realizaram pedidos acima de R$ 100, ordenados pelo nome. Foi utilizado o inner join, que foi escrito apenas join, para retornar apenas os clientes que possuem pelo menos um pedido acima de R$ 100.

```bash

    SELECT DISTINCT c.id,c.nome, c.email # Seleciona os cliente evitando os campos duplicados
    FROM clientes c 
    JOIN pedidos p ON c.id = p.id_clientes # Retorna os clientes que possuem algum pedido
    WHERE p.total > 100 # Apenas para pedidos acima de R$ 100
    ORDER BY c.nome # Ordenado por nome
    
```

</br>

3. **Consulta do total de pedidos realizados por cada cliente:**

Neste código há um SELECT para mostrar quantos pedidos foram feitos para cada cliente, mesmo que o mesmo não tenha nenhum. Dessa forma foi utilizado o LEFT JOIN, para mostrar todos os clientes mesmo que algum não tenha feito nenhum pedido.

```bash

    SELECT c.id, c.nome, COUNT(p.id) AS total_pedidos # Pega as informações do cliente e o numero de pedidos
    FROM clientes c
    LEFT JOIN pedidos p ON c.id = p.id_cliente # Retorna todos os clientes, mesmo os que não têm pedidos
    GROUP BY c.id, c.nome # Agrupa os resultados por id e nome do cliente
    ORDER BY total_pedidos DESC # Ordena pelo total de pedidos de forma decrescente
    
```
