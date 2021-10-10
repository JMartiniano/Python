'''
Pilhas tem o mesmo conceito que Fila, sendo que o primeiro a entrar é o ultimo a sair
Para criar Pilhas é do mesmo jeito que faz Filas, usa o mesmo conceito pra tudo
'''
class Pilha(object):
    def __init__(self):
        self.dados = ['Amarelo', 'Vermelho', 'Verde', 'Azul']
    def getPilha(self):
        return self.dados
    def inserirDados(self, novoElemento):
        self.dados.append(novoElemento)
    def removerDado(self):
        self.dados.pop()
    def topo(self):
        return (self.dados[len(self.dados) - 1]) # aqui pegou o tamnho da lista e subitraiu 1 para achar o índice do topo (ultimo elemento)
    def esvaziar(self):
        while (len(self.dados) != 0):
            self.dados.pop()