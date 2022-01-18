arq_lido = input ('Informe o nome do arquivo: ')
arq = open (arq_lido, 'r')
arquivo = arq.read()
arq.close()

print ('=' * 50)
print (f'O conteúdo do seu arquivo é:\n{arquivo}')
print ('=' * 50)