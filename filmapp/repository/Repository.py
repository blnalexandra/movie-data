from filmapp.domain.Film import Film

class Repository:

    def __init__(self):
        self.__filme = []

    def get_all(self):
        return self.__filme

    def adauga(self, film):
        self.__filme.append(film)