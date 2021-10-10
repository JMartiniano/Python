def media (a, b, c):
    soma = a + b + c
    mediafinal = soma / 3
    return  mediafinal
n1 = int(input('Nota 1: '))
n2 = int(input('Nota 2: '))
n3 = int(input('Nota 3: '))

m = media(n1, n2, n3)

def conceito (a):
    if (m >= 80):
        conc = 'A'
    elif ( m >= 50) and (m < 80):
        conc = 'B'
    else:
        conc = 'C'
    return conc

c = conceito(m)

print (f'Media: {m}')
print (f'Conceito: {c}')
