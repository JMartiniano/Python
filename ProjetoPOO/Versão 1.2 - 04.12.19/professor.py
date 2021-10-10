class Professor():
    def __init__(self, nome, curso, disciplina):
        self.__nome = nome
        self.__curso = curso
        self.__disciplina = disciplina

#   GETS

    def get_nome(self):
        return self.__nome
    def get_curso(self):
        return self.__curso
    def get_disciplina(self):
        return self.__disciplina

#   SETS

    def set_nome(self, novo):
        self.__nome = novo
    def set_curso(self, novo):
        self.__curso = novo
    def set_disciplina(self, novo):
        self.__disciplina = novo

#   ´PROPERTY

    nome = property(get_nome, set_nome)
    curso = property(get_curso, set_curso)
    disciplina = property(get_disciplina, set_disciplina)

#   MOSTRANDO

    def __str__(self):
        s = f'Professor: {str(self.__nome)}\nCurso cadastrado: {str(self.__curso)}\nDisciplina responsável: {str(self.__disciplina.nome)}'
        return s
