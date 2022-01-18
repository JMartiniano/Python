# Importando biblioteca para gerar números aleatórios
from random import randint

# Definindo a quantidade de dígitos por senha
tam = 8

# For que irá gerá 643 senhas aleatórias de 8 dígitos cada
for i in range(2):
    senha = int(''.join(str(randint(0,9)) for _ in range(tam)))
    while len(str(senha)) != tam:
        senha = int(''.join(str(randint(0,9)) for _ in range(tam)))
    # Escreve a senha gerada no arquivo que foi criado antes
    print(f"{str(senha)}\n")