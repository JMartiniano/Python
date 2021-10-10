class ProgramasStream():
    def __init__(self, name, year, likes):
        self.__name = name
        self.__year = year
        self.__likes = likes

    def get_name(self):
        return self.__name
    def set_name(self, newName):
        self.__name = newName
    def get_year(self):
        return self.__year
    def set_year(self, newYear):
        self.__year = newYear
    def get_likes(self):
        return self.__likes
    def set_likes(self, newLikes):
        self.__likes = newLikes

    name = property(get_name, set_name)
    year = property(get_year, set_year)
    likes = property(get_likes, set_likes)

    def show(self):
        print(f'Title: {str(self.__nome)}\nYear: {str(self.__year)}\nLikes: {str(self.__likes)}')