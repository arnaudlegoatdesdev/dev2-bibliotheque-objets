from datetime import datetime, date


class Reservations:
    def __init__(self,id_reservation,date_reservation,date_prevu_emprunt,id_membre,id_benevole,ids_objets):
        self.__id_reservation = id_reservation
        self.__date_reservation = date_reservation
        self.__date_prevu_emprunt = date_prevu_emprunt
        self.__id_membre = id_membre
        self.__id_benevole = id_benevole
        self.__ids_objets = ids_objets
        self.__create_at = datetime.today()
        self.__update_at = datetime.today()

    @property
    def id_reservation(self) -> str:
        return self.__id_reservation

    @property
    def date_reservation(self) -> date:
        return self.__date_reservation

    @date_reservation.setter
    def date_reservation(self, date_reservation) -> None:
        self.__date_reservation = date_reservation

    @property
    def date_prevu_emprunt(self) -> date:
        return self.__date_prevu_emprunt

    @date_prevu_emprunt.setter
    def date_prevu_emprunt(self,date_prevu_emprunt) -> None:
        self.__date_prevu_emprunt = date_prevu_emprunt

    @property
    def id_membre(self) -> str:
        return self.__id_membre

    @property
    def id_benevole(self) -> int:
        return self.__id_benevole

    @property
    def ids_objets(self) -> list:
        return self.__ids_objets

    @property
    def create_at(self) -> datetime:
        return self.__create_at

    @property
    def update_at(self) -> datetime:
        return self.__update_at

    @update_at.setter
    def update_at(self, valeur) -> None:
        self.__update_at = valeur







