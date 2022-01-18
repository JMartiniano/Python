class Conta:
    #CONSTRUTOR
    def __init__(self, tit, agencia, conta, lim):
        #ATRIBUT0S
        self.__titular = tit
        self.__agencia = agencia
        self.__conta = conta
        self.__limite = lim
        self.__saldo = 0

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def get_saldoBanco(self):
        return self.__saldo+self.__limite

    def __get_saldoReal(self): #este método é privativo assim como os atributos, pra mostrar usa o método de quebrar encapsulamento
        return self.__saldo

#TRABALHANDO COM PROPRIEDADES | Propriedade Getter

    @property #serve para simplificar o modo de acesso no arquivo main ou teste
    def titular(self):
        #return self.__titular
    #Agora já que estamos atibuindo um objeto na variável atributo com  a classe Cliente, a forma de printar muda:
        #return self.__titular.nome #ou return self.__titular.get_nome() | Dessa forma chamamos o conteúdo da variável nome
    #no método get nome na propriedeade titular.
        return self.__titular #Já funciona printando o conteúdo da função str da classe Cliente
    '''
    Como faríamos pra chamar: 
    print(conta.titular)
    '''
