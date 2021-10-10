from programas import ProgramasStream

class Series(ProgramasStream):
    def __init__(self, name, year, likes, seasons, spinoffs):
        super().__init__(name, year, likes)
        self.__seasons = seasons
        self.__spinoffs = spinoffs

    def get_seasons(self):
        return self.__seasons
    def set_seasons(self, newSeaons):
        self.__seasons = newSeaons
    def get_spinoffs(self):
        return self.__spinoffs
    def set_spinoffs(self, newSpinoffs):
        self.__spinoffs = newSpinoffs

    seasons = property(get_seasons, set_seasons)
    spinoffs = property(get_spinoffs, set_spinoffs)

    def show(self):
        print(f'Seasons: {str(self.__seasons)}\nSpinoffs: {str(self.__spinoffs)}')