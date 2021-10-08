# Importando biblioteca para gerar números aleatórios
from random import randint

# Abrindo o arquivo onde serão gravadas as senhas geradas
arqsenhas = open('/home/martiniano/Documentos/CadastroEscolas/senhas.txt', 'a')

# Definindo a quantidade de dígitos por senha
tam = 8

# For que irá gerá 643 senhas aleatórias de 8 dígitos cada
for i in range(643):
    senha = int(''.join(str(randint(0,9)) for _ in range(tam)))
    while len(str(senha)) != tam:
        senha = int(''.join(str(randint(0,9)) for _ in range(tam)))
    # Escreve a senha gerada no arquivo que foi criado antes
    arqsenhas.write(f"{str(senha)}\n")