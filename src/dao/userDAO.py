from src.business.user.user import User
import sqlite3
import hashlib


class UserDAO : 
    def __init__(self, db_name='data/database.db'):

        """
        Initialize the class with the name of the SQLite database file.

        Parameters:
        db_name (str): Name of the SQLite database file.
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


    def verifier_utilisateur (self, login):
        """
        Vérifie si un utilisateur est dans la base de données.

        Parameters
        ----------
        login: str
            Nom d'utilisateur à vérifier.
        Return
        ------
        True si l'utilisateur y est, False sinon.
        """

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM utilisateur WHERE login = ?", (login,))
        list_login = cursor.fetchone()

        present = True
        if list_login is None:
            present = False 
        return present

    def rajouter_utilisateur(self, newlogin, newpassword):
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
        bool
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        verif = UserDAO().verifier_utilisateur(newlogin)

        if verif == False :
            hached_password = self.hached(newlogin, newpassword)

            cursor.execute("INSERT INTO utilisateur (login, password, isadmin) VALUES (?,?,?)", (newlogin, hached_password, 0))
            conn.commit()
            cursor.close()
            conn.close()
        return not verif

    def recuperer_mdp(self, login) :
        """
        Récupère le mdp d'un utilisateur en fonction de son login
        Parameters
        ----------
        login: str
            Nom d'utilisateur du nouvel utilisateur.

        Return
        ------
        tuple
        """        

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT password, isadmin FROM utilisateur WHERE login = ?", (login,))
        real_password, isadmin = cursor.fetchone()
        cursor.close()
        conn.close()

        return real_password, isadmin


"""a=UserDAO()
print(a.rajouter_utilisateur('best_user','mdpasse'))"""