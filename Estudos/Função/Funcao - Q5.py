def primo (a):
    if (a == 1) or (a == 0):
        return False
    elif (a == 2):
        return True
    elif (a > 2):
        for k in range(2, a):
            if (a % k == 0):
                return False
            elif (a % k != 0) and (k == a-1):
                return True

num = (input('Número: '))

if num != '':
    num = int(num)
    atribuidor = primo(num)
    print (num, atribuidor)
else:
    print('ENCERRADO!')

cem = input('Deseja ver 0 - 100? [Y ou N]')

if cem == 'Y' or cem == 'y':
    for x in range(1, 101):
        atribuidor = primo(x)
        print (x, atribuidor)
    print('ENCERRADO!')
else:
    print('ENCERRADO!')