
from datetime import date

class Membre:
    def __init__(self, id_membre, nom, fin_abonnement, eligible=True):
        self._id = id_membre
        self._nom = nom
        self._fin_abonnement = fin_abonnement
        self._eligible = eligible

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
    def fin_abonnement(self):
        return self._fin_abonnement

    @fin_abonnement.setter
    def fin_abonnement(self, valeur):
        self._fin_abonnement = valeur

    @property
    def eligible(self):
        return self._eligible

    @eligible.setter
    def eligible(self, valeur):
        self._eligible = valeur

    def abonnement_valide(self):
        return self._fin_abonnement >= date.today()