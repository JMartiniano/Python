'''def main ():
    nome = input('Seu nome: ')
    cidade = input('Sua cidade: ')
    return (f'Olá {nome}, você mora em {cidade}.')

print (main())
'''
'''
def media(a, b):
    return (a + b) / 2
def main():
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    return media(nota1, nota2)
print (f'Média = {main()}')
'''
'''
def salario(a, b):
    return (a * b) * 30
def main ():
    h = float(input('Horas de trabalho por dia: '))
    ch = float(input('Custo da hora de trabalho: '))
    return salario(h, ch)

print (f'Slário: {main()}')
'''

lista = []

for x in range (1,11):
    lista.append(x)
print(lista)

for i in range (len(lista)):
    maior = lista[0]
    if ( lista[i] > maior ):
        maior = lista[i]

print(maior)