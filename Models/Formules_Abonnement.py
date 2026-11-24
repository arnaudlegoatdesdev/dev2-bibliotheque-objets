from datetime import date, datetime


class Formules_Abonnement:
    def __init__(self,id_type_abonnement,titre,prix_abonnement,nbr_emprunts_possible,matricule_admin):
        self.__id_type_abonnement = id_type_abonnement
        self.__titre = titre
        self.__prix_abonnement = prix_abonnement
        self.__nbr_emprunts_possible = nbr_emprunts_possible
        self.__matricule_admin = matricule_admin
        self.__create_at = datetime.today()
        self.__update_at = datetime.today()

    @property
    def id_type_abonnement(self) -> str:
        return self.__id_type_abonnement

    @property
    def titre(self) -> str:
        return self.__titre

    @titre.setter
    def titre(self, titre) -> None:
        self.__titre = titre

    @property
    def prix_abonnement(self) -> float:
        return self.__prix_abonnement

    @prix_abonnement.setter
    def prix_abonnement(self, prix_abonnement) -> None:
        self.__prix_abonnement = prix_abonnement

    @property
    def nbr_emprunts_possible(self) -> int:
        return self.__nbr_emprunts_possible

    @nbr_emprunts_possible.setter
    def nbr_emprunts_possible(self, nbr_emprunts_possible) -> None:
        self.__nbr_emprunts_possible = nbr_emprunts_possible

    @property
    def matricule_admin(self) -> str:
        return self.__matricule_admin

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