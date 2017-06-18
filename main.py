from view.View import MainView

app = MainView()

def run():
    app.selecionar_funcionario()
    app.acoes()

if __name__ == '__main__':
    run()