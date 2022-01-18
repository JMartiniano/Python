class Funcionario:
    #construtor
    def __init__(self, nome, dpto, salr, dataEn, rg): #características do funcinonario
        #atributos
        self.__nome = nome
        self.__dpto = dpto
        self.__salario = salr
        self.__dataEntrada = dataEn
        self.__rg = rg

        '''
        As variáveis recebem __ no começo para encapsular elas e torná-las imutáveis no arquivo main
        Quando usamos esse tipo de variável não podemos mais chama-las no main, tornando impossível printa-las,
        sendo necessário criar funções para printar ou alterar as variáveis
        '''
#Agora para atribuir esses valores vamos abrir outro arquivo main para importar a class

    #Obeter - get
    #salario

    def get_salario(self):
        return self.__salario

    def get_GanhoAnual(self):
        return self.__salario * 12

    #Redefinir - Set
    #Redefinindo salário

    def set_salario(self, novoSa):
        self.__salario = novoSa

    def set_aumento(self, aumento):
        self.__salario *= (1 + aumento/100)
