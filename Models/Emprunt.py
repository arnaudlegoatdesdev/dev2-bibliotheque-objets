from datetime import date, datetime


class Emprunt:
    def __init__(self,id_emprunt,date_debut,date_prevu,date_retour,id_benevole,id_objet,id_membre):
        self.__id_emprunt = id_emprunt
        self.__date_debut = date_debut
        self.__date_prevu = date_prevu
        self.__date_retour = date_retour
        self.__id_benevole = id_benevole
        self.__id_objet = id_objet
        self.__id_membre = id_membre


    @property
    def id(self):
        return self.__id_emprunt

    @property
    def date_debut(self) -> date:
        return self.__date_debut

    @date_debut.setter
    def date_debut(self,date_debut) -> None:
        self.__date_debut = date_debut

    @property
    def date_prevu(self) -> date:
        return self.__date_prevu

    @date_prevu.setter
    def date_prevu(self,date_prevu) -> None:
        self.__date_prevu = date_prevu

    @property
    def date_retour(self) -> date:
        return self.__date_retour

    @date_retour.setter
    def date_retour(self,date_retour) -> None:
        self.__date_retour = date_retour

    @property
    def id_benevole(self) -> int:
        return self.__id_benevole

    @property
    def id_objet(self) -> int:
        return self.__id_objet

    @property
    def id_membre(self) -> int:
        return self.__id_membre

    #la classe n'est pas encore terminé il faudra revenir pour faire son str
    # def __str__(self):


