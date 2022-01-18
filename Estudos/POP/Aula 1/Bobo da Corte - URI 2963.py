n  = int(input())

votos = []
for x in range(n):
    z = int(input())
    votos.append(z)

for i in range(len(votos)):
    if (i == 0):
        maior = votos[i]
    elif( votos[i] > maior):
        maior = votos[i]

if ( maior == votos[0]):
    print('S')
else:
    print('N')
