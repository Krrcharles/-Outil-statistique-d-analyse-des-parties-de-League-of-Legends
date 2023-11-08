import sqlite3
import hashlib
import UserDAO from src.dao.userDAO


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

    def hached(self, login, password):
        """
        Fonction qui prend un mot de passe en clair et un nom d'utilisateur,
        hache le mot de passe avec le sel et retourne le résultat.

        Parameters
        ----------
        login: str
            Nom d'utilisateur.
        password: str
            Mot de passe en clair.

        Return
        ------
        Le mot de passe haché.
        """
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), login.encode('utf-8'), 100)
        return password_hash

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
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT password, isadmin FROM utilisateur WHERE login = ?", (login,))

        real_password, isadmin = cursor.fetchone()
        test_password = self.hached(login, password)

        cursor.close()
        conn.close()

        if test_password == real_password:
            if isadmin == 1:
                return ("admin")
            return ("membre")
        return ("failed")


# D = Connexion_services('data/database.db')

# print(D.inscription('teemo', 'lemdpkitue'))

# D.inscription('teemo', 'unmdpnul')

# print(D.connexion('teemo', 'lemdpkitue'))

# print(D.connexion('admin', 'admin'))

# print(D.connexion('teemo', '" or 1=1; -- '))
