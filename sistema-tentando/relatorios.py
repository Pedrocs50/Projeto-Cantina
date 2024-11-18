'''PARA GERAR OS RELATÓRIOS EM EXCEL'''

import pandas as pd
from banco import BancoDeDados

class GeradorRelatorio:
    @staticmethod
    def gerar_relatorio_vendas():
        banco = BancoDeDados()
        conn = banco.conectar()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT Vendas.id_venda, Produtos.nome, Vendas.quantidade_vendida, Vendas.data_venda, Funcionarios.nome
        FROM Vendas
        LEFT JOIN Produtos ON Vendas.id_produto = Produtos.id_produto
        LEFT JOIN Funcionarios ON Vendas.id_funcionario = Funcionarios.id_funcionario''')
        vendas = cursor.fetchall()
        conn.close()

        df = pd.DataFrame(vendas, columns=["ID Venda", "Produto", "Quantidade", "Data", "Funcionário"])
        df.to_excel("relatorio_vendas.xlsx", index=False)
        print("Relatório de vendas gerado com sucesso: 'relatorio_vendas.xlsx'")
