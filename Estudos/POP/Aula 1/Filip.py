a, b = input().split()
ia = a[::-1]
ib = b[::-1]
a, b = int(ia), int(ib)
if a > b:
    print(a)
else:
    print(b)