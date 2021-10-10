from programas import ProgramasStream

class Filmes(ProgramasStream):
    def __init__(self, name, year, likes, duration, premiere, date):
        super().__init__(name, year, likes)
        self.__duration = duration
        self.__premiere = premiere
        self.__date = date

    def get_duration(self):
        return self.__duration
    def set__duration(self, newDuration):
        self.__duration = newDuration
    def get_premiere(self):
        return self.__premiere
    def set_premiere(self, newPremiere):
        self.__premiere = newPremiere
    def get_date(self):
        return self.__date
    def set_date(self, newDate):
        self.__date = newDate

    duration = property(get_duration, set__duration)
    premiere = property(get_premiere, set_premiere)
    date = property(get_date, set_date)

    def show(self):
        print(f'Duration: {str(self.__duration)}\nPremiere: {str(self.__premiere)}')
