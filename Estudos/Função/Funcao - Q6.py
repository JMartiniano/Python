def vogal (a):
    if ( a == 'a') or ( a == 'e') or ( a == 'i') or ( a == 'o') or ( a == 'u'):
        return True
    else:
        return False

letra = input("Letra: ")
atribuidor = vogal(letra)
print(atribuidor)