class Coordenador():
    def __init__(self, nome, universidade):
        self.__nome = nome
        self.__universidade = universidade

#   GETS

    def get_nome(self):
        return self.__nome
    def get_universidade(self):
        return self.__universidade

#   SETS

    def set_nome(self, novo):
        self.__nome = novo
    def set_universidade(self, novo):
        self.__universidade = novo

#   PROPERTY

    nome = property(get_nome, set_nome)
    universidade = property(get_universidade, set_universidade)

#   MOSTRANDO

    def __str__(self):
        s = f'Coordenador Geral: {str(self.__nome)}\nUniversidade: {str(self.__universidade)}'
        return s
