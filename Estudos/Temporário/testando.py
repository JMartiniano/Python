def primos (a):
    if (a == 0) or (a == 1):
        return True
    elif (a == 2):
        return  False
    elif (a > 2):
        for k in range (2, a):
            if ( a%k == 0):
                return False
            if ( a%k != 0 ) or ( k == a-1 ):
                return True

verdade = []
falso = []
todos = []

print ('BEM VINDO À CALCULADORA DE NÚMEROS PRIMOS\nEscolha uma opção para começar:')
print ('1 - Digitar um valor\n2 - Digitar um intervalo')
op = int(input('Opção: '))
print ('=' * 50)

if op == 1:
    print ('Você escolheu a opção 1')
    num = int(input('Valor: '))
    atri = primos(num)
    if atri == True:
        atri = 'é primo'
    else:
        atri = 'não é primo'
    print (f'{num} {atri}')
    print('=' * 50)
else:
    print('Você escolheu a opção 2')
    comeco = int(input('Começo do intervalo: '))
    fim = int(input('Fim do intervalo: '))
    print('=' * 50)
    print ('Seus resultados:')
    for k in range (comeco, fim + 1):
        atri = primos(k)
        todos.append(k)
        if k == comeco:
            menor = k
            maior = k
        elif k > maior:
            maior = k
        elif k < menor:
            menor = k
        if atri == True:
            verdade.append(k)
            atri = 'é primo'
        if atri == False:
            falso.append(k)
            atri = 'não é primo'
        print (f'{k} {atri}')

    for x in verdade:
        if x == verdade[0]:
            menorT = x
            maiorT = x
        elif x > maiorT:
            maiorT = x
        elif x < menorT:
            menorT = x
    for y in falso:
        if y == falso[0]:
            menorF = y
            maiorF = y
        elif y > maiorF:
            maiorF = y
        elif y < menorF:
            menorF = x

    tamV = len(verdade)
    tamF = len(falso)
    tamT = len(todos)

    print('=' * 50)
    print ('Dados extras:')
    print (f'De todos os números verificasdos: ')
    print (f'Menor: {menor}\nMaior: {maior}')
    print (f'Quantidade: {tamT}')
    print('=' * 50)
    print ('Dos primos:')
    print (f'Menor: {menorT}\nMaior: {maiorT}')
    print (f'Quantidade: {tamV}')
    print ('São eles:', end = ' ')
    print(verdade)
    print('=' * 50)
    print ('Dos não primos:')
    print (f'Menor: {menorF}\nMaior: {maiorF}')
    print(f'Quantidade: {tamF}')
    print ('São eles:', end = ' ')
    print (falso)
    print('=' * 50)
    print ('ENCERRADO')

    for x in verdade:
        v = str(verdade)
        arquivo = open('Primos.txt', 'w')
        arquivo.write(v)
        arquivo.close()
    for x in falso:
        f = str(falso)
        arquivo = open('Não Primos.txt', 'w')
        arquivo.write(f)
        arquivo.close()

