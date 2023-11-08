import sqlite3
import hashlib
from src.dao.userDAO import UserDAO



class Connexion_services():
    """
    Cette classe gère l'inscription et la connexion des utilisateurs
    en stockant les mots de passe de manière sécurisée.
    """
    def __init__(self, db_name='data/database.db'):
        """
        Initialise la classe avec le nom de la base de données.

        Parameters
        ----------
        db_name: db
        Nom du fichier de base de données SQLite.
        """
        self.db_name = db_name

    def inscription(self, newlogin, newpassword):
        """
        Enregistre un nouvel utilisateur dans la base de données.

        Parameters
        ----------
        newlogin: str
            Nom d'utilisateur du nouvel utilisateur.
        newpassword: str
            Mot de passe en clair du nouvel utilisateur.

        Return
        ------
        True si l'inscription est réussie, False si le nom d'utilisateur existe déjà.
        """
        classe = UserDAO()
        inscrit = classe.rajouter_utilisateur (newlogin,newpassword)
        if inscrit is False :
            return "Nom d'utilisateur déjà utilisé"


    def connexion(self, login, password):
        """
        Vérifie les informations d'authentification de l'utilisateur.

        Parameters
        ----------
        login: str
            Nom d'utilisateur.
        password: str
            Mot de passe en clair à vérifier.

        Return
        ------
        True si l'authentification est réussie, False sinon.
        """
        connexion = False
        classe = UserDAO()
        test_password = classe.hached(login, password)
        utilisateur = classe.recuperer_mdp(login,password)

        if test_password == utilisateur[0]:
            connexion = True
            if utilisateur[1] == 1:
                print("admin")
                connexion = False
        return connexion


# D = Connexion_services('data/database.db')

#print(D.inscription('teemo_ultime', 'lemdpkitue'))

# D.inscription('teemo', 'unmdpnul')

#print(D.connexion('teemo', 'lemdpkitue'))

# print(D.connexion('admin', 'admin'))

# print(D.connexion('teemo', '" or 1=1; -- '))
