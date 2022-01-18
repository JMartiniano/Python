class Universidade():
    def __init__(self, curso1, curso2):
        self.__curso1 = curso1
        self.__curso2 = curso2

#   gets

    def get_curso1(self):
        return self.__curso1
    def get_curso2(self):
        return self.__curso2
#   sets

    def set_curso1(self, novo):
        self.__curso1 = novo
    def set_curso2(self, novo):
        self.__curso2 = novo

#   propriedades

    curso1 = property(get_curso1, set_curso1)
    curso2 = property(get_curso2, set_curso2)

#   mostrando

    def __str__(self):
        s = f'Cursos: \n{str(self.__curso1)}\n{str(self.__curso2)}'
        return s
