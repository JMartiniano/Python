class Arvore():
    def __init__(self, c, d = None, e = None):
       self.chave = c
       self.esquerda = e
       self.direita = d


######## Inserindo valores na Árvore ########

# --> Método 1
#arvore = Arvore(4, Arvore(6), Arvore(2))

# --> Método 2

n = input('Seu nome: ')
e = input('Curso: ')
d = input('Matrícula: ')
arvore = Arvore(n, Arvore(e), Arvore(d))


