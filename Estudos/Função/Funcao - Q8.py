
def potencia (a):
    pot = a ** 2
    return pot

num = int(input('Numero elevado a 2: '))

fats = potencia(num)
print(f'{num} ao quadrado é {fats}')

for x in range (1, 11):
    fats = potencia(x)
    print (f'{x} ao quadrado é {fats}')

