class Aluno():
    #construtor
    def __init__(self, nome, end, sexo):
        self.__nome = nome
        self.__endereco = end
        self.__sexo = sexo
        self.__turma = None

    def matricularAlunoTurma(self, turma):
        self.__turma = turma

    def get_nome(self):
        return self.__nome
    def set_nome(self, novoNome):
        self.__nome = novoNome
    def get_end(self):
        return self.__endereco
    def set_end(self, novoEnd):
        self.__endereco = novoEnd
    def get_sexo(self):
        return self.__sexo
    def set_sexo(self, novoSexo):
        self.__sexo = novoSexo
    def get_turma(self):
        return self.__turma
    def set_turma(self, novaTurma):
        self.__turma = novaTurma