import estacionamento
filaTeste = estacionamento.Fila()

print ('=-' * 50)
print ('ESTACIONAMENTO')
print ('=-' * 50)

'''
escolha1 = input('Deseja abrir o estacionamento [y/n]: ')

if (escolha1 == 'y' or escolha1 == 'Y'):
    print('=-' * 50)
    print ('ESTACIONAMENTO ABERTO!\nVocê já pode começar a cadastrar os clientes.')
'''

escolha2 = int(input('Menu:\n1 - Cadastrar novo cliente\n2 - Ver situação do escionamento\n3 - Remover elemento\n4 - Fechar estacionamento\nSelecione:'))
while escolha2 == 1 or escolha2 == 2 or escolha2 ==3:
    while (escolha2 == 1):
        print('Digite 0 para sair')
        novo = input('Placa do cliente: ')
        if novo != 's' and novo != '0':
            filaTeste.inserir(novo)
        elif novo == 's':
            print(filaTeste.getFila())
        elif novo == '0':
            escolha2 = int(input('Menu:\n1 - Cadastrar novo cliente\n2 - Ver situação do escionamento\n3 - Remover elemento\n4 - Fechar estacionamento\nSelecione:'))
    while (escolha2 == 2):
        print('=-' * 50)
        print(f'Situação do estacionamento')
        print(filaTeste.getFila())
        sair = input('Digite E para sair\n')
        print('=-' * 50)
        if sair == 'E' or sair == 'e':
            escolha2 = int(input('Menu:\n1 - Cadastrar novo cliente\n2 - Ver situação do escionamento\n3 - Remover elemento\n4 - Fechar estacionamento\nSelecione:'))
    while (escolha2 == 3):
        if (filaTeste.tamanho() == 0):
            print ("Lista Vazia!")
            escolha2 = int(input('Menu:\n1 - Cadastrar novo cliente\n2 - Ver situação do escionamento\n3 - Remover elemento\n4 - Fechar estacionamento\nSelecione:'))
        else:
            d = input('Digite 0 para sair\nInforme a placa do carro que está saindo: ')
            p = filaTeste.posicao(d)
            filaTeste.rotacao(p)
            filaTeste.remover(d)
        sair = input('Digtite E para sair\n')
        if ( sair == 'e') or ( sair == 'E'):
            escolha2 = int(input('Menu:\n1 - Cadastrar novo cliente\n2 - Ver situação do escionamento\n3 - Remover elemento\n4 - Fechar estacionamento\nSelecione:'))

else:
    print('=-' * 50)
    print ('Estacionamento encerrado!')
    print('=-' * 50)