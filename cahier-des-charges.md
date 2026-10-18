# Cahier des charges - Bibliothèque d'objets

## Informations sur le document

### Titre :
    Cahier des charges - Bibliothèque d'objets
### Auteurs du document :
    Groupe 2TL1-6
### Validation du projet par le client

### Historique des versions
| Version | Date | Modification     |
|:--------|:-----|:-----------------|
| v0.1    |      | Version Initiale |
## Convention d'identification
| Element                    | Format  | Exemple |
|:---------------------------|:--------|:--------|
| Règle métier               | RM-xx   | RM-01   |
| Donnée                     | D-xx    | D-02    |
| Fonctionnalité             | F-xx    | F-03    |
| Exigence fonctionnelle     | EF-xx.y | EF-04.1 |
| Exigence non fonctionnelle | ENF-xx  | ENF-05  |
| Livrable                   | L-xx    | L-06    |
| Question ouverte           | Q-xx    | Q-07    |

### Table des matières
1. Contexte
2. Description générale
3. Exigences
4. Contraintes
5. Budget
6. Livrables et Planning
7. Validation du projet
8. Maintenance
9. Questions ouvertes
10. Glossaire

## 1. Contexte

### 1.1. Présentation du client

- La Remise est une bibliothèque d'objets située à Etterbeek. Elle permet à ses membres d'emprunter des objets spécifiques du quotidien plutôt que de devoir les acheter. Son catalogue compte environ 350 objets répartis en 12 catégories, telles que bricolage, jardin, cuisine et plus.

- Notre cliente pour ce projet est Nadia Pereira, cofondatrice bénévole de la Remise. La bibliothèque fonctionne avec une équipe de six bénévoles qui travaillent au même niveau et qui s'assureront des permanences. Ils accueillent les membres, ajoutent et modifient les fiches du catalogue et enregistrent les emprunts et les retours.

- La Remise compte environ 120 membres qui paient un abonnement annuel. Deux formules d'abonnements sont présents, une formule plein tarif et une à tarif réduit. Il faut noter que le contact humain est très important selon notre cliente, les discussions entre membres et les réunions sont à conserver et ne doivent pas être digitalisées.

### 1.2. Présentation du projet

- Actuellement, La Remise utilise Airtable en version gratuite pour gérer son catalogue, mais cet outil commence à saturer. Les emprunts et les réservations sont enregistrés dans un tableur séparé d'Airtable ce qui rend le suivi peu fiable.

- Cette organisation ne permet pas de connaitre facilement et de manière fiable la disponibilité et l'état des objets. Certains dégâts sont découverts seulement lors de l'emprunt suivant. Le suivi de l'entretien et de l'historique des objets reste insuffisant, notamment pour les kits composés de plusieurs pièces.

- Le projet consiste à remplacer ces outils par une application unique regroupant le catalogue, les membres, les emprunts et les réservations. Elle doit faciliter le travail quotidien des bénévoles et leur faire gagner du temps ainsi qu'améliorer le suivi des objets.

### 1.3. Objectifs du projet

- Centraliser le catalogue, les membres, les emprunts et les réservations dans une seule application afin que les bénévoles n'aient plus à utiliser Airtable et le tableur externe de manière fastidieuse.

- Permettre aux bénévoles de connaitre la disponibilité et l'état d'un objet avant de le prêter, afin d'éviter de proposer un objet déjà emprunté en réparation ou réservé.

- Faciliter le contrôle des objets au retour, notamment grâce à la liste des pièces de certains kits, pour repérer les dégâts et les éléments manquants avant l'emprunt suivant.

- Permettre de retrouver l'historique des emprunts et des incidents de chaque objet afin d'identifier les problèmes récurrents ou les incidents associés à un membre.

## 2. Description générale

### 2.1. Vue d'ensemble du produit et de son environnement

- L'application servira d'outil de gestion aux bénévoles pendants les permanences. Elle remplacera Airtable pour le catalogue et le tableur utilisé pour les emprunts, les retours et les réservations.

- Elle sera principalement utilisée sur l'ordinateur portable du local, qui dispose d'une connexion internet fonctionnant généralement bien.

- Le catalogue existant devra être repris au démarrage de l'application, avec les objets, leurs catégories, leurs photos et leur disponibilité. Le catalogue papier affiché au local sera conservé.

### 2.2. Profils utilisateurs

- **Bénévoles de permanence** : les six bénévoles sont les principaux utilisateurs de l'application. Ils gèrent le catalogue, les membres, les réservations, les emprunts et les retours, ainsi que l'état des objets et les cautions. Ils disposent des mêmes accès. N'ayant pas de connaissances techniques particulières, ils ont besoin d'un outil simple à utiliser pendant les permanences.

- **Membres** : la bibliothèque compte environ 120 membres disposant d'un abonnement annuel. La cliente souhaite qu'ils puissent consulter le catalogue pendant les permanences. Les opérations de gestion restent effectuées par les bénévoles. La consultation à distance et la reservation autonome par les membres est évoquée comme une possibilitée plus tard, mais la cliente n'est pas encore décidé.

### 2.3. Périmètre

### 2.4. Règles métier

### 2.5. Données

## 3. Exigences

### 3.1. Exigences fonctionnelles

#### Vue d'ensemble et MVP

Pour le système de gestion d'une bibliothèque d'objets, les exigences fonctionnelles sont organisées autour des fonctionnalités principales du logiciel. Chaque fonctionnalité est identifiée par un identifiant unique (**F-xx**), tandis que ses exigences détaillées utilisent la convention **EF-xx.y**.

#### Vue d'ensemble des fonctionnalités

| ID       | Fonctionnalité                                                 | Acteur(s)         | Priorité      | 
|----------|----------------------------------------------------------------|-------------------|---------------| 
| **F-01** | Gérer les membres                                              | Bénévole          | Indispensable | 
| **F-02** | Gérer les comptes utilisateurs                                 | Administrateur    | Indispensable | 
| **F-03** | Gérer le catalogue des objets                                  | Bénévole, Système | Indispensable | 
| **F-04** | Gérer les types d'objets                                       | Bénévole          | Indispensable | 
| **F-05** | Gérer les formules d'abonnement                                | Bénévole          | Indispensable | 
| **F-06** | Gérer les abonnements des membres                              | Bénévole          | Indispensable | 
| **F-07** | Gérer les réservations d'objets                                | Bénévole          | Indispensable | 
| **F-08** | Gérer les emprunts et les retours                              | Bénévole          | Indispensable | 
| **F-09** | Envoyer les notifications relatives aux abonnements par e-mail | Bénévole, Système | Souhaitable   | 
| **F-10** | Envoyer les confirmations de réservation par e-mail            | Bénévole, Système | Souhaitable   | 
| **F-11** | Envoyer les reçus d'emprunt par e-mail                         | Bénévole, Système | Souhaitable   | 
| **F-12** | Envoyer des rappels par e-mail de retour des objets empruntés  | Bénévole, Système | Souhaitable   | 

#### Vue d'ensemble du MVP

Le MVP (*Minimum Viable Product*) sera centré sur les fonctionnalités indispensables au fonctionnement de la bibliothèque. Il permettra au Bénévole et/ou à l’Administrateur de gérer :

* Les membres
* Les comptes utilisateurs
* Le catalogue des objets et leurs types
* Les formules d'abonnement et les abonnements des membres
* Les réservations, les emprunts et les retours d’objets

Il permettra également d'enregistrer les réservations, les emprunts et les retours d'objets afin d'assurer le suivi de leur disponibilité et de leur état physique.

Les fonctionnalités de notification automatique et d'envoi de reçus par e-mail pourront être intégrées dans une version ultérieure, selon le périmètre retenu et la validation de Madame Pereira.

Les fonctionnalités **F-01** à **F-08** sont détaillées ci-dessous sous forme d'exigences fonctionnelles. Les fonctionnalités **F-09** à **F-12** seront précisées ultérieurement, notamment en ce qui concerne les délais d'envoi, les événements déclencheurs et les canaux de notification.

### Détail des exigences fonctionnelles (MVP)

#### F-01 : Gérer les membres

Le bénévole peut enregistrer les membres de la bibliothèque, modifier leurs informations, consulter leurs dossiers et retrouver des membres à l'aide de critères de recherche, de tri et de filtrage.

* **EF-01.1** : Le bénévole peut ajouter un membre en renseignant les informations nécessaires à son identification, notamment son nom, son prénom et ses coordonnées.
* **EF-01.2** : Le système refuse la création d'un membre lorsque les champs obligatoires ne sont pas renseignés.
  * *Critère d'acceptation* : Le bénévole tente d'enregistrer un membre sans nom. L'enregistrement est refusé et le système signale le champ manquant.
* **EF-01.3** : Le système attribue un identifiant unique à chaque membre enregistré.
  * *Critère d'acceptation* : Deux membres peuvent porter le même nom, mais ils possèdent des identifiants différents.
* **EF-01.4** : Le bénévole peut modifier les informations d'un membre existant.
  * *Critère d'acceptation* : Le bénévole modifie le numéro de téléphone d'un membre. Les nouvelles informations sont enregistrées.
* **EF-01.5** : Le bénévole peut consulter et imprimer la liste des membres ainsi que les informations détaillées de chaque membre.
* **EF-01.6** : Le bénévole peut trier et filtrer la liste des membres selon des critères tels que le nom, le prénom, la formule d’abonnement ou le statut du membre.
* **EF-01.7** : Le système empêche la création d'un doublon lorsque les informations utilisées pour identifier un membre sont déjà associées à un dossier existant, selon les règles d'unicité définies.
  * *Critère d'acceptation* : Si une adresse e-mail doit être unique, la création d'un second membre avec la même adresse est refusée.
* **EF-01.8** : Le système permet de consulter les abonnements, réservations et emprunts associés à un membre.

> **Données impliquées** : D-01 (données du membre), D-06 (données des abonnements), D-07 (données des réservations), D-08 (données des emprunts).

#### F-02 : Gérer les comptes utilisateurs

L'administrateur peut créer, modifier, consulter et désactiver les comptes permettant aux utilisateurs autorisés d'accéder au système.

* **EF-02.1** : L'administrateur peut créer un compte utilisateur en renseignant les informations nécessaires à sa connexion, notamment une adresse e-mail et un mot de passe initial ou un mécanisme de définition du mot de passe.
* **EF-02.2** : Le système associe un identifiant unique à chaque compte utilisateur.
* **EF-02.3** : Le système refuse la création d'un compte si l'adresse e-mail utilisée est déjà associée à un autre compte.
  * *Critère d'acceptation* : Si le compte `admin@bibliotheque.be` existe déjà, la création d'un second compte avec cette adresse est refusée.
* **EF-02.4** : L'administrateur peut modifier les informations d'un compte utilisateur.
* **EF-02.5** : L'administrateur peut consulter et imprimer la liste des comptes utilisateurs et leurs informations.
* **EF-02.6** : L'administrateur peut désactiver un compte utilisateur.
  * *Critère d'acceptation* : Lorsqu'un compte est désactivé, son titulaire ne peut plus ouvrir de session avec ce compte.
* **EF-02.7** : Le système distingue les rôles des utilisateurs, notamment administrateur et bénévole, afin de limiter l'accès aux fonctionnalités selon les autorisations accordées.
* **EF-02.8** : Le système interdit l'accès aux fonctionnalités réservées à l'administrateur aux utilisateurs disposant uniquement du rôle de bénévole.

> **Données impliquées** : D-02 (données du compte utilisateur).

#### F-03 : Gérer le catalogue des objets

Le bénévole peut enregistrer et gérer les objets physiques mis à disposition des membres. Chaque exemplaire physique doit être identifiable individuellement, même lorsque plusieurs exemplaires appartiennent au même modèle.

* **EF-03.1** : Le bénévole peut ajouter un objet au catalogue en renseignant ses informations, notamment son nom, sa description, son type et, si nécessaire, sa marque et son modèle.
* **EF-03.2** : Le système attribue un identifiant unique à chaque exemplaire physique enregistré dans le catalogue.
  * *Critère d'acceptation* : La bibliothèque possède trois perceuses identiques. Le système permet d'enregistrer les trois exemplaires séparément, chacun avec son propre identifiant.
* **EF-03.3** : Le système refuse l'enregistrement d'un exemplaire si son identifiant unique existe déjà.
* **EF-03.4** : Le bénévole peut modifier les informations d'un objet existant, sans modifier son identité.
* **EF-03.5** : Le bénévole peut mettre à jour l'état physique d'un objet : bon état, usure normale, endommagé ou incomplet.
  * *Critère d'acceptation* : Le bénévole signale qu'une perceuse est endommagée. Le nouvel état est enregistré pour cet exemplaire précis.
* **EF-03.6** : Le système distingue l'état physique d'un objet de sa disponibilité.
  * *Critère d'acceptation* : Une perceuse peut être en bon état tout en étant empruntée. Son état physique reste « bon état » et sa disponibilité est « emprunté ».
* **EF-03.7** : Le bénévole peut retirer un exemplaire du catalogue afin qu'il ne soit plus proposé à la réservation ou à l'emprunt.
  * *Critère d'acceptation* : Un objet retiré ne peut plus faire l'objet d'un nouvel emprunt.
* **EF-03.8** : Le système conserve les informations nécessaires à la traçabilité des objets retirés qui possèdent un historique d'emprunts ou de réservations.
* **EF-03.9** : Le bénévole peut consulter et imprimer la liste des objets et leurs informations détaillées.
* **EF-03.10** : Le système permet de rechercher, trier et filtrer les objets selon des critères tels que le nom, le type, l'état physique ou la disponibilité.
* **EF-03.11** : Le système met à jour la disponibilité d'un exemplaire en fonction des opérations de réservation, d'emprunt, de retour et de retrait du catalogue.
* **EF-03.12** : Le bénévole peut associer à chaque objet une catégorie de valeur parmi les catégories A, B, C et D.
* **EF-03.13** : Le bénévole peut consulter la catégorie de valeur et en déduire le montant de la caution associé à chaque objet.

> **Données impliquées** : D-03 (données des objets), D-04 (données des types d'objets), D-07 (données des réservations), D-08 (données des emprunts).

#### F-04 : Gérer les types d'objets

Le bénévole peut organiser les objets en catégories afin de faciliter leur classement, leur recherche et leur consultation.

* **EF-04.1** : Le bénévole peut créer un type d'objet en renseignant son nom et, éventuellement, une description.
* **EF-04.2** : Le système attribue un identifiant unique à chaque type d'objet.
* **EF-04.3** : Le système refuse la création de deux types portant le même nom lorsque l'unicité du nom est requise.
  * *Critère d'acceptation* : Si le type « Jardinage » existe déjà, la création d'un second type portant ce nom est refusée.
* **EF-04.4** : Le bénévole peut modifier les informations d'un type d'objet existant.
* **EF-04.5** : Le bénévole peut consulter et imprimer la liste des types d'objets et leurs détails.
* **EF-04.6** : Le système permet d'associer un exemplaire du catalogue à un type d'objet existant.
* **EF-04.7** : Le système empêche la suppression ou la désactivation d'un type encore utilisé par des objets, sauf si les objets concernés sont réaffectés à un autre type ou si une règle de gestion prévoit une autre solution.

> **Données impliquées** : D-04 (données des types d'objets), D-03 (données des objets).

#### F-05 : Gérer les formules d'abonnement

Le bénévole peut définir et gérer les formules d'abonnement proposées par la bibliothèque, en précisant leurs caractéristiques et les conditions d'utilisation.

* **EF-05.1** : Le bénévole peut créer une formule d'abonnement en renseignant son nom, sa durée, son prix et les conditions associées.
* **EF-05.2** : Le système attribue un identifiant unique à chaque formule d'abonnement.
* **EF-05.3** : Le système refuse la création d'une formule si les informations obligatoires sont absentes ou si les valeurs renseignées ne respectent pas les règles de validation.
  * *Critère d'acceptation* : Une formule dont le prix est négatif est refusée.
* **EF-05.4** : Le bénévole peut modifier les caractéristiques d'une formule existante.
* **EF-05.5** : Le bénévole peut désactiver une formule afin qu'elle ne soit plus proposée aux nouveaux abonnés.
* **EF-05.6** : Le système conserve les informations historiques des abonnements souscrits à une formule désactivée.
* **EF-05.7** : Le bénévole peut consulter et imprimer la liste des formules d'abonnement et leurs détails.
* **EF-05.8** : Le bénévole définit les avantages et les limites associés à chaque formule, notamment le nombre maximal d'objets pouvant être empruntés simultanément.

> **Données impliquées** : D-05 (données des formules d'abonnement), D-06 (données des abonnements).

#### F-06 : Gérer les abonnements des membres

Le bénévole peut souscrire et gérer les abonnements des membres, en assurant le suivi de leur période de validité et de leur statut.

* **EF-06.1** : Le bénévole peut créer un abonnement pour un membre existant en sélectionnant une formule d'abonnement active.
* **EF-06.2** : Le système associe chaque abonnement à un membre et à une formule d'abonnement en fonction des exigences du bénévole.
* **EF-06.3** : Le système enregistre la date de début, la date de fin et le statut de l'abonnement.
* **EF-06.4** : Le système refuse la création d'un abonnement lorsque le membre ou la formule sélectionnée n'existe pas.
* **EF-06.5** : Le système vérifie que la date de fin de l'abonnement est postérieure à sa date de début.
  * *Critère d'acceptation* : Un abonnement commençant le 1er novembre ne peut pas se terminer le 30 octobre de la même année.
* **EF-06.6** : Le bénévole peut modifier les informations d'un abonnement existant, conformément aux règles de gestion.
* **EF-06.7** : Le bénévole peut suspendre un abonnement.
* **EF-06.8** : Le système distingue les différents statuts d'un abonnement, notamment actif, suspendu et expiré.
* **EF-06.9** : Le système permet de consulter et d’imprimer la liste des abonnements et leurs détails, avec la possibilité de filtrer par membre, formule ou statut.
* **EF-06.10** : Le système vérifie la validité de l'abonnement d'un membre avant de lui permettre d'effectuer une opération soumise à cette condition.
  * *Critère d'acceptation* : Si un abonnement expiré interdit les emprunts, le système refuse un nouvel emprunt pour le membre concerné.
* **EF-06.11** : Le système conserve l'historique des abonnements d'un membre, y compris les abonnements expirés ou suspendus.

> **Données impliquées** : D-01 (données du membre), D-05 (données des formules d'abonnement), D-06 (données des abonnements).

#### F-07 : Gérer les réservations d'objets

Les membres peuvent réserver les objets proposés par la bibliothèque, sous réserve de respecter les conditions de réservation. Cette réservation peut se faire par appel ou en présentiel. Le bénévole se charge d’enregistrer, consulter et gérer les réservations.

* **EF-07.1** : Le bénévole peut créer une réservation en sélectionnant un exemplaire disponible du catalogue ou disponible à la période voulue par le membre.
* **EF-07.2** : Le système associe chaque réservation à un membre, à un exemplaire et à une date de réservation.
* **EF-07.3** : Le système vérifie que le membre remplit les conditions requises pour réserver un objet.
* **EF-07.4** : Le système refuse une réservation si l'exemplaire ne peut pas être réservé, notamment s'il est retiré du catalogue ou indisponible selon les règles de gestion.
  * *Critère d'acceptation* : Un exemplaire déjà emprunté ne peut pas être réservé si la bibliothèque n'autorise pas les réservations sur les objets empruntés.
* **EF-07.5** : Le système empêche la création de réservations incompatibles pour un même exemplaire, conformément aux règles de disponibilité.
* **EF-07.6** : Le bénévole peut consulter les informations relatives à ses réservations.
* **EF-07.7** : Le bénévole peut consulter et imprimer la liste des réservations de l'ensemble des membres.
* **EF-07.8** : Le bénévole peut modifier les informations d'une réservation, dans les limites des règles de gestion.
* **EF-07.9** : Le bénévole peut annuler une réservation.
* **EF-07.10** : Le système conserve le statut de chaque réservation, notamment en attente, confirmée, annulée ou terminée, selon le cycle de vie retenu.
* **EF-07.11** : Le système actualise la disponibilité de l'exemplaire en fonction du statut de la réservation.
* **EF-07.12** : Le système conserve l'historique des réservations afin de permettre leur consultation ultérieure.
* **EF-07.13** : Le système peut annuler une réservation si la date fixée pour l’emprunt est échue sans que le membre ne soit venu finaliser l’emprunt dans la bibliothèque.

> **Données impliquées** : D-01 (données du membre), D-03 (données des objets), D-06 (données des abonnements), D-07 (données des réservations).

#### F-08 : Gérer les emprunts et les retours

Le bénévole peut enregistrer les emprunts et les retours des objets physiques. Le système assure le suivi des dates, des membres concernés et de la disponibilité des exemplaires.

* **EF-08.1** : Le bénévole peut enregistrer l'emprunt d'un exemplaire par un membre.
* **EF-08.2** : Le système enregistre le membre concerné, l'exemplaire emprunté, la date d'emprunt et la date de retour prévue.
* **EF-08.3** : Le système vérifie que le membre dispose d'un abonnement valide lorsque celui-ci est requis pour emprunter un objet.
* **EF-08.4** : Le système vérifie que l'exemplaire peut être emprunté avant d'enregistrer l'opération.
  * *Critère d'acceptation* : Un exemplaire déjà emprunté ou indisponible dans la période voulu par le membre, retiré du catalogue ou indisponible à cause de son état ne peut pas faire l'objet d'un nouvel emprunt.
* **EF-08.5** : Le système vérifie que le membre ne dépasse pas le nombre maximal d'emprunts simultanés autorisé par sa formule d'abonnement, si cette limite est définie.
* **EF-08.6** : Le système enregistre le retour d'un exemplaire emprunté ainsi que la date effective du retour.
* **EF-08.7** : Lors du retour, le bénévole peut mettre à jour l'état physique de l'objet.
* **EF-08.8** : Le système actualise la disponibilité de l'exemplaire après son retour, en tenant compte de son état physique et des éventuelles réservations.
* **EF-08.9** : Le système permet de consulter l'historique des emprunts et des retours d'un membre ou d'un exemplaire.
* **EF-08.10** : Le système permet au bénévole de consulter et imprimer la liste des emprunts en cours, des emprunts terminés et des emprunts en retard.
* **EF-08.11** : Le système identifie un emprunt en retard lorsque la date de retour prévue est dépassée et que le retour effectif n'a pas été enregistré.
* **EF-08.12** : Le système conserve l'historique des emprunts terminés afin de préserver la traçabilité des objets.
* **EF-08.13** : Lors de l'emprunt, le système indique la catégorie de valeur de l'objet pour que le bénévole puisse en déduire le montant de la caution.
* **EF-08.14** : Lorsque la catégorie de l'objet prévoit une caution, le bénévole enregistre le paiement de celle-ci en liquide au moment de l'emprunt.
* **EF-08.15** : Lors du retour de l'objet, le bénévole enregistre la restitution de la caution au membre.
* **EF-08.16** : Si l'objet est abîmé, le bénévole peut retenir une partie ou la totalité de la caution, en indiquant une justification.
* **EF-08.17** : Le système conserve, pour chaque emprunt concerné, le montant de la caution perçu, le montant restitué, le montant éventuellement retenu et la justification de toute retenue.

> **Données impliquées** : D-01 (données du membre), D-03 (données des objets), D-06 (données des abonnements), D-07 (données des réservations), D-08 (données des emprunts).
#### Minimum Viable Product

### Fonctionnalités secondaires (Post-MVP)

#### F-09 : Notifier les membres à l'approche de l'expiration de leur abonnement

Le système informe automatiquement les membres lorsque leur abonnement approche de sa date d'expiration, afin de leur permettre de prendre les dispositions nécessaires pour le renouveler.

* **EF-09.1** : Le système identifie périodiquement les abonnements dont la date d'expiration approche.
* **EF-09.2** : Le système envoie une notification au membre concerné avant l'expiration de son abonnement.
  * *Critère d'acceptation* : Si l’e-mail du membre n’est pas enregistré dans le système, alors aucun rnotification ne lui sera envoyé.
* **EF-09.3** : La notification contient les informations essentielles de l'abonnement, notamment sa date d'expiration.
* **EF-09.4** : Le système permet de définir le délai précédant l'expiration auquel la notification doit être envoyée.
* **EF-09.5** : Le système évite d'envoyer plusieurs notifications identiques pour une même échéance, selon la fréquence définie.
* **EF-09.6** : Le système ne déclenche pas de rappel d'expiration pour un abonnement qui a été renouvelé ou dont le statut ne justifie plus l'envoi du rappel.

> **Données impliquées** : D-01 (données du membre), D-06 (données des abonnements), D-09 (données des notifications).

#### F-10 : Notifier les membres après une réservation

Le système informe automatiquement les membres de l'enregistrement dans le système de leurs réservations et leur communique les informations utiles pour le suivi de celles-ci.

* **EF-10.1** : Le système envoie une notification au membre après la création d'une réservation.
  * *Critère d'acceptation* : Si l’e-mail du membre qui fait la reservation n’est pas enregistré dans le système, alors aucune notification ne lui sera envoyé.
* **EF-10.2** : La notification contient le nom de l'objet réservé, la date de réservation, la date fixée pour l’emprunt et le statut de la réservation.
* **EF-10.3** : Lorsque cela est applicable, la notification précise la période de disponibilité prévue de l'objet ou les modalités de retrait.
* **EF-10.4** : Le système informe le membre lorsque sa réservation est annulée ou lorsque son statut est modifié de manière significative.
* **EF-10.5** : Le système associe chaque notification à la réservation correspondante.

> **Données impliquées** : D-01 (données du membre), D-03 (données des objets), D-07 (données des réservations), D-09 (données des notifications).

#### F-11 : Envoyer les reçus d'emprunt par e-mail

Le système génère un reçu après l'enregistrement d'un emprunt et l'envoie par courrier électronique au membre concerné.

* **EF-11.1** : Le système génère un reçu après l'enregistrement réussi d'un emprunt.
* **EF-11.2** : Le reçu contient les informations essentielles de l'opération, notamment l'identité du membre, l'objet emprunté, la date d'emprunt, la date de retour prévue et la caution versée.
* **EF-11.3** : Le système envoie le reçu à l'adresse e-mail associée au membre.
  * *Critère d'acceptation* : Si l’e-mail du membre qui fait l’emprunt n’est pas enregistré dans le système, alors aucun reçu ne lui sera envoyé.
* **EF-11.4** : Le système ne génère pas de reçu pour un emprunt qui n'a pas été enregistré avec succès.
* **EF-11.5** : Le système conserve les informations nécessaires pour retrouver le reçu associé à un emprunt.
* **EF-11.6** : En cas d'échec de l'envoi, le système enregistre l'incident afin de permettre une nouvelle tentative ou une intervention du bénévole.

> **Données impliquées** : D-01 (données du membre), D-03 (données des objets), D-08 (données des emprunts), D-10 (données des reçus).

#### F-12 : Notifier les membres à l'approche de la date de retour des objets empruntés

Le système envoie automatiquement des rappels aux membres lorsque la date prévue de retour d'un objet approche, afin de limiter les retards de restitution.

* **EF-12.1** : Le système identifie périodiquement les emprunts dont la date de retour prévue approche.
* **EF-12.2** : Le système (le bénévole peut également le faire) envoie un rappel au membre concerné avant la date de retour prévue.
  * *Critère d'acceptation* : Si l’e-mail du membre qui fait l’emprunt n’est pas enregistré dans le système, alors aucune notification ne lui sera envoyé.
* **EF-12.3** : Le rappel indique le nom de l'objet emprunté et la date prévue de retour.
* **EF-12.4** : Le système permet de configurer le délai précédant la date de retour auquel le rappel doit être envoyé.
* **EF-12.5** : Le système ne déclenche pas de rappel de retour pour un emprunt dont le retour a déjà été enregistré.
* **EF-12.6** : Le système peut envoyer un rappel supplémentaire lorsqu'un emprunt devient en retard, si cette règle est retenue par la bibliothèque.
* **EF-12.7** : Le système enregistre les notifications envoyées afin d'éviter les doublons et de permettre le suivi des rappels.

> **Données impliquées** : D-01 (données du membre), D-03 (données des objets), D-08 (données des emprunts), D-09 (données des notifications).
#### Fiches des fonctionnalités

### 3.2. Exigences non fonctionnelles
- **ENF-01 :** Une documentation utilisateur est fournie pour permettre une utilisation autonome de l'application par les bénévoles.
- **ENF-02 :** Une documentation développeur est fournie pour permettre la maintenance de l'application par les bénévoles.
- **ENF-03 :** Le code source est fourni de façon Open Source.
- **ENF-04 :** L'application possède une interface graphique. (GUI)
- **ENF-05 :** L'application est utilisable par six personnes simultanément.
## 4. Contraintes
- Les données sont traitées conformément au RGPD.
- Le développement de l'application est effectué en python en accord avec le cours de développement informatique 2.
- L'utilisation de l'application ne demande aucune connaissance technique étant donné qu'aucun personnel technique ne se trouve dans l'équipe de bénévols.
## 5. Budget

Le projet est réalisé dans un cadre scolaire , sans coût pour la bibliothèque. Charge estimée : 140 heures de travail (4 etudiants * 35 heures).

## 6. Livrables et planning

### 6.1. Livrables
- **L-01** L'Application installée et mise en ligne
- **L-02** Une guide d'utilisation pour la responsable et les bénévoles
- **L-03** La repsie de la listes des membres et des objets depuis le fichier excel
- **L-04** Le code source et la documentation technique

### 6.2. Échéances
| SEMAINE  | ECHEANCE                                            |
|:---------|:----------------------------------------------------|
| S2       | Validation du cahiers de charge                     |
|          | conception                                          |
|          | livraison du MVP (F-01 - F-08). reprises des membres et objets (L-03)|
|          | second increment : F-09 - F-12                      |
|          | version finale , guide d'utilisation recette finale |

### 6.3. Retours vers le client
- Demo à la responsable et aux benevoles à chaque livraison et point technique
- Question ouverte avec le client toutes les semaines

## 7. Validation du projet

- **Qui :** Les 06 Bénévoles et la resposable de la bibliothèque accompagnés d'un ou plusieurs membres du groupe  
- **Quand :** En S2 pour la validation du cahier de charge, s-- pour la livraison du MVP et S-- pour la validation de la version finale   
- **Sur quelle base :** la verification des critères d'exigences fonctionnelles section 3.1 , non fonctionnelles 3.2, des contraintes section 4  
- **Suivi des anomalies :** Les anomalies sont rélévés et prise en compte, avec l'identifiant de la section concernées et sa gravité (mineure,majeure,bloquante)   
- **Reception :** la responsable de la bibliothèque prononce la reception de la version finale en S-- s'il ne reste aucune anomalie bloquante ou majeure. Pour les anomalies mineures elles sont listées comme reservéés.


## 8. Maintenance

## 9. Questions ouvertes

## 10. Glossaire


