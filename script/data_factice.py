from modeles import Objet, Membre, Emprunt
from datetime import date, timedelta

aujourdhui = date.today()

objets = [
    Objet(1, "marteau", "reparation", "bon", disponible=False),
    Objet(2, "tournevis", "reparation", "bon", disponible=True),
    Objet(3, "jeu d’échecs", "jeux_société", "usure normale", disponible=True),
    Objet(4, "perceuse", "reparation", "bon", disponible=False),
    Objet(5, "ponceuse", "reparation", "usure normale", disponible=False),
    Objet(6, "sac de couchage", "camping", "bon", disponible=False),
    Objet(7, "lampe de camping", "camping", "bon", disponible=False),
    Objet(8, "matelas de camping", "camping", "bon", disponible=True),
    Objet(9, "appareil à raclette", "cuisine", "endommagé", disponible=False),
    Objet(10, "mixeur", "cuisine", "incomplet", disponible=False),
    Objet(11, "râteau", "jardin", "bon", disponible=True),
    Objet(12, "jeu de société", "jeux_société", "bon", disponible=True)
]

membres = [
    Membre(1, "Delave", "Alice", "1 rue Fictive", "0000000001", "alice@example.com", aujourdhui + timedelta(days=365), "réduit"),
    Membre(2, "Martin", "Benoît", "2 rue Fictive", "0000000002", "benoit@example.com", aujourdhui + timedelta(days=180), "plein"),
    Membre(3, "Durand", "Clara", "3 rue Fictive", "0000000003", "clara@example.com", aujourdhui - timedelta(days=1), "plein"),
    Membre(4, "Petit", "David", "4 rue Fictive", "0000000004", "david@example.com", aujourdhui + timedelta(days=365), "plein"),
    Membre(5, "Moreau", "Emma", "5 rue Fictive", "0000000005", "emma@example.com", aujourdhui + timedelta(days=90), "réduit"),
    Membre(6, "Leroy", "Farid", "6 rue Fictive", "0000000006", "farid@example.com", aujourdhui + timedelta(days=30), "plein")
]

emprunts = [
    Emprunt(1, objets[0], membres[0], aujourdhui - timedelta(days=2), aujourdhui + timedelta(days=5)),
    Emprunt(2, objets[6], membres[0], aujourdhui - timedelta(days=1), aujourdhui + timedelta(days=6)),
    Emprunt(3, objets[3], membres[1], aujourdhui - timedelta(days=3), aujourdhui + timedelta(days=4)),
    Emprunt(4, objets[4], membres[1], aujourdhui - timedelta(days=4), aujourdhui + timedelta(days=3)),
    Emprunt(5, objets[5], membres[1], aujourdhui - timedelta(days=5), aujourdhui + timedelta(days=2)),
    Emprunt(6, objets[8], membres[5], aujourdhui - timedelta(days=15), aujourdhui - timedelta(days=8), date_retour_reelle=aujourdhui - timedelta(days=10), etat_retour="endommagé"),
    Emprunt(7, objets[9], membres[4], aujourdhui - timedelta(days=14), aujourdhui - timedelta(days=7), date_retour_reelle=aujourdhui - timedelta(days=9), etat_retour="incomplet"),
    Emprunt(8, objets[2], membres[3], aujourdhui - timedelta(days=12), aujourdhui - timedelta(days=5), date_retour_reelle=aujourdhui - timedelta(days=7), etat_retour="usure normale"),
    Emprunt(9, objets[11], membres[5], aujourdhui - timedelta(days=10), aujourdhui - timedelta(days=3), date_retour_reelle=aujourdhui - timedelta(days=5), etat_retour="bon")
]

data = {
    "objets" : objets,
    "membres" : membres,
    "emprunts" : emprunts
}