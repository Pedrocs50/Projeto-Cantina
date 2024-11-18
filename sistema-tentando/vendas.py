'''OPERAÇÕES RELACIONADAS ÀS VENDAS'''

from banco import BancoDeDados
from datetime import datetime
from funcionarios import Funcionario

class Venda:
    def __init__(self, id_produto, quantidade_vendida, id_funcionario=None):
        self.id_produto = id_produto
        self.quantidade_vendida = quantidade_vendida
        self.id_funcionario = id_funcionario
        self.banco = BancoDeDados()

    def realizar_venda(self):
        conn = self.banco.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT quantidade_em_estoque, preco FROM Produtos WHERE id_produto = ?", (self.id_produto,))
        produto = cursor.fetchone()

        if produto and produto[0] >= self.quantidade_vendida:
            total = produto[1] * self.quantidade_vendida
            data_venda = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('''
            INSERT INTO Vendas (id_produto, quantidade_vendida, data_venda, id_funcionario)
            VALUES (?, ?, ?, ?)''', (self.id_produto, self.quantidade_vendida, data_venda, self.id_funcionario))

            nova_quantidade = produto[0] - self.quantidade_vendida
            cursor.execute("UPDATE Produtos SET quantidade_em_estoque = ? WHERE id_produto = ?", 
                           (nova_quantidade, self.id_produto))

            if self.id_funcionario:
                cursor.execute("UPDATE Funcionarios SET saldo_a_pagar = saldo_a_pagar + ? WHERE id_funcionario = ?", 
                               (total, self.id_funcionario))
            conn.commit()
            print(f"Venda realizada com sucesso! Total: R$ {total:.2f}")
        else:
            print("Estoque insuficiente ou produto não encontrado.")
        conn.close()
