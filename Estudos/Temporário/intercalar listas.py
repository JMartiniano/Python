l1 = []
l2 = []

def inter (a,b):
    l3 = []
    tamA = len(a)
    tamB = len(b)
    for x in range (tamA):
        l3.insert(x, a[x])
    for x in range (tamB):
        l3.insert(x + x, b[x])
    return l3

print ('=' * 50)
tamL1 = int(input(f'Tamanho de L1:'))
tamL2 = int(input(f'Tamanho de L2: '))
print ('=' * 50)

print ('Lista 1')
for x in range (tamL1):
    num = int(input(f'Número[{x}]: '))
    l1.append(num)
print ('=' * 50)
print ('Lista 2')
for x in range (tamL2):
    num = int(input(f'Número[{x}]: '))
    l2.append(num)

atri = inter(l1, l2)

print ('=' * 50)
print ('Intercalada: ')
print (f'Lista 3: {atri}')
print ('=' * 50)