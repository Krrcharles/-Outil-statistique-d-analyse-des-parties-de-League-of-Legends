import sqlite3
import hashlib

########################################
### CREATION DE LA TABLE UTILISATEUR ###
########################################

# Le mettre en fonction ?????

# Connexion à la base de données
#conn = sqlite3.connect('data/database.db')

# Création objet "cursor"
#cursor = conn.cursor()

# Création de la table utilisateur
#cursor.execute('''
#    CREATE TABLE IF NOT EXISTS utilisateurs (
#        id SERIAL PRIMARY KEY,
#        login TEXT,
#        password INTEGER,
#        isadmin BOOL
#    )
#''')

# Validez les modifications
#conn.commit()

# Fermez le curseur et la connexion à la base de données lorsque vous avez terminé
#cursor.close()
#conn.close()


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
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM utilisateurs WHERE login = ?", (login,))
        user_id = cursor.fetchone()

        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), user_id, 100)

        cursor.close()
        conn.close()
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
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM utilisateurs WHERE login = ?", (newlogin,))
        list_login = cursor.fetchone()

        if list_login is not None:
            cursor.close()
            conn.close()
            return False

        hached_password = self.hached(newlogin, newpassword)

        cursor.execute("INSERT INTO utilisateur VALUES (?,?,?)", (newlogin, hached_password, False))
        conn.commit()
        cursor.close()
        conn.close()
        return True

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
        cursor.execute("SELECT password FROM utilisateurs WHERE login = ?", (login,))
        realpassword = self.hached(login, cursor.fetchone())

        if password == realpassword:
            cursor.close()
            conn.close()
            return True

        cursor.close()
        conn.close()
        return False
