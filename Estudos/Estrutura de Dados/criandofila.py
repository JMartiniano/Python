#Criando uma fila. Para isso é necessário usar uma classe fila e uma função __init__.
#self é usado para permitir que uma variável que está dentro de uma função seja tratada como uma variável global.

class Fila(object):
    def __init__(self):
        self.dados = []
#Podemos chamar essa fila para outro programa, para isso é precisar criar outro programa que esteja na mesma pasta deste
#que darei o nome de ProgramaFila, nele está o código certo para chamar esta fila

    def getFila(self):
        return self.dados
#Desta forma estamos possíbilitando que a Fila seja printada no ProgramaFila, sempre usando o self. para usar 'dados'

    def novoDado(self, novoValor):
        self.dados.append(novoValor)
#Com esta função estamos dando append no final da fila, os dados será recebidos pelo ProgramaFila

    def removerDado(self):
        self.dados.pop(0)
#Essa função retira o primeiro índice da lista, será chamada no ProgramaFila

    def remover(self,valor):
        posi = self.dados.index(valor)
        for i in range (0, posi + 1):
            self.dados.pop(0)
#Nessa função recebemos uma valor lá no ProgramaFila, aqui ele é tratado como valor, na variável posi achamos o índice
#dele, em seguida usamo o for para irmos do começo da Fila até a posição dele, em seguinda com o pop(0) vamos apagando
#os dados que estão na posiçaõ 0, até que sobre apenas o restante da fila.




