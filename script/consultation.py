def afficher_dispo(val):
    if val:
        return "Disponible"
    else:
        return "Indisponible"

def afficher_precis_objets(objet):
    print(f"ID : {objet.id_obj}, Nom : {objet.nom}, Catégorie : {objet.categorie}, État : {objet.etat}, Disponibilité : {afficher_dispo(objet.disponible)}")

def afficher_tout_objets(objets):
        for objet in objets:
           print(f"ID : {objet.id_obj}, Nom : {objet.nom}, Catégorie : {objet.categorie}, État : {objet.etat}, Disponibilité : {afficher_dispo(objet.disponible)}")

def rechercher_objet(objet, texte):
    resultat = []

    for i in objet:
        if str.lower(texte) in i.nom.lower():
            resultat.append(i)
        else:
            pass

    return resultat