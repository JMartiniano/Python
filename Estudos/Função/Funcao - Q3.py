def fatorial (a):
    f = a * (a - 1)
    for k in range (2, a-1):
        f = f * (a - k)
    return f

num = int(input('Número: '))

atribuidor = fatorial(num)

print (f'{num} fatorado é {atribuidor}')