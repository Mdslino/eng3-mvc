class Subject:
    def __init__(self):
        self.__observers = []

    def registrar_observer(self, observer):
        if observer not in self.__observers:
            self.__observers.append(observer)

    def remover_observer(self, observer):
        try:
            self.__observers.remove(observer)
        except ValueError:
            pass

    def notificar_observer(self, modificador=None):
        for observer in self.__observers:
            if modificador != observer:
                observer.update(self)

    @property
    def observers(self):
        return self.__observers

    @observers.setter
    def observers(self, observer):
        self.registrar_observer(observer)
