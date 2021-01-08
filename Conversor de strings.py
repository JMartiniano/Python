print("Conversor de strings!")

while True:
    op = int(input("1 - Tudo minúsculo\n2 - Tudo maiúsculo\n3 - Iniciais Maiúsculas\n0 - Sair\nEscolha:"))
    if op != 0:
        string = input("Entrada: ")
        if op == 1:
            print(f"Saída: {string.lower()}")
        elif op == 2:
            print(f"Saída: {string.upper()}")
        elif op == 3:
            print(f"Saída: {string.capitalize()}")
    else:
        break
