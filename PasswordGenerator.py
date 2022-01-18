# Importando biblioteca para gerar números aleatórios
from random import randint

# Definindo a quantidade de dígitos por senha
tam = int(input('Password length: '))
total = int(input('How many passwords? '))

optOne = input('Write passwords in a file?[y or n]')

if optOne == 'n' or optOne == 'N':
    # For que irá gerá 643 senhas aleatórias de 8 dígitos cada
    for i in range(total):
        senha = int(''.join(str(randint(0,9)) for _ in range(tam)))
        while len(str(senha)) != tam:
            senha = int(''.join(str(randint(0,9)) for _ in range(tam)))
        # Escreve a senha gerada no arquivo que foi criado antes
        print(f"{(i+1)}: {str(senha)}\n")
elif optOne == 'y' or optOne == 'Y':
    arqName = input('File path with name and extensions: ')
    arq = open(f'{arqName}', 'w')
    optThree = input('Show passwords on screen?[y or n]')
    optTwo = input('Line with numbers?[y or n]')
        # For que irá gerar 643 senhas aleatórias de 8 dígitos cada
    for i in range(total):
        senha = int(''.join(str(randint(0,9)) for _ in range(tam)))
        while len(str(senha)) != tam:
            senha = int(''.join(str(randint(0,9)) for _ in range(tam)))
    
        if optThree == 'y' or optThree == 'Y' and optTwo == 'y' or optTwo == 'Y':
            print(str(senha))
            arq.write(f"{(i+1)}: {str(senha)}\n")
            print ('opção 1')
        
        elif optThree == 'y' or optThree == "Y" and optTwo == 'n' or optTwo == 'N':
            print(str(senha))
            arq.write(f"{str(senha)}\n")
            print ('opção 2')

        elif optThree == 'n' or optThree == 'N' and optTwo == 'n' or optTwo == 'N':
            arq.write(f"{str(senha)}\n")
            print ('opção 3')
        
        elif optThree == 'n' or optThree == 'N' and optTwo == 'y' or optTwo == 'Y':
            print ('opção 4')
            arq.write(f"{(i+1)}: {str(senha)}\n")
        
