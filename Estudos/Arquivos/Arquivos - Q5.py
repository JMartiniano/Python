arq_lido = input('Nome do arquivo: ')

arq = open (arq_lido, 'r')

print ('=' * 50)
print (f'Arquivo {arq_lido}:')
linha = arq.readline()
while linha:
    print (linha, end = '')
    linha = arq.readline()
arq.close()
print ()

print ('=' * 50)

arq = open (arq_lido, 'a')
add = input('Adicionar: ')
arq.write(add)
arq.close()

arq = open (arq_lido, 'r')

print ('=' * 50)
print (f'{arq_lido} editado: ')

linha = arq.readline()
while linha:
    print (linha, end= '')
    linha = arq.readline()
arq.close()
print ()
print ('=' * 50)