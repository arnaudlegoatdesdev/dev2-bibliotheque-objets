from datetime import datetime


class Cathegorie_Valeur:
    def __init__(self, id_cathegorie,titre,description,montant_caution,id_administrateur) -> None:
        self.__id_cathegorie = id_cathegorie
        self.__titre = titre
        self.__description = description
        self.__montant_caution = montant_caution
        self.__id_administrateur = id_administrateur
        self.__create_at = datetime.today()
        self.__update_at = datetime.today()

    @property
    def id_cathegorie(self) -> str:
        return self.__id_cathegorie

    @property
    def titre(self) -> str:
        return self.__titre

    @titre.setter
    def titre(self, titre) -> None:
        self.__titre = titre

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description) -> None:
        self.__description = description

    @property
    def montant_caution(self) -> int:
        return self.__montant_caution

    @montant_caution.setter
    def montant_caution(self, montant_caution) -> None:
        self.__montant_caution = montant_caution

    @property
    def id_administrateur(self) -> str:
        return self.__id_administrateur

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
