p, r = input().split()
p, r  = int(p), int(r)

if ( (p/2) == r ):
    print ('Nivel 1')
elif ( (p/1.5) == r ):
    print ('Nivel 2')
else:
    print ('Nivel 3')