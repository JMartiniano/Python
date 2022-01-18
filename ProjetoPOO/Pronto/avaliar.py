from inserir import InserirQuestao

class Avaliar(InserirQuestao):
    def __init__(self, questao, voto1, voto2):
        super().__init__(questao)
        self.__voto1 = voto1
        self.__voto2 = voto2

#   GETS

    def get_voto1(self):
        return self.__voto1
    def get_voto2(self):
        return self.__voto2

#   SET

    def set_voto1(self, novo):
        self.__voto1 = novo
    def set_voto2(self, novo):
        self.__voto2 = novo

#   MÉTOODO DE AVALIAÇÃO

    def avaliacao(self, a):
        a = super().questao
        avl_ap = []
        avl_refazer = []
        if self.__voto1 == 1 or self.__voto2 == 2:
            print('Avaliação Reprovada !')
        elif (self.__voto1 == 2 and self.__voto2 == 3) or (self.__voto1 == 3 and self.__voto2 == 2):
            avl_refazer.append(a)
        else:
            avl_ap.append(a)
        return avl_ap, avl_refazer

#   PROPERTY

    voto1 = property(get_voto1, set_voto1)
    voto2 = property(get_voto2, set_voto2)

#   MOSTRANDO

    def __str__(self):
        s = f'Questao em votação: {super().questao}\nVoto 1: {self.__voto1} | Votante: {str(self.__prof1)}\nVoto 2: {self.__voto2} | Votante: {str(self.__prof2)} '
        return s