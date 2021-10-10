import node
import listaEncadeada
#Mostra Primeira forma
def mostrarLista(no):
   while (no != None):
       print(no.getValor())
       no = no.getProximo()
#Primeira Forma
def main():
   no1 = node.No()
   no2 = node.No()
   no3 = node.No()

   no1.setValor(1)
   no2.setValor(2)
   no3.setValor(3)

   no1.setProximo(no2)
   no2.setProximo(no3)

   #Segunda Forma
   lista1 = listaEncadeada.listaEncadeada
   lista1 = inserirNo(2)
   lista1 = inserirNo(3)
   lista1 = inserirNo(4)

   def printLista(self):
       no = self.cabeca
       while (no)


main()