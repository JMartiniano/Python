v, p = input().split()
v, p = int(v), int(p)

if ( v%p == 0 ):
    print (v//p)
elif ( v%p != 0):
    pagar = v//p
    total = (pagar + 1) * p
    sobra = total - v
    print(pagar + 1)
    print(f"SOBRA {sobra}")




'''
pagar = v/p
if (pagar%p != 0 ):
    total = pagar * p
    print(total - v)
elif ( pagar%p == 0):
    print(pagar)
'''

