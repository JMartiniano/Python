n, m = input().split()
n, m = int(n), int(m)

cont = 0
for y in range(n):
    z = input().split()
    if not '0' in z:
        cont += 1
print(cont)