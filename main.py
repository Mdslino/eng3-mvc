from view.View import MainView
from model.Inventory import Inventory
from model.Produto import Produto

inventory = Inventory()
app = MainView()


def popular_produtos():
    produtos = [
        Produto('Banana', 3.75, 25),
        Produto('Maçã', 1.70, 50),
        Produto('Uva', 6.80, 70),
        Produto('Mandioca', 2.25, 15)
    ]
    for produto in produtos:
        inventory.adicionar_produto(produto)


def run():
    app.selecionar_funcionario()
    app.acoes()


if __name__ == '__main__':
    popular_produtos()
    run()
