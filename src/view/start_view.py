from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session


class StartView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello {Session().user_identifiant}",
                "choices": [
                    "Invite",
                    "Connection",
                    "Admin",
                    "Create",
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

        elif reponse["choix"] == "Connection":
            from view.connection_view import ConnectionView

            return ConnectionView()

        elif reponse["choix"] == "Invite":
            from view.connection_view import InviteView

            return InviteView()

        elif reponse["choix"] == "Create":
            from view.connection_view import CreateView

            return CreateView()

        elif reponse["choix"] == "Stats":
            from view.battle_view import StatsView

            return StatsView()
