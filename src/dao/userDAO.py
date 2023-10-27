from src.business.user.user import User
import sqlite3
import hashlib


class UserDAO() : 
    def __init__(self, db_name='data/database.db'):

        """
        Initialize the class with the name of the SQLite database file.

        Parameters:
        db_name (str): Name of the SQLite database file.
        """
        self.db_name = db_name


    def afficher_utilisateur(self, login):
        """
        affiche un utilisateur de l'application présent dans la bdd.

        Parameters
        ----------
        login: str
            Nom d'utilisateur de l'utilisateur.

        Return
        ------
        l'instance user de la classe User
        """

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        query = """SELECT id, login, password, isadmin 
                    FROM utilisateur 
                    WHERE login = ?
                    """
      
        cursor.execute(query, (login,))
        list_login = cursor.fetchone()

        user = None

        if list_login :
            user = User(
                id = list_login[0],
                login = list_login[1],
                password = list_login[2],
                is_admin = list_login[3] 
            )

        return user

    def inserer_utilisateur(self, newlogin, newpassword) :

        """Permet d'insérer dans la bdd un nouvel utilisateur"""

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        query  = "INSERT INTO utilisateur (login, password, isadmin) VALUES (?,?,?)"
        cursor.execute(query,(newlogin, newpassword, 0))

"""A = UserDAO('data/database.db')
print(A.afficher_utilisateur('Bamara_Le_Goat'))"""