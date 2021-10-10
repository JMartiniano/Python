node.py


class No(object):
    def __init__(self):
        self.valor = None
        self.proximo = None

    def getValor(self):
        return self.valor

    def getProximo(self):
        return self.proximo

    def setValor(self, valor):
        self.valor = valor

    def setProximo(self, prox):
        self.proximo = prox
