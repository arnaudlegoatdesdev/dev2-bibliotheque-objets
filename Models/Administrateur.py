from Models.User import User


class Administrateur(User):
    def __init__(self, matricule, id_user, nom, prenom, date_naissance, email, telephone, image) -> None:
        super().__init__(id_user, nom, prenom, date_naissance, email, telephone, image)
        self.__matricule = matricule

    @property
    def matricule(self):
        return self.__matricule