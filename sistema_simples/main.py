from produtos import Produto
from vendas import Venda
from banco import BancoDeDados

def main():
    # Cria o banco de dados e as tabelas
    banco = BancoDeDados()
    banco.criar_tabelas()

    while True:
        print("\nMenu:")
        print("1. ADICIONAR PRODUTO")
        print("2. REMOVER PRODUTO")
        print("3. LISTAR PRODUTOS")
        print("4. VENDER PRODUTO")
        print("5. LISTAR VENDAS")
        print("6. SAIR")
        
        option = int(input("Opção: "))
        
        if option == 1:
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            produto = Produto(nome, preco, quantidade)
            produto.adicionar_produto()
            
        elif option == 2:
            Produto.listar_produtos()
            id_produto = int(input("ID do produto para remover: "))
            Produto.remover_produto(id_produto)
        
        elif option == 3:
            Produto.listar_produtos()
            
        elif option == 4:
            id_produto = int(input("ID do produto para vender: "))
            quantidade_vendida = int(input("Quantidade a vender: "))
            venda = Venda(id_produto, quantidade_vendida)
            venda.realizar_venda()
        
        elif option == 5:
            Venda.listar_vendas()
        
        elif option == 6:
            print("Saindo...")
            break

if __name__ == "__main__":
    main()
