'''MENU'''

from produtos import Produto
from funcionarios import Funcionario
from vendas import Venda
from relatorios import GeradorRelatorio
from banco import BancoDeDados

def main():
    banco = BancoDeDados()
    banco.criar_tabelas()

    while True:
        print("\nMenu:")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Listar Produtos")
        print("4. Adicionar Funcionário")
        print("5. Listar Funcionários")
        print("6. Vender Produto")
        print("7. Gerar Relatório de Vendas")
        print("8. Sair")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            produto = Produto(nome, preco, quantidade)
            produto.salvar()
        
        elif opcao == 2:
            produtos = Produto.listar_produtos()
            for p in produtos:
                print(f"{p[0]} - {p[1]} (R$ {p[2]:.2f} - Estoque: {p[3]})")
            id_produto = int(input("ID do produto para remover: "))
            Produto("", 0, 0).remover(id_produto)
        
        elif opcao == 3:
            produtos = Produto.listar_produtos()
            if produtos:
                print("\nProdutos Disponíveis:")
                for p in produtos:
                    print(f"{p[0]} - {p[1]} (R$ {p[2]:.2f} - Estoque: {p[3]})")
            else:
                print("Nenhum produto cadastrado.")
        
        elif opcao == 4:
            nome = input("Nome do funcionário: ")
            funcionario = Funcionario(nome)
            funcionario.salvar()
        
        elif opcao == 5:
            funcionarios = Funcionario.listar_funcionarios()
            if funcionarios:
                print("\nFuncionários Cadastrados:")
                for f in funcionarios:
                    print(f"{f[0]} - {f[1]} (Saldo a pagar: R$ {f[2]:.2f})")
            else:
                print("Nenhum funcionário cadastrado.")
        
        elif opcao == 6:
            produtos = Produto.listar_produtos()
            if produtos:
                print("\nProdutos Disponíveis:")
                for p in produtos:
                    print(f"{p[0]} - {p[1]} (R$ {p[2]:.2f} - Estoque: {p[3]})")
                id_produto = int(input("ID do produto: "))
                quantidade = int(input("Quantidade: "))
                print("\nVenda para:")
                print("1. Cliente Comum")
                print("2. Funcionário")
                tipo = int(input("Escolha: "))
                if tipo == 1:
                    venda = Venda(id_produto, quantidade)
                elif tipo == 2:
                    funcionarios = Funcionario.listar_funcionarios()
                    for f in funcionarios:
                        print(f"{f[0]} - {f[1]}")
                    id_funcionario = int(input("ID do funcionário: "))
                    venda = Venda(id_produto, quantidade, id_funcionario)
                else:
                    print("Opção inválida. Cancelando venda.")
                    continue
                venda.realizar_venda()
            else:
                print("Nenhum produto disponível para venda.")
        
        elif opcao == 7:
            GeradorRelatorio.gerar_relatorio_vendas()
        
        elif opcao == 8:
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

