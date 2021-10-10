n = int(input())
r = [x for x in input().split()]
tam = len(r)
maior = 0

for x in range (tam):
    r[x] = int(r[x])
    if ( x == 0 ):
        maior = r[x]
    else:
        if r[x] > maior:
            maior = r[x]

area = 3 * (maior ** 2)
#print(maior)
print (area)


