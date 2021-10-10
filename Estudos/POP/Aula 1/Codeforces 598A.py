numeros = int(input())
for i in range(numeros):
    n = int(input())
    for x in range(1,n+1):
        if x%2 == 0:
            res = x - n-x
        else:
            res = x + n-x
    print(res)

#ENTREGUE