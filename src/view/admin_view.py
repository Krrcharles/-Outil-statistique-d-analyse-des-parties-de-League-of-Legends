from InquirerPy import prompt
from InquirerPy.separator import Separator

from view.member_view import MemberView
from view.session import Session


class AdminView(MemberView):
    def __init__(self):
        super().__init__()
        self.infos_option.append(Separator("🛠️"))
        self.infos_option.append("Modification") # modif a determiner
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "What are you looking for",
                "choices": self.infos_option,
            }
        ]

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
            return AdminView()

        else:
            from view.start_view import StartView

            return StartView()