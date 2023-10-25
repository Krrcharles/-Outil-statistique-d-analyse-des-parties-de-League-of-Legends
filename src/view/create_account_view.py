from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session


class CreateView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "identifiant",
                "message":"What's your login",
            },
            {
                "type": "input",
                "name": "password",
                "message":"What's your password",
            }
        ]

    def display_info(self):
        print(f"Hello, please enter your new login and password")

    def make_choice(self):
        answers = prompt(self.__questions)
        Session().user_identifiant = answers["name_1"]
        Session().user_mdp = answers["name_2"]

        from view.start_view import StartView

        return MemberView()