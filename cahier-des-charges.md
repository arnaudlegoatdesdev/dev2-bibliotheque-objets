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

- Le projet comprend la gestion du catalogue et des exemplaires physiques, des membres et de leurs abonnements, des réservations, des emprunts et des retours. Il inclut le suivi de l'état des objets, des pièces des kits, des cautions et des historiques d'emprunts et d'incidents.

- Le catalogue existant dans Airtable devra être repris au démarrage. Les bénévoles pourront modifier les fiches objets sans validation préalable, avec une trace permettant de retrouver qui a effectué les modifications. Les membres pourront consulter le catalogue pendant les permanences.

- L’application ne remplacera pas les permanences physiques, les échanges avec les membres ou les conseils d’utilisation des objets. Le catalogue papier affiché au local sera conservé.

- La mise en ligne, l’accès des membres à distance, la réservation autonome, les notifications par e-mail, la création de nouvelles formules d’abonnement et l’intégration du planning des bénévoles restent à valider avec la cliente. Ces points seront repris dans les questions ouvertes.

### 2.4. Règles métier

- **RM-01** : L’abonnement est annuel. La formule pleine coûte 30 € et permet d’emprunter trois objets simultanément. Le tarif réduit coûte 10 € et permet d’en emprunter deux simultanément.

- **RM-02** : Un emprunt dure une semaine. Il peut être prolongé une seule fois, pour une semaine supplémentaire, si l’objet n’est pas réservé par un autre membre.

- **RM-03** : Les réservations sont gratuites et concernent une permanence précise. Un objet déjà emprunté peut être réservé pour la prochaine permanence.

- **RM-04** : Si le membre ne vient pas chercher l’objet réservé, la réservation expire à la fin de la permanence concernée, sans frais.

- **RM-05** : Un membre ayant un objet en retard ne peut plus effectuer de nouvel emprunt tant que l’objet n’est pas rendu. Aucune amende n’est appliquée pour les retards.

- **RM-06** : Au troisième retard dans l’année, un bénévole appelle le membre pour lui rappeler la charte.

- **RM-07** : Au retour, le bénévole vérifie l’état de l’objet et les pièces attendues pour les kits. L’état est indiqué parmi les valeurs suivantes : bon, usure normale, endommagé ou incomplet.

- **RM-08** : Un objet endommagé ou incomplet est mis de côté et ne peut pas être emprunté en attendant sa vérification par un bénévole bricoleur.

- **RM-09** : La caution dépend de la catégorie de valeur de l’objet : aucune caution pour A, 20 € pour B, 50 € pour C et 100 € pour D.

- **RM-10** : La caution est payée en liquide à l’emprunt et restituée en liquide au retour. Si l’objet est abîmé ou si des pièces manquent, le bénévole peut en retenir une partie en indiquant une justification.

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
| **F-09** | Gérer les sauvegardes et la restauration des données           | Administrateur, Système | Indispensable | 
| **F-10** | Initialiser le système à partir des données existantes         | Administrateur, Système | Indispensable |
| **F-11** | Envoyer les notifications relatives aux abonnements par e-mail | Bénévole, Système | Souhaitable   | 
| **F-12** | Envoyer les confirmations de réservation par e-mail            | Bénévole, Système | Souhaitable   | 
| **F-13** | Envoyer les reçus d'emprunt par e-mail                         | Bénévole, Système | Souhaitable   | 
| **F-14** | Envoyer des rappels par e-mail de retour des objets empruntés  | Bénévole, Système | Souhaitable   | 

#### Vue d'ensemble du MVP

Le MVP (*Minimum Viable Product*) sera centré sur les fonctionnalités indispensables au fonctionnement de la bibliothèque. Il permettra au Bénévole et/ou à l’Administrateur de gérer :

* Les membres
* Les comptes utilisateurs
* Le catalogue des objets et leurs types
* Les formules d'abonnement et les abonnements des membres
* Les réservations, les emprunts et les retours d’objets

Il permettra également d'enregistrer les réservations, les emprunts et les retours d'objets afin d'assurer le suivi de leur disponibilité et de leur état physique.

Les fonctionnalités de notification automatique et d'envoi de reçus par e-mail pourront être intégrées dans une version ultérieure, selon le périmètre retenu et la validation de Madame Pereira.

Les fonctionnalités **F-01** à **F-10** sont détaillées ci-dessous sous forme d'exigences fonctionnelles. Les fonctionnalités **F-11** à **F-14** seront précisées ultérieurement, notamment en ce qui concerne les délais d'envoi, les événements déclencheurs et les canaux de notification.

Le MVP intégrera également les fonctionnalités de sauvegarde et de restauration des données ainsi que l’importation initiale des données existantes de la bibliothèque. Cette importation permettra de récupérer les données des membres et du catalogue actuellement stockées dans Airtable, ainsi que l’historique des emprunts conservé dans un tableur, après vérification de leur cohérence.

#### Détail des exigences fonctionnelles (MVP)

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

#### F-09 : Gérer les sauvegardes et la restauration des données

L’administrateur peut déclencher une sauvegarde des données de la bibliothèque et restaurer les données à partir d’une sauvegarde existante. Le système permet de protéger les données contre les pertes accidentelles et de récupérer un état cohérent de la bibliothèque en cas d’incident.

- **EF-09.1** : Le système permet à l’administrateur de déclencher manuellement une sauvegarde des données de la bibliothèque.
- **EF-09.2** : Le système peut effectuer automatiquement des sauvegardes selon une fréquence définie par l’administrateur.
- **EF-09.3** : Chaque sauvegarde doit contenir les données nécessaires à la reprise du système, notamment les membres, les objets, les abonnements, les réservations, les emprunts et les informations relatives aux cautions.
- **EF-09.4** : Le système conserve les informations permettant d’identifier chaque sauvegarde, notamment sa date de création et son statut.
- **EF-09.5** : L’administrateur peut consulter la liste des sauvegardes disponibles.
- **EF-09.6** : L’administrateur peut restaurer les données à partir d’une sauvegarde sélectionnée.
- **EF-09.7** : Avant une restauration susceptible de remplacer les données existantes, le système demande une confirmation explicite à l’administrateur.
- **EF-09.8** : Le système vérifie qu’une sauvegarde est exploitable avant de lancer sa restauration.
- **EF-09.9** : Le système signale le résultat d’une sauvegarde ou d’une restauration et indique les éventuelles erreurs rencontrées.
- **EF-09.10** : Le système conserve une trace des opérations de sauvegarde et de restauration, notamment leur date, leur résultat et l’utilisateur qui les a déclenchées.

> **Données impliquées** : D-01 (données des membres), D-03 (données des objets), D-04 (données des types d’objets), D-05 (données des formules d’abonnement), D-06 (données des abonnements), D-07 (données des réservations), D-08 (données des emprunts), D-09 (données des notifications), D-10 (données des reçus).

#### F-10 : Initialiser le système à partir des données existantes

L’administrateur peut initialiser le système en important les données historiques de la bibliothèque actuellement stockées dans Airtable et dans un tableur. Le système permet de contrôler, de valider et d’intégrer ces données afin de démarrer l’utilisation de la nouvelle application sans devoir tout encoder manuellement.

- **EF-10.1** : Le système permet à l’administrateur d’importer les données des membres depuis Airtable.
- **EF-10.2** : Le système permet à l’administrateur d’importer les données du catalogue des objets depuis Airtable.
- **EF-10.3** : Le système permet à l’administrateur d’importer les données historiques des emprunts depuis un tableur compatible avec le format retenu pour le projet.
- **EF-10.4** : Le système permet d’associer les colonnes des fichiers ou des sources importées aux champs correspondants du nouveau système, selon un mapping défini.
- **EF-10.5** : Le système vérifie la cohérence des données importées, notamment la présence des champs obligatoires, la validité des formats et la cohérence des références entre membres, objets et emprunts.
- **EF-10.6** : Le système détecte les doublons potentiels et les données qui ne peuvent pas être importées correctement.
- **EF-10.7** : Avant de lancer l’importation définitive, le système présente un récapitulatif des données à importer et des éventuelles erreurs détectées.
- **EF-10.8** : L’administrateur peut confirmer ou annuler l’importation après avoir consulté le récapitulatif.
- **EF-10.9** : Le système conserve les relations entre les membres, les exemplaires physiques et les emprunts lors de l’importation des données historiques.
- **EF-10.10** : Le système attribue des identifiants internes uniques aux données importées lorsque cela est nécessaire, tout en conservant les références historiques utiles à la traçabilité.
- **EF-10.11** : Le système génère un rapport d’importation indiquant le nombre d’enregistrements importés, ignorés ou rejetés, ainsi que les erreurs détectées.
- **EF-10.12** : Le système permet à l’administrateur de consulter le rapport d’une importation terminée afin de faciliter la correction des données rejetées.
- **EF-10.13** : Le système empêche qu’une même donnée soit importée plusieurs fois sans contrôle, notamment lors d’une nouvelle tentative d’importation.
- **EF-10.14** : Avant l’importation initiale, le système permet de sauvegarder les données déjà présentes afin de pouvoir les récupérer en cas de problème.

> **Données impliquées** : D-01 (données des membres), D-03 (données des objets), D-04 (données des types d’objets), D-06 (données des abonnements), D-07 (données des réservations), D-08 (données des emprunts).

#### Fonctionnalités secondaires (Post-MVP)

#### F-11 : Notifier les membres à l'approche de l'expiration de leur abonnement

Le système informe automatiquement les membres lorsque leur abonnement approche de sa date d'expiration, afin de leur permettre de prendre les dispositions nécessaires pour le renouveler.

* **EF-11.1** : Le système identifie périodiquement les abonnements dont la date d'expiration approche.
* **EF-11.2** : Le système envoie une notification au membre concerné avant l'expiration de son abonnement.
  * *Critère d'acceptation* : Si l’e-mail du membre n’est pas enregistré dans le système, alors aucun rnotification ne lui sera envoyé.
* **EF-11.3** : La notification contient les informations essentielles de l'abonnement, notamment sa date d'expiration.
* **EF-11.4** : Le système permet de définir le délai précédant l'expiration auquel la notification doit être envoyée.
* **EF-11.5** : Le système évite d'envoyer plusieurs notifications identiques pour une même échéance, selon la fréquence définie.
* **EF-11.6** : Le système ne déclenche pas de rappel d'expiration pour un abonnement qui a été renouvelé ou dont le statut ne justifie plus l'envoi du rappel.

> **Données impliquées** : D-01 (données du membre), D-06 (données des abonnements), D-09 (données des notifications).

#### F-12 : Notifier les membres après une réservation

Le système informe automatiquement les membres de l'enregistrement dans le système de leurs réservations et leur communique les informations utiles pour le suivi de celles-ci.

* **EF-12.1** : Le système envoie une notification au membre après la création d'une réservation.
  * *Critère d'acceptation* : Si l’e-mail du membre qui fait la reservation n’est pas enregistré dans le système, alors aucune notification ne lui sera envoyé.
* **EF-12.2** : La notification contient le nom de l'objet réservé, la date de réservation, la date fixée pour l’emprunt et le statut de la réservation.
* **EF-12.3** : Lorsque cela est applicable, la notification précise la période de disponibilité prévue de l'objet ou les modalités de retrait.
* **EF-12.4** : Le système informe le membre lorsque sa réservation est annulée ou lorsque son statut est modifié de manière significative.
* **EF-12.5** : Le système associe chaque notification à la réservation correspondante.

> **Données impliquées** : D-01 (données du membre), D-03 (données des objets), D-07 (données des réservations), D-09 (données des notifications).

#### F-13 : Envoyer les reçus d'emprunt par e-mail

Le système génère un reçu après l'enregistrement d'un emprunt et l'envoie par courrier électronique au membre concerné.

* **EF-13.1** : Le système génère un reçu après l'enregistrement réussi d'un emprunt.
* **EF-13.2** : Le reçu contient les informations essentielles de l'opération, notamment l'identité du membre, l'objet emprunté, la date d'emprunt, la date de retour prévue et la caution versée.
* **EF-13.3** : Le système envoie le reçu à l'adresse e-mail associée au membre.
  * *Critère d'acceptation* : Si l’e-mail du membre qui fait l’emprunt n’est pas enregistré dans le système, alors aucun reçu ne lui sera envoyé.
* **EF-13.4** : Le système ne génère pas de reçu pour un emprunt qui n'a pas été enregistré avec succès.
* **EF-13.5** : Le système conserve les informations nécessaires pour retrouver le reçu associé à un emprunt.
* **EF-13.6** : En cas d'échec de l'envoi, le système enregistre l'incident afin de permettre une nouvelle tentative ou une intervention du bénévole.

> **Données impliquées** : D-01 (données du membre), D-03 (données des objets), D-08 (données des emprunts), D-10 (données des reçus).

#### F-14 : Notifier les membres à l'approche de la date de retour des objets empruntés

Le système envoie automatiquement des rappels aux membres lorsque la date prévue de retour d'un objet approche, afin de limiter les retards de restitution.

* **EF-14.1** : Le système identifie périodiquement les emprunts dont la date de retour prévue approche.
* **EF-14.2** : Le système (le bénévole peut également le faire) envoie un rappel au membre concerné avant la date de retour prévue.
  * *Critère d'acceptation* : Si l’e-mail du membre qui fait l’emprunt n’est pas enregistré dans le système, alors aucune notification ne lui sera envoyé.
* **EF-14.3** : Le rappel indique le nom de l'objet emprunté et la date prévue de retour.
* **EF-14.4** : Le système permet de configurer le délai précédant la date de retour auquel le rappel doit être envoyé.
* **EF-14.5** : Le système ne déclenche pas de rappel de retour pour un emprunt dont le retour a déjà été enregistré.
* **EF-14.6** : Le système peut envoyer un rappel supplémentaire lorsqu'un emprunt devient en retard, si cette règle est retenue par la bibliothèque.
* **EF-14.7** : Le système enregistre les notifications envoyées afin d'éviter les doublons et de permettre le suivi des rappels.

> **Données impliquées** : D-01 (données du membre), D-03 (données des objets), D-08 (données des emprunts), D-09 (données des notifications).


### 3.2. Exigences non fonctionnelles proposées

Les exigences ci-dessous sont des propositions déduites du contexte du projet. Elles ne sont pas encore des contraintes explicitement validées par Mme Pereira.

#### Vue d’ensemble des exigences non fonctionnelles

| ID | Exigence non fonctionnelle | Priorité proposée |
| :--- | :--- | :--- |
| **ENF-01** | Sécurité et contrôle d’accès | Indispensable |
| **ENF-02** | Confidentialité et protection des données | Indispensable |
| **ENF-03** | Performance | Souhaitable |
| **ENF-04** | Fiabilité et intégrité des données | Indispensable |
| **ENF-05** | Disponibilité du système | Souhaitable |
| **ENF-06** | Sauvegarde et récupération des données | Indispensable |
| **ENF-07** | Ergonomie et facilité d’utilisation | Indispensable |
| **ENF-08** | Compatibilité avec les environnements retenus | À confirmer |
| **ENF-09** | Maintenabilité et évolutivité | Souhaitable |
| **ENF-10** | Traçabilité des opérations | Indispensable |
| **ENF-11** | Expérience utilisateur et accessibilité de l'interface (UI/UX) | Souhaitable |

#### ENF-01 — Sécurité et contrôle d’accès

Le système doit protéger les données et empêcher les utilisateurs non autorisés d’accéder aux fonctionnalités ou aux informations qui ne leur sont pas destinées.

- **ENF-01.1** : Le système doit exiger une authentification pour accéder aux fonctionnalités protégées.
- **ENF-01.2** : Les mots de passe doivent être stockés sous une forme sécurisée, à l’aide d’un mécanisme de hachage adapté.
- **ENF-01.3** : Le système doit appliquer les autorisations correspondant au rôle de chaque utilisateur.
- **ENF-01.4** : Les sessions doivent expirer après une période d’inactivité définie, si cela est pertinent pour l’application.

> **Pourquoi ?** Le système gère des comptes, des informations personnelles de membres et des opérations réalisées par les bénévoles et les administrateurs.

#### ENF-02 — Confidentialité et protection des données

- **ENF-02.1** : Le système doit limiter l’accès aux données personnelles aux utilisateurs qui en ont besoin dans le cadre de leurs fonctions.
- **ENF-02.2** : Les données personnelles ne doivent pas être divulguées à des personnes non autorisées.
- **ENF-02.3** : Les données doivent être conservées et supprimées conformément aux règles de conservation applicables.

> **Pourquoi ?** Les dossiers des membres peuvent contenir des noms, des coordonnées, des informations d’abonnement et un historique d’emprunts.

#### ENF-03 — Performance

- **ENF-03.1** : Le système doit afficher les résultats d’une recherche dans le catalogue en moins de 2 secondes dans des conditions normales d’utilisation.
- **ENF-03.2** : Les opérations courantes — consultation d’un membre, enregistrement d’un emprunt ou d’un retour — doivent être exécutées en moins de 3 secondes dans des conditions normales d’utilisation.

> **Pourquoi ?** Les bénévoles doivent pouvoir gérer rapidement les emprunts et les retours, notamment lorsqu’ils accueillent plusieurs membres. Les délais de 2 et 3 secondes sont des objectifs proposés, à valider avec le client.

#### ENF-04 — Fiabilité et intégrité des données

- **ENF-04.1** : Le système doit garantir l’unicité des identifiants des membres, des comptes utilisateurs et des exemplaires physiques.
- **ENF-04.2** : Une opération interrompue ne doit pas laisser les données dans un état incohérent.
- **ENF-04.3** : Le système doit empêcher qu’un même exemplaire soit attribué à plusieurs emprunts simultanés incompatibles.
- **ENF-04.4** : Les montants des cautions encaissées, restituées ou retenues doivent être enregistrés de manière cohérente et traçable.

> **Pourquoi ?** Une erreur pourrait entraîner un double emprunt, une disponibilité incorrecte ou une contestation concernant une caution.

#### ENF-05 — Disponibilité du système

- **ENF-05.1** : Le système doit être accessible pendant les heures d’ouverture de la bibliothèque, sous réserve des opérations de maintenance annoncées.
- **ENF-05.2** : Les interruptions planifiées doivent être limitées et, si possible, communiquées à l’avance.

> **Pourquoi ?** Les bénévoles doivent pouvoir consulter le catalogue et enregistrer les opérations pendant leurs permanences. Un taux de disponibilité précis, par exemple 99 %, ne devrait être imposé que si le client le juge nécessaire.

#### ENF-06 — Sauvegarde et récupération des données

- **ENF-06.1** : Le système doit disposer d’un mécanisme de sauvegarde des données.
- **ENF-06.2** : Les sauvegardes doivent permettre de restaurer les informations en cas de panne ou de perte de données.
- **ENF-06.3** : La procédure de restauration doit être testée périodiquement.

> **Pourquoi ?** La perte des données pourrait supprimer les historiques d’emprunts, les dossiers des membres ou le suivi des cautions.

#### ENF-07 — Ergonomie et facilité d’utilisation

- **ENF-07.1** : L’interface doit être compréhensible par des bénévoles ne possédant pas nécessairement de compétences informatiques avancées.
- **ENF-07.2** : Les champs obligatoires, les erreurs de saisie et les confirmations d’opération doivent être clairement signalés.
- **ENF-07.3** : Les actions courantes, telles que rechercher un objet, enregistrer un emprunt ou confirmer un retour, doivent être accessibles avec un nombre raisonnable d’étapes.

> **Pourquoi ?** Le système est destiné à faciliter le travail des bénévoles, et non à rendre les opérations plus complexes.

#### ENF-08 — Compatibilité

- **ENF-08.1** : Le système etant un logiciel, il doit fonctionner sur les versions récentes des principaux systèmes d’exploitations retenus pour le projet.
- **ENF-08.2** : L’interface doit rester utilisable sur les formats d’écran retenus, notamment les ordinateurs utilisés à la bibliothèque.

> **Pourquoi ?** Cette exigence dépend de la plateforme qui sera choisie pour développer l’application.

#### ENF-09 — Maintenabilité et évolutivité

- **ENF-09.1** : Le code source doit être organisé de manière modulaire afin de faciliter les corrections et les évolutions.
- **ENF-09.2** : Les règles métier importantes, notamment celles relatives aux abonnements, aux emprunts et aux cautions, doivent être documentées.
- **ENF-09.3** : L’ajout de nouveaux types d’objets ou de nouvelles formules d’abonnement ne doit pas nécessiter une modification majeure de l’application.

> **Pourquoi ?** La bibliothèque pourrait faire évoluer ses règles de gestion, ses catégories d’objets et ses formules d’abonnement.

#### ENF-10 — Traçabilité des opérations

- **ENF-10.1** : Le système doit permettre de retrouver l’historique des opérations importantes, notamment les emprunts, les retours et les modifications de l’état des objets.
- **ENF-10.2** : Les traces techniques ne doivent pas exposer inutilement les mots de passe ou d’autres données sensibles.

> **Pourquoi ?** La traçabilité facilite la résolution des litiges et permet de comprendre ce qui s’est passé lorsqu’un objet est endommagé ou qu’une caution est retenue.

#### ENF-11 — Expérience utilisateur et accessibilité de l'interface (UI/UX)

L'interface utilisateur doit offrir une navigation intuitive, fluide et accessible, minimisant la charge cognitive des utilisateurs lors de la manipulation quotidienne du système.

- **ENF-11.1** : L'interface doit proposer un design ergonomique respectant les principes d'accessibilité de base (notamment des contrastes de couleurs suffisants et une taille de police lisible) pour faciliter la lecture sur les écrans de la bibliothèque.
- **ENF-11.2** : Le système doit fournir un retour visuel immédiat et explicite à l'utilisateur suite à chaque action validée (confirmation de succès, message d'alerte en cas d'erreur de saisie ou blocage).

> **Pourquoi ?** Une bonne expérience utilisateur (UX) et une interface (UI) épurée permettent aux bénévoles d'enchaîner rapidement les opérations aux heures de forte affluence tout en réduisant les risques d'erreurs de saisie.
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


