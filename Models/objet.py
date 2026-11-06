from Models.etat import ETAT_BON


class Objet:
    def __init__(self, id_objet, nom, description, etat=ETAT_BON, disponible=True):
        self._id = id_objet
        self._nom = nom
        self._description = description
        self._etat = etat
        self._disponible = disponible

    @property
    def id(self):
        return self._id

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, valeur):
        self._nom = valeur

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, valeur):
        self._description = valeur

    @property
    def etat(self):
        return self._etat

    @etat.setter
    def etat(self, valeur):
        self._etat = valeur

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valeur):
        self._disponible = valeur

    def est_en_bon_etat(self):
        return self._etat == ETAT_BON
