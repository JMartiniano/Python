class Animal():
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    def caminha(self):
        return 'Andou'
    def get_nome(self):
        return self.__nome
    def set_nome(self, novo):
        self.__nome = novo
    def get_raca(self):
        return self.__raca
    def set_raca(self, novo):
        self.__raca = novo

    caminha = property(caminha)
    nome = property(get_nome, set_nome)
    raca = property(get_raca, set_raca)

    def __str__(self):
        s = f'Nome: {self.__nome}\nRaça: {self.__raca}'
        return s
