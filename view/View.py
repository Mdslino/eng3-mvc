from controller.Vendedor import Vendedor
from model.Inventory import Inventory
from controller.Gerente import Gerente
from prettytable import PrettyTable


class GerenteView:
    def __init__(self):
        self.__gerente = Gerente(Inventory())

    @property
    def gerente(self):
        return self.__gerente

    def busca_produto(self):
        table = PrettyTable(['Nome', 'Preço', 'Quantidade'])
        nome_produto = input("Digite o nome do produto: ")
        produtos = self.gerente.buscar(nome_produto)
        for produto in produtos:
            table.add_row(
                [produto['nome'], produto['preco'], produto['quantidade']])
        print(table)

    def adicionar_produto(self):
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o valor do produto: "))
        quantidade = int(input("Digite a quantidade do produto"))
        self.gerente.adicionar(nome, preco, quantidade)
        print("{} adcionado com sucesso!!".format(nome))

    def deletar_produto(self):
        nome = input("Digite o nome do produto")
        self.gerente.deletar(nome)
        print("{} deletado com sucesso!!".format(nome))

    def modificar_produto(self):
        nome = input("Nome do produto: ")
        print("O que você gostaria de modificar?")
        print("1 - Preço")
        print("2 - Quantidade")
        print("3 - Ambos")
        options = {
            'opcao': self.gerente.modificar
        }
        opcao = int(input("Digite a opção: "))
        if opcao == 1:
            preco = float(input("Digite o preço: "))
            options['opcao'](nome, preco=preco)
            print("Preço modificado com sucesso!!")
        elif opcao == 2:
            quantidade = int(input("Digite a quantidade: "))
            options['opcao'](nome, quantidade=quantidade)
            print("Quantidade modificada com sucesso!!")
        elif opcao == 3:
            preco = float(input("Digite o preço: "))
            quantidade = int(input("Digite a quantidade: "))
            options['opcao'](nome, preco=preco, quantidade=quantidade)
            print("Preço e Quantidade de {} alterados com sucesso".format(nome))
        else:
            raise ValueError("Valor incorreto de opção")

    def listar_produtos(self):
        produtos = self.gerente.listar()
        table = PrettyTable(['Nome', 'Preço', 'Quantidade'])
        for produto in produtos:
            table.add_row(
                [produto['nome'], produto['preco'], produto['quantidade']])
        print(table)

    def vender_produto(self):
        table = PrettyTable(['Nome', 'Preço', 'Quantidade'])
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade vendida: "))
        produtos = self.gerente.buscar(nome)
        for produto in produtos:
            table.add_row(
                [produto['nome'], produto['preco'], produto['quantidade']])
        print(table)
        self.gerente.vender(nome, quantidade)
        print("\n\n")
        produtos = self.gerente.buscar(nome)
        for produto in produtos:
            table.add_row(
                [produto['nome'], produto['preco'], produto['quantidade']])
        print(table)


class VendedorView:
    def __init__(self):
        self.__vendedor = Vendedor(Inventory())

    @property
    def vendedor(self):
        return self.__vendedor

    def busca_produto(self):
        table = PrettyTable(['Nome', 'Preço', 'Quantidade'])
        nome_produto = input("Digite o nome do produto: ")
        produtos = self.vendedor.buscar(nome_produto)
        for produto in produtos:
            table.add_row(
                [produto['nome'], produto['preco'], produto['quantidade']])
        print(table)

    def listar_produtos(self):
        produtos = self.vendedor.listar()
        table = PrettyTable(['Nome', 'Preço', 'Quantidade'])
        for produto in produtos:
            table.add_row(
                [produto['nome'], produto['preco'], produto['quantidade']])
        print(table)

    def vender_produto(self):
        table = PrettyTable(['Nome', 'Preço', 'Quantidade'])
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade vendida: "))
        produtos = self.vendedor.buscar(nome)
        for produto in produtos:
            table.add_row(
                [produto['nome'], produto['preco'], produto['quantidade']])
        print(table)
        self.vendedor.vender(nome, quantidade)
        print("\n\n")
        produtos = self.vendedor.buscar(nome)
        for produto in produtos:
            table.add_row(
                [produto['nome'], produto['preco'], produto['quantidade']])
        print(table)


class MainView:
    def __init__(self):
        self.__funcionario = None

    @property
    def funcionario(self):
        return self.__funcionario

    @funcionario.setter
    def funcionario(self, tipo):
        self.__funcionario = tipo

    def selecionar_funcionario(self):
        tipos = {
            '1': GerenteView,
            '2': VendedorView
        }
        print('Qual seu cargo?')
        print('1 - Gerente')
        print('2 - Vendedor')
        opcao = int(input('Digite a opção: '))
        self.funcionario = tipos[str(opcao)]()

    def acoes(self):
        if isinstance(self.funcionario, GerenteView):
            tipos_acoes = {
                '1': self.funcionario.buscar_produto,
                '2': self.funcionario.adicionar_produto,
                '3': self.funcionario.deletar_produto,
                '4': self.funcionario.modificar_produto,
                '5': self.funcionario.listar_produtos,
                '6': self.funcionario.vender_produto,
                '7': self.selecionar_funcionario,
                '0': exit
            }

            print('O que gostaria de fazer?')
            print('1 - Buscar Produto')
            print('2 - Adicionar Produto')
            print('3 - Deletar Produto')
            print('4 - Modificar Produto')
            print('5 - Listar Produto')
            print('6 - Vender Produto')
            print('7 - Modificar Funcionário')
            print('0 - Sair')
            opcao = int(input('Digite a opção: '))
            tipos_acoes[str(opcao)]()
            self.acoes()

        elif isinstance(self.funcionario, VendedorView):
            tipos_acoes = {
                '1': self.funcionario.buscar_produto,
                '2': self.funcionario.listar_produtos,
                '3': self.funcionario.vender_produto,
                '4': self.selecionar_funcionario,
                '0': exit
            }

            print('O que gostaria de fazer?')
            print('1 - Buscar Produto')
            print('2 - Listar Produto')
            print('3 - Vender Produto')
            print('4 - Modificar funcionário')
            print('0 - Sair')
            opcao = int(input('Digite a opção: '))
            tipos_acoes[str(opcao)]()
            self.acoes()
