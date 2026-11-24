from datetime import datetime


class Sauvegarde:
    def __init__(self, id_membre, titre, description,date,url,id_benevole):
        self.__id_membre = id_membre
        self.__titre = titre
        self.__description = description
        self.__date = date
        self.__url = url
        self.__id_benevole = id_benevole
        self.__create_at = datetime.today()
        self.__update_at = datetime.today()

    @property
    def id_membre(self) -> str:
        return self.__id_membre

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
    def date(self) -> datetime:
        return self.__date

    @date.setter
    def date(self, date) -> None:
        self.__date = date

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url) -> None:
        self.__url = url

    @property
    def id_benevole(self):
        return self.__id_benevole

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