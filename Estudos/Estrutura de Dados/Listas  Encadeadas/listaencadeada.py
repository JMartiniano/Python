listaEncadeada.py

import node
   #Primeira Forma
class listaEncadeada(object):
   def __init__(self):
       self.cabeca = None
       self.cauda = None
   #Mostra Primeira forma
   def mostrarLista(no):
       while (no != None):
           print(no.getValor())
           no = .getProximo()

   #Segunda Forma
   def inserirNo(self, valor):
       item = node.No()
       item.setValor(valor)

       if (self.cabeca == None) and (self.cauda == None):
           self.cabeca = item
           self.cauda = item
       else:
           self.cauda.setProximo(item)
           item.setProximo(None)
           self.cauda = item

   def printLista(self):
       no = self.cabeca