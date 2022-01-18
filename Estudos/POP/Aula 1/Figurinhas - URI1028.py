def mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a
casos = int(input())
for x in range(casos):
    ricardo, vicente = input().split()
    ricardo, vicente = int(ricardo), int(vicente)
    print(mdc(ricardo, vicente))

#entregue dia 15/10/19




