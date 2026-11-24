
from datetime import datetime


class Membre:
    def __init__(self,id_membre, nom, prenom,tel,adresse,email, image, mat_benevole):
        self.__id = id_membre
        self.__nom = nom
        self.__prenom = prenom
        self.__tel = tel
        self.__adresse = adresse
        self.__email = email
        self.__image = image
        self.__mat_benevole = mat_benevole
        self.__create_at = datetime.today()
        self.__update_at = datetime.today()

    @property
    def id(self) -> str:
        return self.__id

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
    def prenom(self,prenom) -> None:
        self.__prenom = prenom

    @property
    def tel(self) -> int:
        return self.__tel

    @tel.setter
    def tel(self, tel) -> None:
        self.__tel = tel

    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image) -> None:
        self.__image = image

    @property
    def adresse(self) -> str:
        return self.__adresse

    @adresse.setter
    def adresse(self,adresse) -> None:
        self.__adresse = adresse

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self,email) -> None:
        self.__email = email

    @property
    def mat_benevole(self) -> str:
        return self.__mat_benevole

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