from InquirerPy import prompt

from src.view.abstract_view import AbstractView
from src.view.session import Session
from src.view.connexion_view import ConnexionView


class StartView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "Hello",
                "choices": [
                    "Créer un compte",
                    "Rester en tant qu'invité",
                    "Se connecter",
                    "Quitter l'application",
                ],
            }
        ]

    def display_info(self):
        with open("src/graphical_assets/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quit":
            pass

        elif reponse["choix"] == "Créer un compte":  
            from src.view.create_account_view import CreateAccountView

            return CreateAccountView()

        elif reponse["choix"] == "Rester en tant qu'invité":
            from src.view.invite_view import InviteView

            return InviteView()

        elif reponse["choix"] == "Se connecter":
            from src.view.connexion_view import ConnexionView

            return ConnexionView()

