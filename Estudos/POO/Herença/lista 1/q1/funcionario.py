'''
Analise o panorama a seguir, desenhe o diagrama de classes e a implemente. No presente projeto,
identificou-se a classe Funcionario e a classe Gerente. Funcionario tem nome, id e salário como
características. Além disso, Gerente tem nome, id, salário, gratificação e agência que administra como
características.
'''

class Funcionario():
    def __init__(self, nome, id, salario):
        self.__nome = nome
        self.__id = id
        self.__salario = salario

    def get_nome(self):
        return self.__nome
    def set_nome(self, novoNome):
        self.__nome = novoNome
    def get_id(self):
        return self.__id
    def set_id(self, novoID):
        self.__id = novoID
    def get_salario(self):
        return self.__salario
    def set_salario(self, novoSalario):
        self.__salario = novoSalario

    nome = property(get_nome, set_nome)
    id = property(get_id, set_id)
    salario =  property(get_salario, set_salario)

    def __str__(self):
        s = f'Nome: {self.__nome}\nID: {self.__id}\nSalario: {self.__salario}'
        return s