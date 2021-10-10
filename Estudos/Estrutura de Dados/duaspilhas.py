class Pilha(object):
    def __init__(self):
        self.dados = []
    def inserirDaddos(self, novoDado):
        self.dados.append(novoDado)
    def getPilha(self):
        return self.dados
    def tamanho(self):
        return (len(self.dados))
    def comparandoElementos(self):
        elementos = []
        for x in range(len(self.dados)):
            dado = self.dados[x]
            elementos.append(dado)
        return elementos