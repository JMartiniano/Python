class Pilha(object):
    def __init__(self):
        self.estados = []
    def inserirDados(self,novoDado):
        self.estados.append(novoDado)
    def getPilha(self):
        return self.estados