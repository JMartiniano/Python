class InserirQuestao():
    def __init__(self, questao):
        self.__questao = questao

#   GET

    def get_questao(self):
        return self.__questao

#   SET

    def set_questao(self, novo):
        self.__questao = novo

#   PROPRIEDADES

    questao = property(get_questao, set_questao)

#   MOSTRANDO

    def __str__(self):
        s = f'Questão: {str(self.questao)}'
        return s
