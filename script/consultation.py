def afficher_dispo(val):
    if val:
        return "Disponible"
    else:
        return "Indisponible"

def afficher_objets(objets):
    print(f"ID : {objets.id_obj}, Nom : {objets.nom}, Catégorie : {objets.categorie}, État : {objets.etat}, Disponibilité : {afficher_dispo(objets.disponible)}")
