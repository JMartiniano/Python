dicionario = {}
'''
for x in range(2):
    name = input("Type your name, bicth: ")
    endereco = input("Street of you house: ")
    data = input("Nascimento D/M/A: ")
    dicionario[name] = [endereco, data]

print(dicionario)
#p = input("Pesquisa")
#print(dicionario[p])

#mostrando dicionario, conteúdo sem chave:

print ('Mostrando os conteúdos sem a chave:')
for valor in dicionario.values():
    print(valor)

#mostrando dicionario, chave sem conteúdo:

print ('Mostrando as chaves sem conteúdos:')
for chave in dicionario.keys():
    print (chave)

#mostrando dicionario, item com valor um por um:

print ('Mostrando valor com chaves:')
for items in dicionario.items():
    print(items)
'''

for x in range(2):
    endereco = input('Endereço:')
    cep = int(input('CEP: '))
    dicionario[endereco] = cep

print('CEPS: ')
for valor in dicionario.values():
    print(valor)

print(dicionario[input('Pesquisa o endereço: ')])
#print(dicionario[int(input('Pesquisa o CEP: '))])
a = int(input('Pesquisa o CEP: '))
for valor in dicionario.values():

#remover:
#Se remorer a chave a apaga tudo:

dicionario.pop('Chave que quero remover')

#Se eu quero remover uma chave pelo conteúdo:

del(dicionario['Conteúdo que eu quero apagar a chabe com tudo'])
#remocer:
#para remover valor e manter a chave:

dicionario["Chave que vai limpar todo o valor"] = None

#FAZER EXERCÌCIO D