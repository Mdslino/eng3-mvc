from .Produto import Produto


class Singleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]


class Inventory(metaclass=Singleton):
    def __init__(self):
        self.__produtos = []

    @property
    def produtos(self):
        return self.__produtos

    @produtos.setter
    def produtos(self, produto):
        self.adicionar_produto(produto)

    def adicionar_produto(self, produto):
        if isinstance(produto, Produto):
            self.produtos.append({
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
        return encontrados

    def remover_produto(self, nome_produto):
        for p in self.produtos:
            if p['nome'] == nome_produto:
                self.produtos.remove(p)

    def modificar_produto(self, nome_produto, **kwargs):
        print('Preço passado no parametro: {}'.format(kwargs.get('preco')))
        print('Quantidade passado no parametro: {}'.format(kwargs.get('quantidade')))
        for produto in self.produtos:
            for value in produto.values():
                if value == nome_produto:
                    if kwargs.get('preco'):
                        produto['preco'] = kwargs.get('preco')
                    if kwargs.get('quantidade'):
                        produto['quantidade'] = kwargs.get('quantidade')
