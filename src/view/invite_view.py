from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session


class InviteView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "invite",
                "choices": [
                    "Player games : ",
                    "Player information",
                    "Champion statistics",
                    "Champion Rankings ()",
                ],
                "message": "What are you looking for",
            }
        ]

    def display_info(self):
        print(f"")

    def make_choice(self):
        answers = prompt(self.__questions)
        Session().user_identifiant = answers["login"]
        Session().user_mdp = answers["password"]

        from view.start_view import StartView

        return MemberView()