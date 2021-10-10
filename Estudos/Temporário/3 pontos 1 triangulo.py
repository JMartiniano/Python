p1 = int(input('Informe o Ponto 1: '))
p2 = int(input('Informe o Ponto 2: '))
p3 = int(input('Informe o Ponto 3: '))

if ( p1 < (p2 + p3)):
    if (p2 > p3):
        if ( p1 > (p2 - p3)):
            print (f'{p1, p2, p3} formam um triangulo')
        else:
            print (f'{p1, p2, p3} não formam um triangulo')
    elif (p3 > p2):
        if ( p1 > (p3 - p2)):
            print (f'{p1, p2, p3} formam um triangulo')
        else:
            print(f'{p1, p2, p3} não formam um triangulo')
    print(f'{p1, p2, p3} não formam um triangulo')
else:
    print (f'{p1, p2, p3} não formam um triangulo')