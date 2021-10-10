class Pilha(object):
    def __init__(self):
        self.S = []
    def inserir(self, valor):
        self.S.append(valor)
    def getPilha(self):
        return self.S
    def crescente(self):
        tam = len(self.S)
        aux = []
        for x in range(tam):
            self.S[x] = int(self.S[x])
            if ( x == 0 ):
                maior = self.S[x]
            else:
                if ( self.S[x] > maior):
                    aux.append(self.S[x])
        return aux