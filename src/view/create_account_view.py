from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session


class CreateAccountView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "identifiant",
                "message": "What's your login",
            },
            {
                "type": "input",
                "name": "password",
                "message": "What's your password",
            }
        ]

    def display_info(self):
        print("Hello, please enter your new login and password")

    def make_choice(self):
        answers = prompt(self.__questions)

        Session().user_identifiant = answers["identifiant"]
        Session().user_mdp = answers["password"]

        # methode en suspens

        choice = prompt(
            [
                {
                    "type": "confirm",
                    "name": "connect",
                    "message": "Do you want to connect ?",
                    "default": True,
                }
            ]
        )

        if choice["connect"]:
            from view.member_view import MemberView

            return MemberView()

        else:
            from view.invite_view import InviteView

            return InviteView()