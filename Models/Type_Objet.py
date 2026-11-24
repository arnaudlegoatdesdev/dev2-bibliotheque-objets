from datetime import datetime


class Type_Objet:
    def __init__(self, id_type_objet,titre,description,piece_manquante_possible,id_administrateur,create_at,update_at) -> None:
        self.__id_type_objet = id_type_objet
        self.__titre = titre
        self.__description = description
        self.__piece_manquante_possible = piece_manquante_possible
        self.__id_administrateur = id_administrateur
        self.__create_at = datetime.strptime(create_at, '%d/%m/%Y')
        self.__update_at = update_at


    @property
    def id_type_objet(self) -> str:
        return self.__id_type_objet

    @property
    def titre(self) -> str:
        return self.__titre

    @property
    def description(self) -> str:
        return self.__description

    @property
    def piece_manquante_possible(self) -> bool:
        return self.__piece_manquante_possible

    @property
    def id_administrateur(self) -> str:
        return self.__id_administrateur

    @property
    def update_at(self) -> str:
        return self.__update_at

    @titre.setter
    def titre(self,titre) -> None:
        self.__titre = titre

    @description.setter
    def description(self,description) -> None:
        self.__description = description


    @piece_manquante_possible.setter
    def piece_manquante_possible(self,value) -> None:
        self.__piece_manquante_possible = value

    @update_at.setter
    def update_at(self) -> None:
        self.__update_at = datetime.now()

    def __str__(self):
        pass