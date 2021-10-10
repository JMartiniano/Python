def primos (a):
    if ( a == 1 ) or ( a == 0 ):
        return True
    elif ( a == 2 ):
        return False
    elif ( a > 2 ):
        for k in range(2, a):
            if ( a%k == 0):
                return False
            elif ( a%k != 0 ) and ( k == a-1 ):
                return True

num = int(input(f'Número: '))

atribuidor = primos(num)

print(f'{num} é primo: {atribuidor}')

deci = input('Deseja verificar algum intervalo[Y or N]: ')

if ( deci == 'Y' ) or (deci == 'y'):
    inicio = int(input('Incício do intervalo: '))
    fim = int(input('Fim do intervalo: '))

    for x in range( inicio, fim+1):
        num = x
        atribuidor = primos(num)
        print (f'{num} é primo: {atribuidor}')
    print ('ENCERRADO')
else:
    print ('ENCERRADO')