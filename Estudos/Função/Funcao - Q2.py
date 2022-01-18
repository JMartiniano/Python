def menor (a, b, c):
    if (a < b) and ( a < c):
        res = a
    elif (b < a) and (b < c):
        res = b
    else:
        res = c
    return res

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

atribuidor = menor (n1, n2, n3)

print (f'O menor número é {atribuidor}')