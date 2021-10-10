from animal import Animal

class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def mia(self):
        return 'Miau'

    mia = property(mia)

    def __str__(self):
        s = f'{super().caminha}\n{self.mia}'
        return s