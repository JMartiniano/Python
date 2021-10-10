from pessoa import Pessoa

class Rica(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def fazCompras(self):
        return 'Fatura do Débito de novembro:\n- Toyta SW4\n- Audi Q5\n- BMW M3'

    fazCompras = property(fazCompras)

    def __str__(self):
        s = f'Nome: {super().nome}\nIdade: {super().idade}\n{self.fazCompras}'
        return s