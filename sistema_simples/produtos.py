from banco import BancoDeDados

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.banco = BancoDeDados()

    def adicionar_produto(self):
        """Método para adicionar um produto no banco de dados."""
        conn = self.banco.conectar()
        cursor = conn.cursor()

        # Inserir dados na tabela Produtos
        cursor.execute('''
        INSERT INTO Produtos (nome, preco, quantidade_em_estoque)
        VALUES (?, ?, ?)''', (self.nome, self.preco, self.quantidade))

        conn.commit()
        self.banco.fechar_conexao(conn)
        print(f"Produto '{self.nome}' adicionado com sucesso!")

    @staticmethod
    def listar_produtos():
        """Método estático para listar todos os produtos do banco de dados."""
        banco = BancoDeDados()
        conn = banco.conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT id_produto, nome, preco, quantidade_em_estoque FROM Produtos")
        produtos = cursor.fetchall()

        if produtos:
            print("ID | Nome | Preço | Estoque")
            print("-" * 40)
            for produto in produtos:
                print(f"{produto[0]} | {produto[1]} | R$ {produto[2]:.2f} | {produto[3]}")
        else:
            print("Nenhum produto cadastrado.")
        
        banco.fechar_conexao(conn)

    @staticmethod
    def remover_produto(id_produto):
        """Método estático para remover um produto do banco de dados."""
        banco = BancoDeDados()
        conn = banco.conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Produtos WHERE id_produto = ?", (id_produto,))
        produto = cursor.fetchone()

        if produto:
            cursor.execute("DELETE FROM Produtos WHERE id_produto = ?", (id_produto,))
            conn.commit()
            print(f"Produto com ID {id_produto} foi removido com sucesso.")
        else:
            print(f"Produto com ID {id_produto} não encontrado.")

        banco.fechar_conexao(conn)
