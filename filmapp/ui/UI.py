from filmapp.domain.Film import Film


class UI:

    def __init__(self, service):
        self.__service = service

    def print_meniu(self):
        print("1. Afisare filme")
        print("2. Adaugare film")
        print("3. Afisare filme categorie")
        print("4. Medie rating categorie")
        print("5. Sortare")
        print("0. Iesire")

    def program(self):
        ruleaza = True
        while ruleaza == True:
            self.print_meniu()
            comanda = input("Comanda:")
            if comanda == "1":
                self.afisare_filme()
            elif comanda == "2":
                self.adauga_film()
            elif comanda == "3":
                self.afisare_filme_categorie()
            elif comanda == "4":
                self.medie_categorie()
            elif comanda == "5":
                self.sortare()
            elif comanda == "0":
                ruleaza = False

    def afisare_filme(self):
        toate_filmele = self.__service.get_all()
        for film in toate_filmele:
            print(film)

    def adauga_film(self):
        try:
            id = int(input("ID:"))
            nume = input("Nume:")
            categorie = input("Categorie:")
            rating = int(input("Rating:"))
            film = Film(id, nume, categorie, rating)
            self.__service.adauga(film)
        except Exception as e:
            print(e)

    def afisare_filme_categorie(self):
        categorie = input("Categorie:")
        filme_din_categorie = self.__service.get_filme_categorie(categorie)
        for film in filme_din_categorie:
            print(film)

    def medie_categorie(self):
        categorie = input("Categorie:")
        medie_categorie = self.__service.calculeaza_medie_categorie(categorie)
        print(medie_categorie)

    def sortare(self):
        filme_sortate = self.__service.sorteaza_filme()
        for film in filme_sortate:
            print(film)