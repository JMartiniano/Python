a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

tres = (a + b + c)
maior = a
menores = b + c
if ( b > maior):
    maior = b
    menores = a + c
if ( c > maior):
    maior = c
    menores = a + b
if (a == b) or ( a == c) or ( b == c):
    print('S')
elif ( (maior - menores) == 0):
    print('S')
else:
    print('N')