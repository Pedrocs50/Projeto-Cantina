# Comandos SQL para Sistema de Cantina

Este documento contém os comandos SQL essenciais para manipulação das tabelas **`Produtos`** e **`Vendas`** em um sistema de controle de vendas para uma cantina.

---

## 1. Comandos para Tabela `Produtos`

### 1.1 Adicionar um Novo Produto
Para adicionar um novo produto na tabela `Produtos`, use o comando `INSERT`:

```sql
INSERT INTO Produtos (nome, preco, quantidade_em_estoque)
VALUES ('Produto Exemplo', 10.50, 100);
Este comando insere um novo produto com nome, preço e quantidade em estoque.´´´

### 1.2 Atualizar Informações de um Produto
Para atualizar o nome, preço ou quantidade de um produto existente, use o comando UPDATE:

sql
Copiar código
UPDATE Produtos
SET nome = 'Produto Novo', preco = 12.50, quantidade_em_estoque = 150
WHERE id_produto = 1;
Esse comando atualiza o produto com id_produto = 1.

1.3 Remover um Produto
Para remover um produto da tabela, use o comando DELETE:

sql
Copiar código
DELETE FROM Produtos
WHERE id_produto = 1;
Esse comando remove o produto com id_produto = 1 da tabela Produtos.

1.4 Selecionar Todos os Produtos
Para listar todos os produtos armazenados na tabela Produtos, use:

sql
Copiar código
SELECT * FROM Produtos;
Esse comando retorna todos os produtos e suas informações.

1.5 Selecionar um Produto Específico
Para selecionar um produto específico pela chave id_produto, use o comando SELECT:

sql
Copiar código
SELECT * FROM Produtos
WHERE id_produto = 1;
Esse comando retorna o produto com id_produto = 1.

2. Comandos para Tabela Vendas
Agora, a tabela Vendas é onde você armazena as informações sobre as vendas realizadas, e você provavelmente precisará interagir com ela para adicionar vendas, calcular valores totais, e atualizar o estoque.

2.1 Registrar uma Venda
Para registrar uma venda na tabela Vendas, use o comando INSERT:

sql
Copiar código
INSERT INTO Vendas (id_produto, quantidade_vendida, data_venda)
VALUES (1, 5, '2024-11-13 12:00:00');
Este comando registra a venda de 5 unidades do produto com id_produto = 1 no banco de dados, associando a venda à data e hora.

2.2 Atualizar Informações de uma Venda
Para atualizar os dados de uma venda registrada (ex: quantidade ou data), use o comando UPDATE:

sql
Copiar código
UPDATE Vendas
SET quantidade_vendida = 10, data_venda = '2024-11-13 14:00:00'
WHERE id_venda = 1;
Esse comando atualiza a venda com id_venda = 1, alterando a quantidade vendida para 10 e a data da venda.

2.3 Remover uma Venda
Para remover uma venda da tabela Vendas, use o comando DELETE:

sql
Copiar código
DELETE FROM Vendas
WHERE id_venda = 1;
Esse comando apaga a venda com id_venda = 1 da tabela Vendas.

2.4 Selecionar Todas as Vendas
Para listar todas as vendas registradas, use:

sql
Copiar código
SELECT * FROM Vendas;
Esse comando retorna todas as vendas registradas na tabela Vendas, com seus respectivos id_produto, quantidade_vendida, e data_venda.

2.5 Selecionar Vendas de um Produto Específico
Para listar todas as vendas de um produto específico, use o JOIN para conectar as tabelas Produtos e Vendas:

sql
Copiar código
SELECT Vendas.id_venda, Produtos.nome, Vendas.quantidade_vendida, Vendas.data_venda
FROM Vendas
JOIN Produtos ON Vendas.id_produto = Produtos.id_produto
WHERE Produtos.id_produto = 1;
Esse comando retorna todas as vendas de um produto específico, baseado no id_produto (neste caso, id_produto = 1).

3. Comandos para Cálculos e Agregações
3.1 Calcular o Total Vendido de um Produto (Quantidade * Preço)
Para calcular o valor total de um produto vendido, multiplicando a quantidade vendida pelo preço do produto, use uma consulta com agregação e um JOIN:

sql
Copiar código
SELECT Produtos.nome, SUM(Vendas.quantidade_vendida * Produtos.preco) AS total_vendido
FROM Vendas
JOIN Produtos ON Vendas.id_produto = Produtos.id_produto
WHERE Produtos.id_produto = 1
GROUP BY Produtos.id_produto;
Esse comando calcula o total vendido de um produto específico (por exemplo, id_produto = 1), multiplicando a quantidade vendida pelo preço do produto e somando o total de todas as vendas.

3.2 Calcular o Total de Vendas (Somar todas as vendas)
Para calcular o total de todas as vendas feitas, somando o valor de todas as transações, use:

sql
Copiar código
SELECT SUM(Vendas.quantidade_vendida * Produtos.preco) AS total_vendas
FROM Vendas
JOIN Produtos ON Vendas.id_produto = Produtos.id_produto;
Esse comando retorna o total de todas as vendas realizadas, multiplicando a quantidade de cada venda pelo preço do produto e somando todos os resultados.

3.3 Contar o Número de Vendas Realizadas
Para contar quantas vendas foram realizadas de um produto ou no total, use o COUNT:

sql
Copiar código
SELECT COUNT(*) AS numero_de_vendas
FROM Vendas
WHERE id_produto = 1;
Esse comando retorna o número de vezes que o produto com id_produto = 1 foi vendido.

4. Comandos de Agregação e Filtros
4.1 Vendas por Data (Filtrar Vendas em um Período Específico)
Para listar todas as vendas realizadas dentro de um período específico (por exemplo, entre 2024-11-01 e 2024-11-15), use o comando WHERE com a data:

sql
Copiar código
SELECT Vendas.id_venda, Produtos.nome, Vendas.quantidade_vendida, Vendas.data_venda
FROM Vendas
JOIN Produtos ON Vendas.id_produto = Produtos.id_produto
WHERE Vendas.data_venda BETWEEN '2024-11-01' AND '2024-11-15';
Esse comando retorna todas as vendas realizadas entre 1º de novembro de 2024 e 15 de novembro de 2024.

4.2 Top Produtos Mais Vendidos
Para listar os produtos mais vendidos, ordenando pela quantidade total vendida, use o GROUP BY e ORDER BY:

sql
Copiar código
SELECT Produtos.nome, SUM(Vendas.quantidade_vendida) AS total_vendido
FROM Vendas
JOIN Produtos ON Vendas.id_produto = Produtos.id_produto
GROUP BY Produtos.id_produto
ORDER BY total_vendido DESC;
Esse comando retorna a lista dos produtos mais vendidos, ordenados pela quantidade vendida.

5. Consultas para Relatórios
5.1 Relatório de Vendas por Produto
Para gerar um relatório de vendas por produto, com total de unidades vendidas e o valor total de vendas, use:

sql
Copiar código
SELECT Produtos.nome, SUM(Vendas.quantidade_vendida) AS total_unidades_vendidas, SUM(Vendas.quantidade_vendida * Produtos.preco) AS total_valor_vendido
FROM Vendas
JOIN Produtos ON Vendas.id_produto = Produtos.id_produto
GROUP BY Produtos.id_produto;
Esse comando gera um relatório com o nome de cada produto, o total de unidades vendidas e o total de vendas em valor monetário.

6. Dicas Adicionais
Join entre tabelas: Para trabalhar com dados que envolvem mais de uma tabela, use sempre o JOIN para fazer a ligação entre elas, como no exemplo de vendas.
Agregação: Utilize funções como SUM(), COUNT(), AVG() e GROUP BY para realizar cálculos e gerar relatórios de vendas ou estoque.
Filtros de Data: Para analisar vendas em determinados períodos, use o filtro de data com WHERE e BETWEEN ou DATE() para facilitar a manipulação de datas.
Conclusão
Esses comandos SQL são os mais comuns e úteis para trabalhar com o banco de dados de um sistema de controle de cantina. Eles permitem adicionar, remover e atualizar produtos e vendas, bem como calcular totais de vendas, gerar relatórios e filtrar dados de acordo com as necessidades do sistema.

