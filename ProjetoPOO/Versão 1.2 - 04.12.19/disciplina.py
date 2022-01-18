class Disciplina():
    def __init__(self, nome, tema1, tema2):
        self.__nome = nome
        self.__tema1 = tema1
        self.__tema2 = tema2

#   get

    def get_nome(self):
        return self.__nome
    def get_tema1(self):
        return self.__tema1
    def get_tema2(self):
        return self.__tema2

#   set

    def set_nome(self, novo):
        self.__nome = novo
    def set_tema1(self, novo):
        self.__tema1 = novo
    def set_tema2(self, novo):
        self.__tema2 = novo

#   propriedades

    nome = property(get_nome, set_nome)
    tema1 = property(get_tema1, set_tema1)
    tema2 = property(get_tema2, set_tema2)
#   mostrando

    def __str__(self):
        s = f'Disciplina: \n{str(self.__nome)}\nTemas: \n{str(self.__tema1)}\n{str(self.__tema2)}'
        return s