from datetime import datetime, date


class Reservations:
    def __init__(self,id_reservation,date_reservation,date_emprunt,id_membre):
        self.__id_reservation = id_reservation
        self.__date_reservation = date_reservation
        self.__date_emprunt = date_emprunt
        self.__id_membre = id_membre

    @property
    def id(self) -> str:
        return self.__id_reservation

    @property
    def date_reservation(self) -> date:
        return self.__date_reservation

    @property
    def date_emprunt(self) -> date:
        return self.__date_emprunt

    @property
    def id_membre(self) -> str:
        return self.__id_membre

    @id.setter
    def id(self,id_reservation) -> None:
        self.__id_reservation = id_reservation

    @date_reservation.setter
    def date_reservation(self,date_reservation) -> None:
        self.__date_reservation = date_reservation

    @date_emprunt.setter
    def date_emprunt(self,date_emprunt) -> None:
        self.__date_emprunt = date_emprunt







