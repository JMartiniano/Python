import crescente
pilhaTeste = crescente.Pilha()

print('~' *50)
print ('Situação da sua Pilha S')
print(pilhaTeste.getPilha())
print('~' *50)
escolha = input('Add elementos? [Y/N]')
while ( escolha == 'y' ) or ( escolha == 'Y' ):
    while (escolha == 'Y') or ( escolha == 'y' ):
        add = input('E - sair\nDigite o novo elemento:')
        if (add != 'E') and (add != 'e'):
            add = int(add)
            pilhaTeste.inserir(add)
            print('~' * 50)
            print(f'Situação atual da Pilha S:\n{pilhaTeste.getPilha()}')
            print('~' * 50)
        else:
            escolha = 'N'
else:
    print('~' * 50)
    print('PILHA ENCERRADA')
    print('~' * 50)

print ('Organizando a sua Pilha S...')
print(f'Sua Pilha S em ordem crescente: {pilhaTeste.crescente()}')
print('~'*50)