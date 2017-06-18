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
            table.add_row([produto['nome'], produto['preco'], produto['quantidade']])
        print(table)

    def adcionar_produto(self):
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
            table.add_row([produto['nome'], produto['preco'], produto['quantidade']])
        print(table)

