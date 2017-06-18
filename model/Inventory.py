from .Subject import Subject
from .Produto import Produto


class Singleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]


class Inventory(Subject, metaclass=Singleton):
    def __init__(self):
        Subject.__init__(self)
        self.__produtos = []

    @property
    def produtos(self):
        return self.__produtos

    @produtos.setter
    def produtos(self, produto):
        self.adicionar_produto(produto)

    def adicionar_produto(self, produto):
        if isinstance(produto, Produto):
            self.__produtos.append({
                'nome': produto.nome,
                'preco': produto.preco,
                'quantidade': produto.quantidade
            })
        else:
            raise TypeError("Isso não é um produto")

    def procurar_produto(self, nome):
        encontrados = []
        for p in self.produtos:
            if p['nome'] == nome:
                encontrados.append(p)
        self.notificar_observer(encontrados)
        return encontrados

    def remover_produto(self, nome_produto):
        for p in self.produtos:
            if p['nome'] == nome_produto:
                self.__produtos.pop(p)

    def modificar_produto(self, nome_produto, **kwargs):
        options = {
            'preco': None,
            'quantidade': None
        }
        options.update(kwargs)
        if kwargs['preco']:
            for i in self.produtos:
                if i['nome'] == nome_produto:
                    i['preco'] = kwargs['preco']
        elif kwargs['quantidade']:
            for j in self.produtos:
                if j['nome'] == nome_produto:
                    j['quantidade'] = kwargs['quantidade']
