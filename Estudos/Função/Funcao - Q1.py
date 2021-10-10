def cubo (a):
    res = a**3
    return res
num = int(input(f"Número: "))
atribuidor = cubo (num)
print (f"O cubo de {num} é {atribuidor}")