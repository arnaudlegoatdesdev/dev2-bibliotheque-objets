from datetime import date
from Models.objet import Objet
from Models.emprunt import Emprunt
from Models.etat import ETAT_BON, ETATS


class ErreurMetier(Exception):
    """Erreur affichable à l'utilisateur (membre introuvable, objet indisponible...)."""


class GestionMembres:
    def __init__(self, membres):
        self._membres = membres

    def lister(self):
        return list(self._membres)

    def trouver(self, id_membre):
        for membre in self._membres:
            if membre.id == id_membre:
                return membre
        return None

    def verifier_abonnement(self, id_membre):
        membre = self.trouver(id_membre)
        if membre is None:
            raise ErreurMetier("Membre introuvable.")
        return membre

    def verifier_pour_emprunt(self, id_membre):
        membre = self.verifier_abonnement(id_membre)
        if not membre.abonnement_valide():
            raise ErreurMetier("L'abonnement du membre n'est plus valide.")
        if not membre.eligible:
            raise ErreurMetier("Le membre n'est pas éligible à l'emprunt.")
        return membre


class GestionCatalogue:
    def __init__(self, objets):
        self._objets = objets
        self._prochain_id = max((o.id for o in objets), default=0) + 1

    def lister(self):
        return list(self._objets)

    def trouver(self, id_objet):
        for objet in self._objets:
            if objet.id == id_objet:
                return objet
        return None

    def _obtenir(self, id_objet):
        objet = self.trouver(id_objet)
        if objet is None:
            raise ErreurMetier("Objet introuvable.")
        return objet

    def ajouter(self, nom, description, etat=ETAT_BON):
        objet = Objet(self._prochain_id, nom, description, etat)
        self._prochain_id += 1
        self._objets.append(objet)
        return objet

    def modifier_infos(self, id_objet, nom, description):
        objet = self._obtenir(id_objet)
        if nom:
            objet.nom = nom
        if description:
            objet.description = description
        return objet

    def modifier_etat(self, id_objet, etat):
        if etat not in ETATS:
            raise ErreurMetier("État inconnu.")
        objet = self._obtenir(id_objet)
        objet.etat = etat
        return objet

    def verifier_disponibilite(self, id_objet):
        return self._obtenir(id_objet)

    def retirer(self, id_objet):
        objet = self._obtenir(id_objet)
        if not objet.disponible:
            raise ErreurMetier("Impossible de retirer un objet actuellement emprunté.")
        self._objets.remove(objet)
        return objet

    def verifier_pour_emprunt(self, id_objet):
        objet = self._obtenir(id_objet)
        if not objet.disponible:
            raise ErreurMetier("Objet déjà emprunté.")
        if not objet.est_en_bon_etat():
            raise ErreurMetier(f"Objet non prêtable (état : {objet.etat}).")
        return objet


class GestionEmprunts:
    def __init__(self, gestion_membres, catalogue, emprunts):
        self._membres = gestion_membres
        self._catalogue = catalogue
        self._emprunts = emprunts
        self._prochain_id = max((e.id for e in emprunts), default=0) + 1

    def lister(self, en_cours_seulement=False):
        if en_cours_seulement:
            return [e for e in self._emprunts if e.en_cours]
        return list(self._emprunts)

    def _obtenir_en_cours(self, id_emprunt):
        for emprunt in self._emprunts:
            if emprunt.id == id_emprunt:
                if not emprunt.en_cours:
                    raise ErreurMetier("Cet emprunt est déjà clôturé.")
                return emprunt
        raise ErreurMetier("Emprunt introuvable.")

    def ajouter(self, id_membre, id_objet):
        membre = self._membres.verifier_pour_emprunt(id_membre)
        objet = self._catalogue.verifier_pour_emprunt(id_objet)
        emprunt = Emprunt(self._prochain_id, membre, objet)
        self._prochain_id += 1
        objet.disponible = False
        self._emprunts.append(emprunt)
        return emprunt

    def enregistrer_retour(self, id_emprunt, nouvel_etat=None):
        emprunt = self._obtenir_en_cours(id_emprunt)
        emprunt.date_retour = date.today()
        emprunt.objet.disponible = True
        if nouvel_etat:
            emprunt.objet.etat = nouvel_etat
        return emprunt