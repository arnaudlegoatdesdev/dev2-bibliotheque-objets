class Type_abonnement:
    def __init__(self,id_type_abonnement,nom_abonnement,prix_abonnement,nbr_emprunts_possible,matricule_admin):
        self.__id_type_abonnement = id_type_abonnement
        self.__nom_abonnement = nom_abonnement
        self.__prix_abonnement = prix_abonnement
        self.__nbr_emprunts_possible = nbr_emprunts_possible
        self.__matricule_admin = matricule_admin


    @property
    def id_type_abonnement(self) -> str:
        return self.__id_type_abonnement

    @property
    def nom_abonnement(self) -> str:
        return self.__nom_abonnement

    @property
    def prix_abonnement(self) -> float:
        return self.__prix_abonnement

    @property
    def nbr_emprunts_possible(self) -> int:
        return self.__nbr_emprunts_possible

    @property
    def matricule_admin(self) -> str:
        return self.__matricule_admin

    @nom_abonnement.setter
    def nom_abonnement(self,nom_abonnement) -> None:
        self.__nom_abonnement = nom_abonnement

    @prix_abonnement.setter
    def prix_abonnement(self,prix_abonnement) -> None:
        self.__prix_abonnement = prix_abonnement

    @nbr_emprunts_possible.setter
    def nbr_emprunts_possible(self,nbr_emprunts_possible) -> None:
        self.__nbr_emprunts_possible = nbr_emprunts_possible

