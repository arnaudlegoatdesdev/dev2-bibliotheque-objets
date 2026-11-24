class Membre:
    def __init__(self,id_membre, nom, prenom,tel,adresse,email):
        self.__id = id_membre
        self.__nom = nom
        self.__prenom = prenom
        self.__tel = tel
        self.__adresse = adresse
        self.__email = email


    @property
    def id(self):
        return self.__id

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self,nom):
        self.__nom = nom

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self,prenom):
        self.__prenom = prenom


    @property
    def tel(self):
        return self.__tel

    @tel.setter
    def tel(self,tel):
        self.__tel = tel

    @property
    def adresse(self):
        return self.__adresse

    @adresse.setter
    def adresse(self,adresse):
        self.__adresse = adresse

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,email):
        self.__email = email


    def __str__(self):
        pass