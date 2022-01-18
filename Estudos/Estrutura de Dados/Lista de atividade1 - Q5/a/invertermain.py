import inverter
pilhaTeste = inverter.Pilha()
print ('=~' * 50)
print ('Criando uma Pilha S: ')
elemento = [x for x in input('Insira os elementos que seja na pilha: ').split()]
tam = len(elemento)
for x in range (tam):
    pilhaTeste.inserir(elemento[x])
print(pilhaTeste.getPilha())
pilhaTeste.inverter()
print ('Sua pilha está sendo invertida, aguarde um momento...')
print('Estamos quase acabando...')
print ('Pronto, terminamos!')
print(pilhaTeste.inverter())