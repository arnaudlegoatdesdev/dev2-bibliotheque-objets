from datetime import datetime


class Sauvegarde:
    def __init__(self, id_membre, titre, description,date,type,url,id_benevole,create_at, update_at):
        self.__id_membre = id_membre
        self.__titre = titre
        self.__description = description
        self.__date = date
        self.__type = type
        self.__url = url
        self.__id_benevole = id_benevole
        self.__create_at = datetime.strptime(create_at, '%d/%m/%Y')
        self.__update_at = update_at

    @property
    def id_membre(self) -> str:
        return self.__id_membre

    @property
    def titre(self) -> str:
        return self.__titre

    @property
    def description(self) -> str:
        return self.__description

    @property
    def date(self):
        return self.__date

    @property
    def type(self):
        return self.__type

    @property
    def url(self):
        return self.__url

    @property
    def id_benevole(self):
        return self.__id_benevole

    @property
    def create_at(self):
        return self.__create_at

    @property
    def update_at(self):
        return self.__update_at

    @titre.setter
    def titre(self, titre):
        self.__titre = titre

    @description.setter
    def description(self, description):
        self.__description = description

    @date.setter
    def date(self, date):
        self.__date = date

    @type.setter
    def type(self, type):
        self.__type = type

    @url.setter
    def url(self, url):
        self.__url = url

    @update_at.setter
    def update_at(self) -> None:
        self.__update_at = datetime.now()

    def __str__(self):
        pass