def soma (a):
    sum = 0
    for x in range ((len(a))):
        vetor = a[x]
        vetor = int(vetor)
        sum += vetor
    return sum

vet = [6,3,8,7,2,5]

atribuidor = soma(vet)
print (f'A:{vet}')
print(f'Soma de A: {atribuidor}')

decisao = input('Deseja adicionar um Vetor B? [Y or N]: ')

if decisao == 'Y':
    B =[]
    print ('Beleza, vamos criar seu Vetor B!\nMas antes, por favor:')
    tam = int(input('Informe o tamanho do Vetor:'))
    for x in range (tam):
        valor = int(input(f'Valor [{x}]: '))
        B.append(valor)

    atribuidor = soma(B)
    print(f'Seu Vetor B:{B}')
    print(f'Soma de B: {atribuidor}')