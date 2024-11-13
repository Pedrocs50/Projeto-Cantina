# vendas.py
from banco import BancoDeDados
from datetime import datetime
from produtos import Produto

class Venda:
    def __init__(self, id_produto, quantidade_vendida):
        self.id_produto = id_produto
        self.quantidade_vendida = quantidade_vendida
        self.banco = BancoDeDados()

    def realizar_venda(self):
        """Método para registrar uma venda e atualizar o estoque."""
        conn = self.banco.conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT quantidade_em_estoque, nome FROM Produtos WHERE id_produto = ?", (self.id_produto,))
        produto = cursor.fetchone()

        if produto:
            quantidade_em_estoque = produto[0]

            if quantidade_em_estoque >= self.quantidade_vendida:
                # Registrar a venda na tabela Vendas
                data_venda = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute('''
                INSERT INTO Vendas (id_produto, quantidade_vendida, data_venda)
                VALUES (?, ?, ?)''', (self.id_produto, self.quantidade_vendida, data_venda))

                # Atualizar o estoque do produto
                nova_quantidade = quantidade_em_estoque - self.quantidade_vendida
                cursor.execute('''UPDATE Produtos
                                  SET quantidade_em_estoque = ?
                                  WHERE id_produto = ?''', (nova_quantidade, self.id_produto))

                conn.commit()
                print(f"{self.quantidade_vendida} unidades do produto '{produto[1]}' foram vendidas com sucesso!")
            else:
                print("Não há estoque suficiente para essa venda.")
        else:
            print(f"Produto com ID {self.id_produto} não encontrado.")

        self.banco.fechar_conexao(conn)

    @staticmethod
    def listar_vendas():
        """Método estático para listar todas as vendas realizadas."""
        banco = BancoDeDados()
        conn = banco.conectar()
        cursor = conn.cursor()

        cursor.execute('''
        SELECT Vendas.id_venda, Produtos.nome, Vendas.quantidade_vendida, Vendas.data_venda
        FROM Vendas
        JOIN Produtos ON Vendas.id_produto = Produtos.id_produto''')

        vendas = cursor.fetchall()

        if vendas:
            print("Histórico de Vendas:")
            print("ID Venda | Produto | Quantidade Vendida | Data da Venda")
            print("-" * 60)
            for venda in vendas:
                print(f"{venda[0]} | {venda[1]} | {venda[2]} | {venda[3]}")
        else:
            print("Nenhuma venda registrada.")

        banco.fechar_conexao(conn)
