class Aluno:
    def __init__(self, nome, matricula, endereco, cpf):
        self.__nome = nome
        self.__matricula = matricula
        self.__endereco = endereco
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def get_endereco(self):
        return self.__endereco

    def get_cpf(self):
        return self.__cpf