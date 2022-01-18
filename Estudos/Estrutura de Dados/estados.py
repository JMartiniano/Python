import estadosmain

pilhaTeste = estadosmain.Pilha()
print(f"Situação atual da pilha: {pilhaTeste.getPilha()}")
print('=' * 50)
escolha = input('Deseja add um novo estado? [Y/N]')
while ( escolha == "Y" ) or ( escolha == 'y' ):
    ne = input('Novo estado: ')
    pilhaTeste.inserirDados(ne)
    print('=' * 50)
    print(f"Situação atual da pilha: {pilhaTeste.getPilha()}")
    print('=' * 50)
    escolha = input('Deseja add um novo estado? [Y/N]')
else:
    print('=' * 50)
    print("ENCERRADO!")
    print('=' * 50)
    print(f"Situação final da pilha: {pilhaTeste.getPilha()}")
    print('=' * 50)