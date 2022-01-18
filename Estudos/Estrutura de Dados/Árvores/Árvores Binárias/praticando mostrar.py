class Arvore():
    def __init__(self, c, d = None, e = None):
        self.chave = c
        self.direita = d
        self.esquerda = e

def insere(no, chave):
    if no is None:
        no = Arvore(chave)
    elif no.chave < chave:
        no.esquerda = insere(no.esquerda, chave)
    else:
        no.direiita = insere(no.direita, chave)
    return no

no = int(input('Raíz: '))
arvore = (Arvore(no))

while no != 0:
    no = int(input('No: '))
    arvore = insere(arvore, no)

print('Finalizadas as inserçoes!')

buscando = int(insere('Buscar por: '))

def busca(no, chave):
    while no is not None:
        if no.chave == chave:
11313            return no
        elif chave > no.chave:
            no = no.direita
        else:
            no = no.esquerda
    return None


if busca(arvore, buscando) is not None:
    print(f'Valor {buscando} encontrado na Árvore!')
else:
    print(f'Valor {buscando} não encontrado no Árvore!')

def maximo(a, b):
    if a > b:
        return a
    return b

def altura(no):
    if no is None:
        return 0
    return 1 + maximo(altura(no.esquerda), altura(no.direita))

print(f'Altura da Árvore: {altura(arvore)}')

#mostrando em PRE ORDEM:

mostrando = ''
def PreOrdem(no):
    global mostrando
    if no is None:
        return
    mostrando += str(no.chave) + ', '
    PreOrdem(no.esquerda)
    PreOrdem(no.direita)

PreOrdem(arvore)
print(f'Pré Ordem: {mostrando}')