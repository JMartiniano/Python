arquivo = open('cadastro.txt', 'w')

nome = input('Seu nome: ')
addnome = arquivo.write(nome + ',')
sexo = input('Sexo: ')
addsexo = arquivo.write(sexo + ',')
idade = input('Idade: ')
addidade = arquivo.write(idade + "\n")
nome = input('Seu nome: ')
addnome = arquivo.write(nome)
while ( nome != '' ):
    sexo = input('Sexo: ')
    addsexo = arquivo.write(',' + sexo + ',')
    idade = input('Idade: ')
    addidade = arquivo.write(idade + "\n")
    nome = input('Seu nome: ')
    addnome = arquivo.write(nome)
arquivo.close()

arquivo = open('cadastro.txt', 'r')
linha = arquivo.readline()

while linha:
    print (linha, end= '')
    linha = arquivo.readline()
arquivo.close()
