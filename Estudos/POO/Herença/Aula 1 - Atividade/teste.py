from filmes import Filmes
from series import Series

def main():
    filme1 = Filmes('A volta dos que não foram', '2035', '1,5M', '200 minutos', 'SIM', '2019' )
    serie1 = Series('Breaking Bad', '2008', '4.9M', '5', 'El Camino')
    print(filme1.show())
    print(serie1.show())
main()