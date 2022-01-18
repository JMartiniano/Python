n = int(input())
a = [x for x in input().split()]
for x in range (len(a)):
    saida = 1
    for k in range(len(a)):
        a[k] = int(a[k])
        saida *= a[k]

print(saida)