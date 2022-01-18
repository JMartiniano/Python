class Arvore():
    def __init__(self, c, d = None, e = None):
        self.chave = c
        self.direita = d
        self.esquerda = e

#inserindo valores:

raiz = int(input('Raiz: '))
arvore = Arvore(raiz)

esc = input('Press A to add a new number\nPress E to exit\n--> ')
while esc is not 3:
    if esc == 'A' or esc == 'a':
        chave = int(input('New number: '))
        def inserir(no, chave):
            if no is None:
                no = Arvore(chave)
            else:
                if chave < no.chave:
                    no.esquerda = inserir(no.esquerda, chave)
                else:
                    no.direita = inserir(no.direita, chave)
            return no
        esc = input('Press A to add a new number\nPress E to exit\n--> ')
    else:
        esc = 3
        print('ENCERRADO!')
