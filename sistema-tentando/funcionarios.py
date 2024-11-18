'''OPERAÇÕES RELACIONADAS AOS FUNCIONÁRIOS'''

from banco import BancoDeDados
from entidades import Entidade

class Funcionario(Entidade):
    def __init__(self, nome):
        self.nome = nome
        self.banco = BancoDeDados()

    def salvar(self):
        conn = self.banco.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Funcionarios (nome) VALUES (?)", (self.nome,))
        conn.commit()
        conn.close()
        print(f"Funcionário '{self.nome}' adicionado com sucesso!")

    @staticmethod
    def listar_funcionarios():
        banco = BancoDeDados()
        conn = banco.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id_funcionario, nome, saldo_a_pagar FROM Funcionarios")
        funcionarios = cursor.fetchall()
        conn.close()
        return funcionarios

    def remover(self, id_funcionario):
        conn = self.banco.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Funcionarios WHERE id_funcionario = ?", (id_funcionario,))
        conn.commit()
        conn.close()
        print(f"Funcionário com ID {id_funcionario} foi removido.")
