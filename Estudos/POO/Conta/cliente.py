#Criando uma classe para informações do cliente que será agregadas à sua conta
#Assim iremos importar o Cliente no arquivo teste e criar um cliente, depois add ele na conta usando o campo titular.


class Cliente:

    def __init__(self, nome, cpf, dataNascimento, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__dataNascimeto = dataNascimento
        self.__endereco = endereco

    def get_nome(self):
        return self.__nome

    #mostrando de outra forma:
    def __str__(self):
        saida = f'Nome: {self.__nome}\nCpf: {self.__cpf}\nNascimento: {self.__dataNascimeto}\nEndereço: {self.__endereco}'
        return saida



