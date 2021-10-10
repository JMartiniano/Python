arq = open ('Cad.txt', 'w')

print ('1° cadastro:')
n = input('Nome: ')
s = input('Sexo: ')
i = input('Idade: ')
arq.write(n + ',' + s + ',' + i + '\n')
print ('2° cadastro:')
n = input('Nome: ')
arq.write(n)
cont = 2
while ( n != '' ):
    cont += 1
    s = input('Sexo: ')
    i = input('Idade: ')
    arq.write(',' + s + ',' + i + '\n')
    print (f'{cont}° cadastro:')
    n = input('Nome: ')
    arq.write(n)
arq.close()