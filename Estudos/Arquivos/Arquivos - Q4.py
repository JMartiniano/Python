arqlido = input('Nome do arquivo: ')

arq = open (arqlido, 'r')

x = 0
print ('=' * 50)
arquivo = arq.readline()
while arquivo:
    x+=1
    print (f'{x} - ', arquivo, end = '')
    arquivo = arq.readline()
arq.close()
print ()
print ('=' * 50)