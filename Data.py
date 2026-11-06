from datetime import date, timedelta

from Models.membre import Membre
from Models.objet import Objet
from Models.emprunt import Emprunt
from Models.etat import ETAT_BON, ETAT_ENDOMMAGE, ETAT_INCOMPLET

def charger_donnees():
    aujourdhui = date.today()

    membres = [
        Membre(1, "Alice Dupont", aujourdhui + timedelta(days=200)),
        Membre(2, "Bruno Martin", aujourdhui - timedelta(days=30)),
        Membre(3, "Chloé Lambert", aujourdhui + timedelta(days=90), eligible=False),
        Membre(4, "David Petit", aujourdhui + timedelta(days=365)),
    ]

    objets = [
        Objet(1, "Perceuse", "Perceuse sans fil avec 2 batteries", ETAT_BON),
        Objet(2, "Échelle", "Échelle aluminium 3 mètres", ETAT_BON),
        Objet(3, "Tondeuse", "Tondeuse électrique", ETAT_BON),
        Objet(4, "Projecteur", "Projecteur vidéo HD", ETAT_ENDOMMAGE),
        Objet(5, "Tente", "Tente 4 places (piquets manquants)", ETAT_INCOMPLET),
    ]

    echelle = objets[1]
    echelle.disponible = False
    emprunts = [Emprunt(1, membres[0], echelle, aujourdhui - timedelta(days=3))]

    return membres, objets, emprunts