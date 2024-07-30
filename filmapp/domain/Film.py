class Film:

    def __init__(self, id, nume, categorie, rating):
        self.__id = id
        self.__nume = nume
        self.__categorie = categorie
        self.__rating = rating

    def get_categorie(self):
        return self.__categorie

    def get_rating(self):
        return self.__rating

    def __str__(self):
        return "Film " + str(self.__id) + ", " + self.__nume + ", " + self.__categorie + ", " + str(self.__rating)