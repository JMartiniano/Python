from no import No

class ListaEncadeada(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def InserirNo(self, valor):
        item = No()
        item.setValor(valor)
        if (self.head == None) and (self.tail == None):
            self.head = item
            self.tail = item
        else:
            self.tail.setProximo(item)
        item.setProximo(None)
        self.tail = item

    def printListas(self):
        no = self.head
        while (no != None):
            print(no.getValor())
            no = no.proximo

    def concatenando(self, l1, l2):
        no = l1.head
        while (no != None):
            no = no.proximo
        no.setProximo(l2.head)

    def removerNo(self, item):
        no = self.head
        while (no != None):
            if (no.getValor() == item):
                no.setValor(no.proximo.getValor())
                no.setProximo(no.proximo.getProximo())
            no = no.proximo

