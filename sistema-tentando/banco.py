'''GERENCIAMENTO DO BANCO DE DADOS'''

import sqlite3

class BancoDeDados:
    def __init__(self, db_name="cantina.db"):
        self.db_name = db_name

    def conectar(self):
        """Conectar ao banco de dados."""
        return sqlite3.connect(self.db_name)

    def criar_tabelas(self):
        """Criar as tabelas necessárias no banco de dados."""
        conn = self.conectar()
        cursor = conn.cursor()

        # Tabela de Produtos
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Produtos (
            id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade_em_estoque INTEGER NOT NULL
        )''')

        # Tabela de Vendas
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Vendas (
            id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
            id_produto INTEGER,
            quantidade_vendida INTEGER,
            data_venda TEXT,
            id_funcionario INTEGER,
            FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto),
            FOREIGN KEY (id_funcionario) REFERENCES Funcionarios(id_funcionario)
        )''')

        # Tabela de Funcionários
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Funcionarios (
            id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            saldo_a_pagar REAL DEFAULT 0
        )''')

        conn.commit()
        conn.close()
