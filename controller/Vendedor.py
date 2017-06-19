from .Employee import Employee


class Vendedor(Employee):
    def __init__(self, model):
        self.__model = model

    @property
    def model(self):
        return self.__model

    def buscar(self, nome):
        return self.model.procurar_produto(nome)

    def adicionar(self, nome, preco, quantidade):
        raise PermissionError("Vendedor não pode adicionar itens ao estoque")

    def deletar(self, nome_produto):
        raise PermissionError("Vendedor não pode deletar itens do estoque")

    def modificar(self, nome_produto, *args, **kwargs):
        raise PermissionError("Vendedor não pode modificar itens do estoque")

    def listar(self):
        produtos = self.model.produtos
        return produtos

    def vender(self, nome_produto, quantidade):
        q = self.buscar(nome_produto)
        q = q[0]['quantidade'] - quantidade
        self.model.modificar_produto(nome_produto, quantidade=q)
