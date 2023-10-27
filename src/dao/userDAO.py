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



A = UserDAO('data/database.db')
print(A.afficher_utilisateur('Bamara_Le_Goat'))