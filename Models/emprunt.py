from datetime import date


class Emprunt:
    def __init__(self, id_emprunt, membre, objet, date_emprunt=None, date_retour=None):
        self._id = id_emprunt
        self._membre = membre
        self._objet = objet
        self._date_emprunt = date_emprunt or date.today()
        self._date_retour = date_retour

    @property
    def id(self):
        return self._id

    @property
    def membre(self):
        return self._membre

    @membre.setter
    def membre(self, valeur):
        self._membre = valeur

    @property
    def objet(self):
        return self._objet

    @objet.setter
    def objet(self, valeur):
        self._objet = valeur

    @property
    def date_emprunt(self):
        return self._date_emprunt

    @property
    def date_retour(self):
        return self._date_retour

    @date_retour.setter
    def date_retour(self, valeur):
        self._date_retour = valeur

    @property
    def en_cours(self):
        return self._date_retour is None