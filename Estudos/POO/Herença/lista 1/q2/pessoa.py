class Pessoa():
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome
    def set_nome(self, novo):
        self.__nome = novo
    def get_idade(self):
        return self.__idade
    def set_idade(self, novo):
        self.__idade = novo

    nome = property(get_nome, set_nome)
    idade = property(get_idade, set_idade)

    def __str__(self):
        s = f'Nome: {self.__nome}\nIdade: {self.__idade}'
        return s