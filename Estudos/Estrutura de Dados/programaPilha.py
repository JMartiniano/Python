import pilhas

#======= Abrindo uma variável para usar a Pilha =========
pilhaTeste = pilhas.Pilha()
#========================================================

#============= printando ===
print(pilhaTeste.getPilha())
#===========================

#======== Inserindo elementos =======
valor = input("Insira um elemento: ")
pilhaTeste.inserirDados(valor)
pilhaTeste.inserirDados("Roxo")
#====================================

#===== Printando o novo estado da Pilha ===============
print(pilhaTeste.getPilha())
#======================================================


#=============== Removendo do topo ====================
pilhaTeste.removerDado()
#======================================================

#===== Printando o novo estado da Pilha ===============
print(pilhaTeste.getPilha())
#======================================================

#======== Achando o topo da Pilha =====================
print(pilhaTeste.topo())
#======================================================

#================ esvaziando a pilha ==================
pilhaTeste.esvaziar()
#======================================================

#===== Printando o novo estado da Pilha ===============
print(f'Pilha esvaziada: {pilhaTeste.getPilha()}')
#======================================================

