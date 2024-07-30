class Service:

    def __init__(self, repository):
        self.__repository = repository

    def get_all(self):
        return self.__repository.get_all()

    def adauga(self, film):
        self.__repository.adauga(film)

    def get_filme_categorie(self, categorie):
        toate_filmele = self.__repository.get_all()
        filme_categorie = []
        for film in toate_filmele:
            if film.get_categorie() == categorie:
                filme_categorie.append(film)
        return filme_categorie

    def calculeaza_medie_categorie(self, categorie):
        filme_categorie = self.get_filme_categorie(categorie)
        suma = 0
        nr_filme = len(filme_categorie)
        if nr_filme == 0:
            return suma
        else:
            for film in filme_categorie:
                suma += film.get_rating()
            return suma/nr_filme

    def sorteaza_filme(self):
        toate_filmele = self.__repository.get_all()
        filme_sortate = sorted(toate_filmele, key=lambda film:film.get_rating(), reverse=True)
        return filme_sortate