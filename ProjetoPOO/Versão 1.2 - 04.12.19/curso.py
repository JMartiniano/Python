class Curso():
    def __init__(self, nome, dcp1, dcp2):
        self.__nome = nome
        self.__dcp1 = dcp1
        self.__dcp2 = dcp2

#   get

    def get_nome(self):
        return self.__nome
    def get_dcp1(self):
        return self.__dcp1
    def get_dcp2(self):
        return self.__dcp2
#   set

    def set_nome(self, novo):
        self.__nome = novo
    def set_dcp1(self, novo):
        self.__dcp1 = novo
    def set_dcp2(self, novo):
        self.__dcp2 = novo

#   propriedades

    nome = property(get_nome, set_nome)
    dcp1 = property(get_dcp1, set_dcp1)
    dcp2 = property(get_dcp2, set_dcp2)

#   mostrando

    def __str__(self):
        s = f'{str(self.__nome)}'
        return s
