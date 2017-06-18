from .Employee import Employee
from model.Produto import Produto


class Vendedor(Employee):
    def __init__(self, view, model):
        self.__view = view()
        self.__model = model()

    def buscar(self):
        listaProdutos = self.__model.produto
        self.view.listaProdutos(listaProdutos)

    def listar(self):
        return self.__model.produto

    def vender(self, nome, quantidade):
        self.buscar()
