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
        question = [
            {
                "type": "list",
                "name": "choix",
                "message": "What are you looking for",
                "choices": infos_option,
            }
        ]
        self.__question = question

    def display_info(self):
        print(f"") # a def

    def make_choice(self): 

        while True:
            answer = prompt(self.__question)

            if answer['choix'] == "Stats Champion" :
                print ("SC")

            elif answer['choix'] == "Ranking Champion" :
                print ("RC")

            elif answer['choix'] == "Stats Player" :
                print ("SP")

            else :
                print("SA")

            self.display_info()  # Appelez la fonction display_info pour afficher les informations

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

            if not another_infos["continue"]:
                from view.start_view import StartView

                return StartView()
