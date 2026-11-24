class Objet:
    def __init__(self,id_objet,nom, etat, statut,description,mat_benevole,id_reservation,id_type_objet):
        self.__id_objet = id_objet
        self.__nom = nom
        self.__etat = etat
        self.__statut = statut
        self.__description = description
        self.__mat_benevole = mat_benevole
        self.__id_reservation = id_reservation
        self.__id_type_objet = id_type_objet


    @property
    def id_objet(self):
        return self.__id_objet

    @property
    def nom(self):
        return self.__nom

    @nom.setter(self):
    def nom(self,nom):
        self.__nom = nom

    @property
    def etat(self):
        return self.__etat

    @etat.setter
    def etat(self,etat):
        self.__etat = etat

    @property
    def statut(self):
        return self.__statut

    @statut.setter
    def statut(self,statut):
        self.__statut = statut

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self,description):
        self.__description = description


    @property
    def mat_benevole(self):
        return self.__mat_benevole

    @property
    def id_reservation(self):
        return self.__id_reservation

    @property
    def id_type_objet(self):
        return self.__id_type_objet

    def __str__(self):
        pass


