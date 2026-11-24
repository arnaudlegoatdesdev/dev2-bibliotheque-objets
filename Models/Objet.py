from datetime import date, datetime
from Enums.EtatObjet import EtatObjet
from Enums.StatutObjet import StatutObjet


class Objet:
    def __init__(self,id_objet,nom,description,mat_benevole,id_type_objet):
        self.__id_objet = id_objet
        self.__nom = nom
        self.__etat = EtatObjet.BON_ETAT
        self.__statut = StatutObjet.DISPONIBLE
        self.__description = description
        self.__mat_benevole = mat_benevole
        self.__id_type_objet = id_type_objet
        self.__create_at = datetime.today()
        self.__update_at = datetime.today()

    @property
    def id_objet(self) -> str:
        return self.__id_objet

    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self,nom) -> None:
        self.__nom = nom

    @property
    def etat(self) -> EtatObjet:
        return self.__etat

    @etat.setter
    def etat(self,etat: EtatObjet) -> None:
        self.__etat = etat

    @property
    def statut(self) -> StatutObjet:
        return self.__statut

    @statut.setter
    def statut(self,statut: StatutObjet) -> None:
        self.__statut = statut

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self,description) -> None:
        self.__description = description

    @property
    def mat_benevole(self) -> str:
        return self.__mat_benevole

    @property
    def id_type_objet(self) -> str:
        return self.__id_type_objet

    @property
    def create_at(self) -> datetime:
        return self.__create_at

    @property
    def update_at(self) -> datetime:
        return self.__update_at

    @update_at.setter
    def update_at(self, valeur) -> None:
        self.__update_at = valeur

    def __str__(self):
        pass


