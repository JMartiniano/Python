arquivo = open('cadastro.txt', 'r')
homens = 0
mulheres = 0
total = 0

for linha in arquivo:
    dado = linha.split(',')
    if (dado[1] == 'Masculino') or (dado[1] == 'M'):
        homens += 1
    else:
        mulheres += 1
    total = homens + mulheres
print ()
if (homens > 1):
    print ('=' * 50)
    print (f'No arquivo, temos:\n{homens} homemns\n{mulheres} mulher\n{total} como total')
    print ('=' * 50)
elif (mulheres > 1):
    print('=' * 50)
    print(f'No arquivo, temos:\n{homens} homem\n{mulheres} mulheres\n{total} como total')
    print('=' * 50)
else:
    print('=' * 50)
    print(f'No arquivo, temos:\n{homens} homem\n{mulheres} mulher\n{total} como total')
    print('=' * 50)
