CREATE TABLE clientes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE pedidos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    data DATE NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_clientes) REFERENCES clientes(id)
);

SELECT DISTINCT c.id,c.nome, c.email 
FROM clientes c 
JOIN pedidos p ON c.id = p.id_clientes 
WHERE p.total > 100 
ORDER BY c.nome

SELECT c.id, c.nome, COUNT(p.id) AS total_pedidos
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.id_cliente
GROUP BY c.id, c.nome
ORDER BY total_pedidos DESC