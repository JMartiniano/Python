class No():

    def __index__(self):
        self.valor = None
        self.proximo = None

    def getValor(self):
        return self.valor
    def getProximo(self):
        return self.proximo

    def setValor(self, novoValor):
        self.valor = novoValor
    def setProximo(self, proximo):
        self.proximo = proximo
