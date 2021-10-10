def par (a):
    if ( a%2 == 0 ):
        res = True
    else:
        res = False
    return res

num = int(input('Número: '))

while num != 0:
    num = int(input('Número: '))

atribuidor = par(num)
print (atribuidor)