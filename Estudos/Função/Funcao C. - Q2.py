def maior (a):
    for x in range((len(a))):
        if x == 0:
            m = a[x]
        else:
            if ( a[x] > m):
                m = a[x]
    return m

tam = int(input('Tamanho do seu Vetor: '))

vet = []
for x in range(tam):
    valor = int(input(f'Valor [{x}]: '))
    vet.append(valor)

atribuidor = maior(vet)
print(f'O maior elemento de {vet} é {atribuidor}')


