# Comandos SQL para Sistema de Cantina

Este documento contém os comandos SQL essenciais para manipulação das tabelas **`Produtos`** e **`Vendas`** em um sistema de controle de vendas para uma cantina.

---

## 1. Comandos para Tabela `Produtos`

### 1.1 Adicionar um Novo Produto
Para adicionar um novo produto na tabela `Produtos`, use o comando `INSERT`:

```sql
    INSERT INTO Produtos (nome, preco, quantidade_em_estoque)
    VALUES ('Produto Exemplo', 10.50, 100);
    Este comando insere um novo produto com nome, preço e quantidade em estoque.
```

### 1.2 A