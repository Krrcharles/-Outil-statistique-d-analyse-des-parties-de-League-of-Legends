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
        if not isinstance(newlogin, str):
            print("Le login n'est pas une chaine de caractère")
            return False

        if not isinstance(newpassword, str):
            print("Le mot de passe n'est pas une chaine de caractère")
            return False

        classe = UserDAO()
        inscrit = classe.rajouter_utilisateur(newlogin, newpassword)
        if inscrit is False:
            print("Nom d'utilisateur déjà utilisé")
            return False

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
        if not isinstance(login, str):
            print("Le login n'est pas une chaine de caractère")
            return False

        if not isinstance(password, str):
            print("Le mot de passe n'est pas une chaine de caractère")
            return False

        connexion = "failed"
        classe = UserDAO()

        if classe.verifier_utilisateur(login) is True:
            test_password = classe.hached(login, password)
            utilisateur = classe.recuperer_mdp(login)

            if test_password == utilisateur[0]:
                connexion = True
                if utilisateur[1] == 1:
                    connexion = 'admin'
                    return connexion
                return connexion
            print("Mauvais mot de passe.")
            return connexion
        else:
            print("Le login n'est pas enregistré")
            return connexion


D = Connexion_services('data/database.db')

# print(D.inscription('teemo_ultime', 'lemdpkitue'))

# D.inscription('teemo', 'unmdpnul')

# print(D.connexion('teemo', 'lemdpkitue'))

print(D.connexion('admin', 'adminddd'))

# print(D.connexion('teemo', '" or 1=1; -- '))
