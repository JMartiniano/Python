print ('=' * 50)
print ('Bem-vindo!\nNeste programa você poderá descobrir quantos caractéries tem em um arquivo texto.\nLembre-se, espaços em branco não contam!\nVamos começar!')
print ('=' * 50)
print ()
arqlido = input ('Nome do arquivo: ')

cont = 0

arq = open (arqlido, 'r')
arqlido = arq.read()

for k in range ((len(arqlido))):
    if (arqlido[k] != ' ') and (arqlido[k] != '\n'):
        cont += 1
arq.close()
print ()
print ('=' * 50)
print ('Quantidade de Caractéries: ')
print (cont)
print ('=' * 50)
print ('ENCERRADO')