class Abonnement:
    def __init__(self,id_abonnement,date_debut,date_fin,mat_benevole,id_membre,id_type_abonnement):
        self.__id_abonnement = id_abonnement
        self.__date_debut = date_debut
        self.__date_fin = date_fin
        self.__mat_benevole = mat_benevole
        self.__id_membre = id_membre
        self.__id_type_abonnement = id_type_abonnement


    @property
    def id_abonnement(self) -> int:
        return self.__id_abonnement

    @property
    def date_debut(self) -> str:
        return self.__date_debut

    @date_debut.setter
    def date_debut(self,date_debut):
        self.__date_debut = date_debut

    @property
    def date_fin(self) -> str:
        return self.__date_fin

    @date_fin.setter
    def date_fin(self,date_fin):
        self.__date_fin = date_fin

    @property
    def mat_benevole(self):
        return self.__mat_benevole

    @property
    def id_membre(self):
        return self.__id_membre


    @property
    def id_type_abonnement(self):
        return self.__id_type_abonnement


    def __str__(self):
        pass