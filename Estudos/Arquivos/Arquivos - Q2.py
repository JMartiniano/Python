arq_lido = input ('Nome do arquivo: ')

arq = open (arq_lido, 'r')
arq_copia = open ('copia.txt','w')

arquivo= arq.readline()

while (arquivo):
    for k in range(len(arquivo)):
        if (arquivo[k] != ' '):
            arq_copia.write(arquivo[k])
        else:
            arq_copia.write('.')
    arquivo = arq.readline()

arq.close()
arq_copia.close()