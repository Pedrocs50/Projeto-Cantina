'''OPERAÇÕES RELACIONADAS AOS PRODTUSO'''

from banco import BancoDeDados
from entidades import Entidade

class Produto(Entidade):
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.banco = BancoDeDados()

    def salvar(self):
        conn = self.banco.conectar()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO Produtos (nome, preco, quantidade_em_estoque)
        VALUES (?, ?, ?)''', (self.nome, self.preco, self.quantidade))
        conn.commit()
        conn.close()
        print(f"Produto '{self.nome}' adicionado com sucesso!")

    @staticmethod
    def listar_produtos():
        banco = BancoDeDados()
        conn = banco.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id_produto, nome, preco, quantidade_em_estoque FROM Produtos")
        produtos = cursor.fetchall()
        conn.close()
        return produtos

    def remover(self, id_produto):
        conn = self.banco.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Produtos WHERE id_produto = ?", (id_produto,))
        conn.commit()
        conn.close()
        print(f"Produto com ID {id_produto} foi removido com sucesso.")
