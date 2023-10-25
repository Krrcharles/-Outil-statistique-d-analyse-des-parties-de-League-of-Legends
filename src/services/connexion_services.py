import sqlite3

########################################
### CREATION DE LA TABLE UTILISATEUR ###
########################################


# Établir une connexion à la base de données (créez la base de données si elle n'existe pas)
#conn = sqlite3.connect('data/database.db')

# Créez un objet "cursor" pour exécuter des commandes SQL
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
    """
    def inscription(newlogin, newpassword):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM utilisateurs WHERE login = ?", newlogin)
        list_login = cursor.fetchone()

        if list_login is not None:
            cursor.close()
            conn.close()
            return False

        cursor.execute("INSERT INTO utilisateur VALUES (?,?,?)", (newlogin, newpassword, False))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def connexion(login, password):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM utilisateurs WHERE login = ?", login)
        realpassword = cursor.fetchone()

        if password == realpassword :
            cursor.close()
            conn.close()
            return True

        cursor.close()
        conn.close()
        return False
