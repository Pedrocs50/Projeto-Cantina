# 1. Conectar ao Banco de Dados
Para abrir um banco de dados SQLite:

sql
Copiar código
sqlite3 nome_do_banco.db
Se o arquivo não existir, ele será criado automaticamente.

2. Criar Tabelas
Para criar uma tabela:

sql
Copiar código
CREATE TABLE nome_da_tabela (
    coluna1 tipo_de_dado PRIMARY KEY,
    coluna2 tipo_de_dado,
    coluna3 tipo_de_dado
);
Exemplo:

sql
Copiar código
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
);
3. Inserir Dados
Para inserir dados em uma tabela:

sql
Copiar código
INSERT INTO nome_da_tabela (coluna1, coluna2, coluna3)
VALUES (valor1, valor2, valor3);
Exemplo:

sql
Copiar código
INSERT INTO clientes (nome, email)
VALUES ('João Silva', 'joao@example.com');
4. Selecionar Dados
Para selecionar todos os dados de uma tabela:

sql
Copiar código
SELECT * FROM nome_da_tabela;
Para selecionar dados específicos:

sql
Copiar código
SELECT coluna1, coluna2 FROM nome_da_tabela WHERE condição;
Exemplo:

sql
Copiar código
SELECT nome, email FROM clientes WHERE id = 1;
5. Atualizar Dados
Para atualizar registros:

sql
Copiar código
UPDATE nome_da_tabela
SET coluna1 = novo_valor1, coluna2 = novo_valor2
WHERE condição;
Exemplo:

sql
Copiar código
UPDATE clientes
SET email = 'novo_email@example.com'
WHERE id = 1;
6. Excluir Dados
Para excluir registros de uma tabela:

sql
Copiar código
DELETE FROM nome_da_tabela WHERE condição;
Exemplo:

sql
Copiar código
DELETE FROM clientes WHERE id = 1;
7. Excluir Tabelas
Para excluir uma tabela inteira:

sql
Copiar código
DROP TABLE nome_da_tabela;
8. Alterar Tabelas
Para adicionar uma nova coluna:

sql
Copiar código
ALTER TABLE nome_da_tabela ADD COLUMN nova_coluna tipo_de_dado;
Para renomear uma tabela:

sql
Copiar código
ALTER TABLE nome_da_tabela RENAME TO novo_nome_da_tabela;
9. Criar Índices
Para criar um índice (melhora a busca):

sql
Copiar código
CREATE INDEX nome_do_indice ON nome_da_tabela (coluna);
10. Visualizar Esquema
Para visualizar a estrutura de uma tabela:

sql
Copiar código
.schema nome_da_tabela
11. Listar Tabelas
Para listar todas as tabelas no banco de dados:

sql
Copiar código
.tables
12. Exibir Dados de uma Tabela
Para exibir os dados de uma tabela específica:

sql
Copiar código
SELECT * FROM nome_da_tabela;
13. Limpar a Tela
Para limpar a tela do terminal (em ambientes SQLite interativos):

sql
Copiar código
.clear
14. Exibir Informações do Banco de Dados
Para exibir informações sobre o banco de dados em uso:

sql
Copiar código
.databases
15. Salvar e Sair
Para salvar as alterações no banco de dados e sair do SQLite:

sql
Copiar código
.exit
16. Transações
Para iniciar uma transação:

sql
Copiar código
BEGIN TRANSACTION;
Para finalizar a transação (com commit):

sql
Copiar código
COMMIT;
Para reverter (rollback) uma transação:

sql
Copiar código
ROLLBACK;
17. Usando Funções Agregadas
SQLite possui várias funções agregadas como COUNT, SUM, AVG, MAX, e MIN. Exemplo de contagem de registros:

sql
Copiar código
SELECT COUNT(*) FROM nome_da_tabela;
Para calcular a soma de uma coluna:

sql
Copiar código
SELECT SUM(coluna) FROM nome_da_tabela;
Esses são os principais comandos que você pode usar ao trabalhar com SQLite. O SQLite também oferece suporte a muitos outros recursos avançados, como JOIN, GROUP BY, ORDER BY, entre outros.