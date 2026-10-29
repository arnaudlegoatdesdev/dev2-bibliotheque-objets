class Objet:
    def __init__(self, id_obj, nom, categorie, etat="bon", disponible=True):
        self.id_obj = id_obj
        self.nom = nom
        self.categorie = categorie
        self.etat = etat # utilisez les valeurs : incomplet, endommagé, usure normale, bon
        self.disponible = disponible

class Membre:
    def __init__(self, id_mem, nom, prenom, adresse, telephone, email, date_fin_abonnement, type_abonnement="plein"):
        self.id_mem = id_mem
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.telephone = telephone
        self.email = email
        self.date_fin_abonnement = date_fin_abonnement
        self.type_abonnement = type_abonnement # utilisez les valeurs : plein, réduit

class Emprunt:
    def __init__(self, id_emp, obj_emprunter, membre_emprunt, date_emprunt, date_retour_prevu, date_retour_reelle=None, etat_retour=None):
        self.id_emp = id_emp
        self.obj_emprunter = obj_emprunter
        self.membre_emprunt = membre_emprunt
        self.date_emprunt = date_emprunt
        self.date_retour_prevu = date_retour_prevu
        self.date_retour_reelle = date_retour_reelle
        self.etat_retour = etat_retour
