from contextlib import nullcontext
from datetime import date, datetime

from Enums.StatutEmprunt import StatutEmprunt


class Emprunt:
    def __init__(self,id_emprunt,date_debut,date_prevu_retour,date_retour,id_benevole,ids_objets,id_membre):
        self.__id_emprunt = id_emprunt
        self.__date_debut = date_debut
        self.__date_prevu_retour = date_prevu_retour
        self.__date_retour = date_retour
        self.__id_benevole = id_benevole
        self.__ids_objets = ids_objets
        self.__caution_restituer = None
        self.__status_emprunt = StatutEmprunt.EN_COURS
        self.__id_membre = id_membre
        self.__create_at = datetime.today()
        self.__update_at = datetime.today()

    @property
    def id(self) -> str:
        return self.__id_emprunt

    @property
    def date_debut(self) -> date:
        return self.__date_debut

    @date_debut.setter
    def date_debut(self,date_debut) -> None:
        self.__date_debut = date_debut

    @property
    def date_prevu_retour(self) -> date:
        return self.__date_prevu_retour

    @date_prevu_retour.setter
    def date_prevu_retour(self,date_prevu_retour) -> None:
        self.__date_prevu_retour= date_prevu_retour

    @property
    def date_retour(self) -> date:
        return self.__date_retour

    @date_retour.setter
    def date_retour(self,date_retour) -> None:
        self.__date_retour = date_retour

    @property
    def caution_restituer(self) -> int | None:
        return self.__caution_restituer

    @caution_restituer.setter
    def caution_restituer(self,caution_restituer) -> None:
        self.__caution_restituer = caution_restituer

    @property
    def status_emprunt(self) -> StatutEmprunt:
        return self.__status_emprunt

    @status_emprunt.setter
    def status_emprunt(self,status_emprunt: StatutEmprunt) -> None:
        self.__status_emprunt = status_emprunt

    @property
    def id_benevole(self) -> int:
        return self.__id_benevole

    @property
    def ids_objets(self) -> list:
        return self.__ids_objets

    @property
    def id_membre(self) -> int:
        return self.__id_membre

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


