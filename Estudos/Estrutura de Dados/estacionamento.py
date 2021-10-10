class Fila(object):
    def __init__(self):
        self.dados = []
    def getFila(self):
        return self.dados
    def inserir(self, valor):
        self.dados.append(valor)
    def posicao(self,elemento):
        self.pos = self.dados.index(elemento)
    def remover(self, elemento):
        pos = self.dados.index(elemento)
        for x in range (0, pos+1):
            self.dados.pop(0)
    def tamanho(self):
        return len(self.dados)
    def rotacao(self, pos):
        self.saiu = []
        for x in range (0, self.pos+1):
            self.saiu.append(self.dados[x])
        for y in range (0, self.pos):
            self.dados.append(self.saiu[y])