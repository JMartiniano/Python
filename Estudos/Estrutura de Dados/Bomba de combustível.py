print ('Menu')
op = int(input('1 - Preços\n2 - Configurar\n'))
pgas = 0
peta = 0
pdie = 0

if ( op == 1 ):
    print (f'Preços:\nGasolina R$:{pgas}\nEtanol R$:{peta}\nDiesel R$:{pdie}')
    op3 = int(input('Escolha um combustível:\n1 - Gasolina\n2 - Etanol\n3 - Diesel\n4 - Voltar\n'))
    if ( op3 == 1 ):
        print (f'Você escolheu Gasolina\nPreço: R$:{pgas}')
        tanto= float(input('Quanto deseja: '))
        cont = 0
        litrostotal = tanto / pgas
        litros = 0
        while cont <= tanto - pgas:
            cont += pgas
            litros = cont / pgas
            print(f'Litros: {litros} Total R$: {cont}')
            op = int(input('1 - Preços\n2 - Configurar\n'))
    elif ( op3 == 2 ):
        print (f'Você escolheu Etanol\nPreço: R$:{peta}')
        tanto= float(input('Quanto deseja: '))
        cont = 0
        litrostotal = tanto / peta
        litros = 0
        while cont <= tanto - peta:
            cont += peta
            litros = cont / peta
            print(f'Litros: {litros} Total R$: {cont}')
            op = int(input('1 - Preços\n2 - Configurar\n'))
    elif ( op3 == 3 ):
        print (f'Você escolheu Diesel\nPreço: R$:{pdie}')
        tanto= float(input('Quanto deseja: '))
        cont = 0
        litrostotal = tanto / pdie
        litros = 0
        while cont <= tanto - pdie:
            cont += pdie
            litros = cont / pdie
            print(f'Litros: {litros} Total R$: {cont}')
    elif  ( op3 == 4 ):
        op = int(input('1 - Preços\n2 - Configurar\n'))

while ( op == 2 ):
    print ('Escolha um combustível para alterar o preço:')
    op2 = int(input('1 - Gasolina\n2 - Etanol\n3 - Diesel\n4 - Voltar\n'))
    if ( op2 == 1 ):
        p = float(input((f'Preço atual: R$:{pgas}\nNovo preço: R$:')))
        pgas = p
        op2 = 4
    elif ( op2 == 2 ):
        p = float(input(f'Preço atual: R$:{peta}\nNovo preço: R$:'))
        peta = p
        op2 = 4
    elif ( op2 == 3 ):
        p = float(input(f'Preço atual: R$:{pdie}\nNovo preço: R$:'))
        pdie = p
        op2 = 4
    elif ( op2 == 4):
        op = int(input('1 - Preços\n2 - Configurar\n'))