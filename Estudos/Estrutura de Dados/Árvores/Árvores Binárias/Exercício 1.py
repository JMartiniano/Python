#Inserir os númeoros menores que o Nó à esquerda e maior à direita. Os valores são: 2,4,6,8,5,7,0 raiz 13
class Arvore():
    def __init__(self, c, d = None, e = None):
        self.chave = c
        self.direita = d
        self.esquerda = e

def inserir(no, chave):
    xif no is None:
        no = Arvore(chave)
    else:
        if chave < no.chave:
            no.esquerda = inserir(no.esquerda, chave)
        else:
            no.direita = inserir(no.direita, chave)
    return no

no = int(input('Raiz: '))

arvore = Arvore(no)

for i in range(5):
    chave = int(input('Valor: '))
    arvore = inserir(arvore, chave)

############### BUSCANDO ELEMENTOS NA ÁRVORE ##############

# METODO 1 - BUSCA LINEAR
'''
busca = int(input('Busca: '))

def buscaLinear(no, chave):
    while no is not None:
        if no.chave == chave:
            return no
        elif chave > no.chave:
            no = no.direita
        else:
            no = no.esquerda
    return None

if buscaLinear(arvore, busca) is not None:
    print (f'Valor {busca} encontrado!')
else:
    print (f'Valor {busca} não encontrado!')
'''
################ CALCULANDO ALTURA DA ÁRVORE ###############

'''
A altura da árvore é definida pelo maior caminho desde a raiz até a folha.
O grau de uma Árvore é difinido pelo número de sub-arvores que saem do nó.
Uma arvore binária só pode ter grau 2
'''

def maximo(a, b): #descobrindo quem é a maior subarvore, essa função vai ser chamada na proxima
    if a > b:
        return a
    return b

def altura(no): #vai percorrer a estrutura e ver o grau dos nós até que seja None
    if no is None:
        return 0
    return 1 + maximo(altura(no.esquerda), altura(no.direita)) #analiso cada subarvore pegando a altura de cada uma com a função maximo e soma 1 pra dar o calculo certo
#no final das arvores vai retornar 0, aí a função maximo vai retornar a maior altura,, somar 1 com ela e vai ficar 1 e o 0 que retornou, vai ver quem é o maior deles e somar com 1.

print (f'Altura: {altura(arvore)}')

#################### MOSTRANDO UMA ARVORE #################
'''
É OBRIGADO A USAR UM DOS TRES MÉTODOS POSSÍVEIS:
'''
#PRE ORDEM:
imprimeArvore = ''
def preOrdem(no):
    global imprimeArvore
    if no is None:
        return
    imprimeArvore += str(no.chave) + ', '
    preOrdem(no.esquerda)
    preOrdem(no.direita)

preOrdem(arvore)
print(f'Pré Ordem: {imprimeArvore}')

'''
#EM ORDEM:
imprimeArvore = ''
def preOrdem(no):
    global ImprimeArvore
    if no is None:
        return
    preOrdem(no.esquerda)
    imprimeArvore += str(no.chave) + ', '
    preOrdem(no.direita)

#POS ORDEM:
imprimeArvore = ''
def preOrdem(no):
    global ImprimeArvore
    if no is None:
        return
    preOrdem(no.esquerda)
    preOrdem(no.direita)
    imprimeArvore += str(no.chave) + ', '
'''

