from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def late(self):
        return 'Auau'
    late = property(late)
    def __str__(self):
        s = f'{super().caminha}\n{self.late}'
        return s