from InquirerPy import prompt
from InquirerPy.separator import Separator

from services.player_service import PlayerService
from services.champion_service import ChampionService

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
        question = [
            {
                "type": "list",
                "name": "choix",
                "message": "What are you looking for",
                "choices": infos_option,
            }
        ]
        champion_question = [
            {
                "type": "list",
                "name": "choix",
                "message": "What are you looking for",
                "choices": "Name Champion",
            }
        ]
        rank_champion_question = [
            {
                "type": "list",
                "name": "choix",
                "message": "What are you looking for",
                "choices": "Name Champion",
            }
        ]
        player_question = [
            {
                "type": "list",
                "name": "choix",
                "message": "What are you looking for",
                "choices": "Name Player",
            }
        ]
        self.__questions = questions
        self.__question = question
        self.infos_option = infos_option
        self.__champion_question = champion_question
        self.__rank_champion_question = rank_champion_question
        self.__player_question = player_question

    def display_info(self):
        print(f"") # a def

    def make_choice(self):
        answers = prompt(self.__questions)

        Session().user_identifiant = answers["identifiant"]
        Session().user_mdp = answers["password"]

        while True:
            answer = prompt(self.__question)

            if answer['choix'] == "Stats Champion" :
                instance = ChampionService()

                rep = prompt[self.__champion_question]
                stats_champion = rep['choix']
                stats_champion = instance.afficher_stat_player(stats_champion)
                print (stats_champion)

            elif answer['choix'] == "Ranking Champion" :
                print ("RC")

            elif answer['choix'] == "Stats Player" :
                instance = PlayerService()

                rep = prompt(self.__player_question)
                stats_player = rep['choix']
                stats_player = instance.afficher_stat_player(stats_player)
                print (stats_player)
            
            else :
                instance = PlayerService()
                stats_player = instance.afficher_stat_player(answers["identifiant"])
                print (stats_player)

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