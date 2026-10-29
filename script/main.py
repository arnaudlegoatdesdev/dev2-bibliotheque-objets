from data_factice import data
from consultation import afficher_precis_objets, afficher_tout_objets, rechercher_objet
import argparse

parser = argparse.ArgumentParser(
    description="Consulte le catalogue de La Remise"
)

parser.add_argument(
    "-r",
    "--recherche"
)

args = parser.parse_args()

if args.recherche is None:
    afficher_tout_objets(data["objets"])
else:
    resultats = rechercher_objet(data["objets"], args.recherche)

    if resultats:
        afficher_tout_objets(resultats)
    else:
        print("Aucun objet trouvé")