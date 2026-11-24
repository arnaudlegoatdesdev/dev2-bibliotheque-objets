from datetime import datetime
from Enums.StatutAbonnement import StatutAbonnement


class Abonnement:
    def __init__(self,id_abonnement,date_debut,date_fin,mat_benevole,id_membre,id_type_abonnement):
        self.__id_abonnement = id_abonnement
        self.__date_debut = date_debut
        self.__date_fin = date_fin
        self.__mat_benevole = mat_benevole
        self.__id_membre = id_membre
        self.__id_type_abonnement = id_type_abonnement
        self.__status_abonnement = StatutAbonnement.ACTIF
        self.__create_at = datetime.today()
        self.__update_at = datetime.today()

    @property
    def id_abonnement(self) -> int:
        return self.__id_abonnement

    @property
    def date_debut(self) -> str:
        return self.__date_debut

    @date_debut.setter
    def date_debut(self, date_debut) -> None:
        self.__date_debut = date_debut

    @property
    def date_fin(self) -> str:
        return self.__date_fin

    @date_fin.setter
    def date_fin(self, date_fin) -> None:
        self.__date_fin = date_fin

    @property
    def status_abonnement(self) -> StatutAbonnement:
        return self.__status_abonnement

    @status_abonnement.setter
    def status_abonnement(self, status_abonnement: StatutAbonnement | str) -> None:
        self.__status_abonnement = StatutAbonnement(status_abonnement)

    @property
    def mat_benevole(self) -> str:
        return self.__mat_benevole

    @property
    def id_membre(self) -> str:
        return self.__id_membre

    @property
    def id_type_abonnement(self) -> None:
        return self.__id_type_abonnement

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