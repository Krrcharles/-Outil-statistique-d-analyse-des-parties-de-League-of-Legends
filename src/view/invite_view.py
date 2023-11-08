from InquirerPy import prompt
from InquirerPy.separator import Separator
from src.services.player_service import PlayerService
from src.services.champion_service import ChampionService


from src.view.abstract_view import AbstractView
from src.view.session import Session


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
        self.__question = [
            {
                "type": "list",
                "name": "choix",
                "message": "What are you looking for",
                "choices": self.infos_option,
            }
        ]
        self.__champion_question = [
            {
                "type": "list",
                "name": "choix",
                "message": "What are you looking for",
                "choices": "Name Champion",
            }
        ]
        self.__rank_champion_question = [
            {
                "type": "list",
                "name": "choix",
                "message": "What are you looking for",
                "choices": "Name Champion",
            }
        ]
        self.__player_question = [
            {
                "type": "list",
                "name": "Name Player",
                "message": "What are you looking for",
            }
        ]
        

    def display_info(self):
        print(f"") # a def

    def make_choice(self): 

        while True:
            answer = prompt(self.__question)

            if answer['choix'] == "Stats Champion" :
                instance = ChampionService()

                rep = prompt[self.__champion_question]
                # stats_champion = rep['choix']
                # stats_champion = instance.afficher_stat_player(stats_champion)
                # print (stats_champion)

            elif answer['choix'] == "Ranking Champion" :
                print ("RC")

            else :
                instance = PlayerService()

                rep = prompt(self.__player_question)
                # stats_player = rep['Name Player']
                # stats_player = instance.afficher_stat_player(stats_player)
                # print (stats_player)

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
