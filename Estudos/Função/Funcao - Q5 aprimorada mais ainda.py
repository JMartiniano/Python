def primos (a):
    if ( a == 0 ) or ( a == 1 ):
        return True
    elif ( a == 2 ):
        return False
    elif ( a > 2 ):
        for k in range (2, a):
            if ( a%k == 0):
                return False
            if ( a%k != 0 ) or ( k == a-1 ):
                return True
print ('=' * 50)
print ('NÚMEROS PRIMOS')
print (f'Escolha uma opção')
choice = int(input('1 - Digitar um número\n2 - Digitar um intervalo\nOpção: '))
print ('=' * 50)
if (choice == 1):
    print('=' * 50)
    print ('Você escolheu a opção 1!')
    num = int(input('Número: '))
    atri = primos(num)
    print (f'{num} é primo? {atri}')
    print('=' * 50)
    print('ENCERRADO')
elif (choice == 2):
    print('=' * 50)
    print ('Você escolheu a opção 2!')
    comeco = int(input('Início do intervalo: '))
    fim = int(input('Fim do intervalo: '))
    for k in range (comeco, fim + 1):
        if k == comeco:
            menor = k
            maior = k
        elif k > maior:
            maior = k
        elif k < menor:
            menor = k
        atri = primos(k)
        print(f'{k} é primo? {atri}')
    print('=' * 50)
    print ('Menor e maior número verificado:')
    print (f'Menor: {menor}\nMaior: {maior}')
    print('=' * 50)
    print ('ENCERRADO')
