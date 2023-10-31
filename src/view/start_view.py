from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from view.connexion_view import ConnexionView


class StartView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello {Session().user_identifiant}",
                "choices": [
                    "Create",
                    "Invite",
                    "Connection",
                    "Quit",
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

        elif reponse["choix"] == "Create":  
            from view.create_account_view import CreateAccountView

            return CreateAccountView()

        elif reponse["choix"] == "Invite":
            from view.invite_view import InviteView

            return InviteView()

        elif reponse["choix"] == "Connection":
            from view.connexion_view import ConnexionView

            return ConnexionView()

