from InquirerPy import prompt
from InquirerPy.separator import Separator

from src.view.member_view import MemberView
from src.services.connexion_services import Connexion_services
from src.view.abstract_view import AbstractView
from src.view.session import Session


class ConnexionView(AbstractView):
    def __init__(self):
        super().__init__()
        self.__questions = [
            {
                "type": "input",
                "name": "identifiant",
                "message": "What is your login",
            },
            {
                "type": "input",
                "name": "password",
                "message": "What is your password",
            },]

    def display_info(self):
        print(f"") # a def

    def make_choice(self):
        answers = prompt(self.__questions)

        user_identifiant = answers["identifiant"]
        password = answers["password"]
        
        # Vérification que l'identifiant existe, et que l'identifiant et le mot de passe coincident 

        instance = Connexion_services()
        resultat = instance.connexion(user_identifiant,password)

        if resultat == "failed" :
            print(f"Il se peut que votre nom d'utilisateur ou mot de passe soit incorrect ou que vous deviez passer à un compte Riot si vous n'avez pas joué depuis quelques mois.")

            return ConnexionView()

        elif resultat == "admin":
            from view.admin_view import AdminView
            Session().user_identifiant = answers["identifiant"]
            Session().user_mdp = answers["password"]

            return AdminView()

        else : 
            from view.member_view import MemberView
            Session().user_identifiant = answers["identifiant"]
            Session().user_mdp = answers["password"]

            return MemberView()