from Enums.RoleUser import RoleUser
from Models.User import User


class Benevole(User):
    def __init__(self, matricule,id_user, nom,prenom,date_naissance,email,password,telephone,image) -> None:
        super().__init__(id_user, nom,prenom,date_naissance,email,password,telephone,image)
        self.__matricule = matricule
        self.__role = RoleUser.BENEVOLE

    @property
    def matricule(self):
        return self.__matricule

    @property
    def role(self) -> RoleUser:
        return self.__role

    def __str__(self) -> str:
        pass