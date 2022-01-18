def edicao (a, b, c):
    pgas = a
    peta = b
    pdie = c
    return pgas, pdie, peta

def calcular (a, b):
    cont = 0
    litrostotal = a / b
    litros = 0
    while cont <= a - b:
        cont += b
        litros = cont / b
        print(f'Litros: {litros} Total R$: {cont}')


op = int(input('1 - Preços\n2 - Configurar\n'))
cont = 0

while ( op == 1 ):
        print (f'Preços:\nGasolina R$:{pgas}\nEtanol R$:{peta}\nDiesel R$:{pdie}')
        op3 = int(input('Escolha um combustível:\n1 - Gasolina\n2 - Etanol\n3 - Diesel\n4 - Voltar\n'))
        tanto = float(input('Quanto:'))
        if ( op3 == 1 ):
            atri = calcular(tanto, pgas)
        elif ( op3 == 2):
            atri = calcular(tanto, peta)
        elif ( p3 == 3 ):
            atri = calcular(tanto, pdie)

while ( op == 2 ):
    um = float(input('1 - Novo preço para Gasolina\n'))
    dois = float(input('2 - Novo preço para Etanol\n'))
    treis = float(input('3 - Novo preço para Diesel\n'))
    atri = edicao(um, dois, treis)
    op = int(input('1 - Preços\n2 - Configurar\n'))