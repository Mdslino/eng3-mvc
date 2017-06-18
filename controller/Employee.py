class Employee:
    def buscar(self, nome):
        raise NotImplementedError()

    def adicionar(self, nome, preco, quantidade):
        raise NotImplementedError()

    def deletar(self, nome_produto):
        raise NotImplementedError()

    def modificar(self, nome_produto, *args, **kwargs):
        raise NotImplementedError()
