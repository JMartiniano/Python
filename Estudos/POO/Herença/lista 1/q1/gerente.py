'''
Analise o panorama a seguir, desenhe o diagrama de classes e a implemente. No presente projeto,
identificou-se a classe Funcionario e a classe Gerente. Funcionario tem nome, id e salário como
características. Além disso, Gerente tem nome, id, salário, gratificação e agência que administra como
características.
'''
from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, id, salario, gratificacao, agencia):
        super().__init__(nome, id, salario)
        self.__gratificacao = gratificacao
        self.__agencia = agencia

    def get_gratificacao(self):
        return self.__gratificacao
    def set_gratificacao(self, novo):
        self.__gratificacao = novo
    def get_agencia(self):
        return self.__agencia
    def set_agencia(self, novo):
        self.__agencia = novo

    gratificacao = property(get_gratificacao, set_gratificacao)
    agencia = property(get_agencia, set_agencia)

    def __str__(self):
        s = f'Nome: {super().nome}\nID: {super().id}\nSalario: {super().salario}\nGratificação: {self.__gratificacao}\nAgência: {self.__agencia}'
        return s

