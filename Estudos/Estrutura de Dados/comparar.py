import duaspilhas

# criando variáveis

pilhaTeste = duaspilhas.Pilha()
pilhaTeste2 = duaspilhas.Pilha()

# add elementos

print ('Pilha 1')
escolha = input('Deseja inserir novo elemento? [Y/N]: ')
while escolha == 'Y' or escolha == 'y':
    ne = input('Novo elemnento: ')
    pilhaTeste.inserirDaddos(ne)
    print('=' * 50)
    print(f'Situação atual da Pilha 1: {pilhaTeste.getPilha()}')
    print('=' * 50)
    escolha = input('Deseja inserir novo elemento? [Y/N]: ')
else:
    print('PILHA 1 ENCERRADA')
    escolha2 = input('Deseja manipular a Pilha 2? [Y/N]: ')
    if escolha2 == 'Y' or escolha2 == 'y':
        escolha3 = input('Deseja inserir novo elemento? [Y/N]: ')
        while escolha3 == 'Y' or escolha3 == 'y':
            ne = input('Novo elemento: ')
            pilhaTeste2.inserirDaddos(ne)
            print('=' * 50)
            print(f'Situação atual da Pilha 2: {pilhaTeste2.getPilha()}')
            print('=' * 50)
            escolha3 = input('Deseja inserir novo elemento? [Y/N]')
        else:
            print('PILHA 2 ENCERRADA')
    elif escolha2 == 'n' or escolha2 == 'N':
        print('PILHA 2 ENCERRADA')

print('='*50)
print(f'Situação atual da Pilha 1: {pilhaTeste.getPilha()}\nSituação atual da Pilha 2: {pilhaTeste2.getPilha()}')
print('='*50)

#comparando as Pilhas 1 e 2

escolha4 = input("Deseja compara as Pilhas agora? [Y/N]")
if (escolha4 == "y") or (escolha4 == 'Y'):
    print ('Comparando as Pilhas 1 e 2')

    print (' - Tamanhos')
    print(f'Tamanho da Pilha 1: {pilhaTeste.tamanho()}')
    print (f'Tamanho da Pilha 2: {pilhaTeste2.tamanho()}')
    print('='*50)
    print(' - Elementos')
    print(f'Elementos da Pilha 1: {pilhaTeste.comparandoElementos()}')
    print(f'Elementos da Pilha 2: {pilhaTeste2.comparandoElementos()}')
    print('='*50)
    elemento1 = pilhaTeste.comparandoElementos()
    elemento2 = pilhaTeste2.comparandoElementos()
    tam1 = pilhaTeste.tamanho()
    tam2 = pilhaTeste2.tamanho()
    print(' - Comparando os elementos')
    if (tam1 == tam2):
        for x in range(tam1):
            if (elemento1[x] == elemento2[x]):
                print(f'Elementos do índice {x} são iguais!')
            else:
                print('Pilhas distintas')
        print('=' * 50)
        print (' - Resultado da comparação')
        print('Pilhas iguais!')
        print('=' * 50)
    else:
        print('=' * 50)
        print (' - Resultado da comparação')
        print ('Pilhas distintas')
        print('=' * 50)
else:
    print('ENCERRADO')