from datetime import date, datetime
from Enums.StatutUser import StatutUser


class User:
    def __init__(self, id_user, nom,prenom,date_naissance,email,telephone,image):
        self.__id_user = id_user
        self.__nom = nom
        self.__prenom = prenom
        self.__date_naissance = date_naissance
        self.__email = email
        self.__telephone = telephone
        self.__image = image
        self.__statut = StatutUser.ACTIF
        self.__create_at = datetime.today()
        self.__update_at = datetime.today()

    @property
    def id_user(self) -> str:
        return self.__id_user

    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom) -> None:
        self.__nom = nom

    @property
    def prenom(self) -> str:
        return self.__prenom

    @prenom.setter
    def prenom(self, prenom) -> None:
        self.__prenom = prenom

    @property
    def date_naissance(self) -> date:
        return self.__date_naissance

    @date_naissance.setter
    def date_naissance(self, date_naissance) -> None:
        self.__date_naissance = date_naissance

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email) -> None:
        self.__email = email

    @property
    def telephone(self) -> int:
        return self.__telephone

    @telephone.setter
    def telephone(self, telephone) -> None:
        self.__telephone = telephone

    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image) -> None:
        self.__image = image

    @property
    def statut(self) -> StatutUser:
        return self.__statut

    @statut.setter
    def statut(self, statut: StatutUser) -> None:
        self.__statut = statut

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