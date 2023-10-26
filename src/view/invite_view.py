from InquirerPy import prompt
from InquirerPy.separator import Separator

from view.abstract_view import AbstractView
from view.session import Session


class InviteView(AbstractView):
    def __init__(self):
        infos_option = [
            Separator("📰"),
            "Stats Champion",
            Separator("👑"),
            "Ranking Champion",
            Separator("🎮"),
            "Stats Player",
        ]
        self.infos_option = infos_option
        questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "What are you looking for",
                "choices": self.infos_option,
            }
        ]
        self.__questions = questions

    def display_info(self):
        print(f"") # a def

    def make_choice(self):
        answers = prompt(self.__questions) 

        # methode en suspens

        another_infos = prompt(
            [
                {
                    "type": "confirm",
                    "name": "continue",
                    "message": "Another Information ?",
                    "default": True,
                }
            ]
        )

        if another_infos["continue"]:
            return InviteView()

        else:
            from view.start_view import StartView

            return StartView()
        