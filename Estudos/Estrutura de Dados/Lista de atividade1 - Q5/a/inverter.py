#inverter usando Pilhas adicionais

class Pilha(object):
    def __init__(self):
        self.S = []
    def inserir(self, novo):
        self.S.append(novo)
    def getPilha(self):
        return self.S
    def inverter(self):
        tam = (len(self.S))
        invertido = []
        for x in range (tam):
            invertido.insert(0, self.S[x])
        return invertido

#COMO EU SEI QUE ISSO FOI INVERTIDO POR FILA OU PILHA SE A UNICA DIEFERENÇA É NA HORA DE TIRAR?