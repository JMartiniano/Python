from listaencadeada import ListaEncadeada

def main():
    lista1 = ListaEncadeada()
    lista2 = ListaEncadeada()
    #lista3 = ListaEncadeada()
    valor1 = input('Lista 1: ')
    while valor1 != 'e':
        valor1 = int(valor1)
        lista1.InserirNo(valor1)
        #lista3.InserirNo(valor1)
        valor1 = input('Lista 1:')
    valor2 = input('Valor 2: ')
    while valor2 != 'e':
        valor2 = int(valor2)
        lista2.InserirNo(valor2)
        #lista3.InserirNo(valor2)
        #lista2.removerNo(valor2)
        valor2 = input('Valor 2: ')
    print('Lista 1:')
    lista1.printListas()
    print('Lista 2:')
    lista2.printListas()

    print('Concatenado: ')
    lista1.concatenando(lista1, lista2)
    print('Lista 1:')
    lista1.printListas()
    #lista3.printListas()
    print('Lista 2:')
    lista2.printListas()


main()
