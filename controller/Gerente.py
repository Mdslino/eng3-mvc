from .Employee import Employee
from model.Produto import Produto


class Gerente(Employee):
    def __init__(self, model):
        self.__model = model

    @property
    def model(self):
        return self.__model

    def buscar(self, nome):
        return self.model.procurar_produto(nome)

    def adicionar(self, nome, preco, quantidade):
        p = Produto(nome, preco, quantidade)
        self.model.adicionar_produto(p)

    def deletar(self, nome_produto):
        self.model.remover_produto(nome_produto)

    def modificar(self, nome_produto, *args, **kwargs):
        self.model.modificar_produto(nome_produto, **kwargs)

    def listar(self):
        produtos = self.__model.produtos
        return produtos

    def vender(self, nome_produto, quantidade):
        q = self.buscar(nome_produto)
        q = q[0]['quantidade'] - quantidade
        self.model.modificar_produto(nome_produto, quantidade=q)
