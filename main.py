from Data import charger_donnees
from Models.etat import ETATS
from Services import ErreurMetier, GestionMembres, GestionCatalogue, GestionEmprunts

_membres, _objets, _emprunts = charger_donnees()
gestion_membres = GestionMembres(_membres)
catalogue = GestionCatalogue(_objets)
gestion_emprunts = GestionEmprunts(gestion_membres, catalogue, _emprunts)


def titre(texte):
    print("\n" + "=" * 60)
    print(texte.center(60))
    print("=" * 60)


def pause():
    input("\nAppuyez sur Entrée pour continuer...")


def lire_texte(invite, obligatoire=True):
    while True:
        texte = input(invite).strip()
        if texte or not obligatoire:
            return texte
        print("Ce champ est obligatoire.")


def lire_entier(invite, obligatoire=True):
    while True:
        texte = input(invite).strip()
        if not texte and not obligatoire:
            return None
        if texte.isdigit():
            return int(texte)
        print("Veuillez entrer un nombre.")


def lire_etat(invite, obligatoire=True):
    for i, etat in enumerate(ETATS, 1):
        print(f"  {i}. {etat}")
    while True:
        choix = input(invite).strip()
        if not choix and not obligatoire:
            return None
        if choix.isdigit() and 1 <= int(choix) <= len(ETATS):
            return ETATS[int(choix) - 1]
        print("Choix invalide.")


def afficher_membres(membres):
    print(f"{'ID':<4}{'Nom':<20}{'Fin abonnement':<16}{'Abonnement':<12}Éligible")
    for m in membres:
        valide = "Valide" if m.abonnement_valide() else "Expiré"
        eligible = "Oui" if m.eligible else "Non"
        print(f"{m.id:<4}{m.nom:<20}{m.fin_abonnement:%d/%m/%Y}      {valide:<12}{eligible}")


def afficher_objets(objets):
    print(f"{'ID':<4}{'Nom':<14}{'État':<12}{'Dispo':<8}Description")
    for o in objets:
        dispo = "Oui" if o.disponible else "Non"
        print(f"{o.id:<4}{o.nom:<14}{o.etat:<12}{dispo:<8}{o.description}")


def afficher_emprunts(emprunts):
    print(f"{'ID':<4}{'Membre':<18}{'Objet':<14}{'Emprunté le':<13}Retour")
    for e in emprunts:
        retour = f"{e.date_retour:%d/%m/%Y}" if e.date_retour else "En cours"
        print(f"{e.id:<4}{e.membre.nom:<18}{e.objet.nom:<14}{e.date_emprunt:%d/%m/%Y}   {retour}")


def afficher_liste_membres():
    afficher_membres(gestion_membres.lister())


def verifier_abonnement_membre():
    afficher_membres(gestion_membres.lister())
    membre = gestion_membres.verifier_abonnement(lire_entier("\nID du membre : "))
    if membre.abonnement_valide():
        print(f" L'abonnement de {membre.nom} est valide jusqu'au {membre.fin_abonnement:%d/%m/%Y}.")
    else:
        print(f" L'abonnement de {membre.nom} a expiré le {membre.fin_abonnement:%d/%m/%Y}.")


def consulter_catalogue():
    afficher_objets(catalogue.lister())


def ajouter_objet():
    nom = lire_texte("Nom de l'objet : ")
    description = lire_texte("Description : ")
    print("État de l'objet :")
    etat = lire_etat("Votre choix : ")
    objet = catalogue.ajouter(nom, description, etat)
    print(f" Objet « {objet.nom} » ajouté (ID {objet.id}).")


def modifier_infos_objet():
    afficher_objets(catalogue.lister())
    id_objet = lire_entier("\nID de l'objet à modifier : ")
    print("(Laissez vide pour conserver la valeur actuelle)")
    nom = lire_texte("Nouveau nom : ", obligatoire=False)
    description = lire_texte("Nouvelle description : ", obligatoire=False)
    objet = catalogue.modifier_infos(id_objet, nom, description)
    print(f" Objet mis à jour : {objet.nom} - {objet.description}")


def modifier_etat_objet():
    afficher_objets(catalogue.lister())
    id_objet = lire_entier("\nID de l'objet : ")
    print("Nouvel état :")
    etat = lire_etat("Votre choix : ")
    objet = catalogue.modifier_etat(id_objet, etat)
    print(f" « {objet.nom} » est maintenant : {objet.etat}.")


def verifier_disponibilite_objet():
    afficher_objets(catalogue.lister())
    objet = catalogue.verifier_disponibilite(lire_entier("\nID de l'objet : "))
    if objet.disponible:
        print(f" « {objet.nom} » est disponible.")
    else:
        print(f" « {objet.nom} » est actuellement emprunté.")


def retirer_objet():
    afficher_objets(catalogue.lister())
    objet = catalogue.retirer(lire_entier("\nID de l'objet à retirer : "))
    print(f"« {objet.nom} » a été retiré du catalogue.")


def ajouter_emprunt():
    # Étapes 1-2 du diagramme : le formulaire affiche membres et objets
    print("--- Membres ---")
    afficher_membres(gestion_membres.lister())
    print("\n--- Objets ---")
    afficher_objets(catalogue.lister())
    # Étapes 3-4 : sélection puis validation
    id_membre = lire_entier("\nID du membre : ")
    id_objet = lire_entier("ID de l'objet : ")
    # Étapes 4-6 : vérifications et enregistrement (dans le service)
    emprunt = gestion_emprunts.ajouter(id_membre, id_objet)
    # Étape 7 : confirmation
    print(f"Emprunt n°{emprunt.id} enregistré : {emprunt.objet.nom} "
          f"prêté à {emprunt.membre.nom} le {emprunt.date_emprunt:%d/%m/%Y}.")


def afficher_liste_emprunts():
    afficher_emprunts(gestion_emprunts.lister())


def enregistrer_retour():
    en_cours = gestion_emprunts.lister(en_cours_seulement=True)
    if not en_cours:
        print("Aucun emprunt en cours.")
        return
    afficher_emprunts(en_cours)
    id_emprunt = lire_entier("\nID de l'emprunt à clôturer : ")
    print("État de l'objet au retour (vide = inchangé) :")
    etat = lire_etat("Votre choix : ", obligatoire=False)
    emprunt = gestion_emprunts.enregistrer_retour(id_emprunt, etat)
    print(f"Retour enregistré : « {emprunt.objet.nom} » est de nouveau disponible.")


def menu(titre_menu, options, sortie="Retour"):
    """Affiche un menu numéroté et exécute l'action choisie, en boucle."""
    while True:
        titre(titre_menu)
        for i, (libelle, _) in enumerate(options, 1):
            print(f"  {i}. {libelle}")
        print(f"  0. {sortie}")
        choix = input("\nVotre choix : ").strip()
        if choix == "0":
            return
        if choix.isdigit() and 1 <= int(choix) <= len(options):
            print()
            try:
                options[int(choix) - 1][1]()
            except ErreurMetier as erreur:
                print(f"{erreur}")
            pause()
        else:
            print("Choix invalide.")


def main():
    menu_membres = [
        ("Afficher la liste des membres", afficher_liste_membres),
        ("Vérifier l'abonnement d'un membre", verifier_abonnement_membre),
    ]
    menu_catalogue = [
        ("Consulter la liste des objets", consulter_catalogue),
        ("Ajouter un objet", ajouter_objet),
        ("Modifier les informations d'un objet", modifier_infos_objet),
        ("Modifier l'état d'un objet", modifier_etat_objet),
        ("Vérifier la disponibilité d'un objet", verifier_disponibilite_objet),
        ("Retirer un objet du catalogue", retirer_objet),
    ]
    menu_emprunts = [
        ("Ajouter un nouvel emprunt", ajouter_emprunt),
        ("Afficher la liste des emprunts", afficher_liste_emprunts),
        ("Enregistrer un retour d'objet", enregistrer_retour),
    ]
    menu_principal = [
        ("Gérer les membres", lambda: menu("GÉRER LES MEMBRES", menu_membres)),
        ("Gérer le catalogue d'objets", lambda: menu("GÉRER LE CATALOGUE", menu_catalogue)),
        ("Gérer les emprunts et les retours", lambda: menu("EMPRUNTS ET RETOURS", menu_emprunts)),
    ]
    menu("BIBLIOTHÈQUE D'OBJETS - MENU PRINCIPAL", menu_principal, sortie="Quitter")
    print("\nAu revoir !")


if __name__ == "__main__":
    main()