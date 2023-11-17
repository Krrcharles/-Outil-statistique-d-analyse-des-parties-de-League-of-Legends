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
            Separator("📖"),
            "Stats Player",
            Separator("🚪"),
            "Disconnect",
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

    def display_info(self):
        print(f"") # a def

    def make_choice(self): 
        answer = prompt(self.__question)

        if answer['choix'] == "Stats Champion" :
            from src.view.stats_champion import StatsChampion

            return StatsChampion()


        elif answer['choix'] == "Ranking Champion" :
            from src.view.stats_ranking_champion import RankingChampion

            return RankingChampion()

        elif answer['choix'] == "Stats Player" :
            from src.view.stats_player import StatsPlayer

            return StatsPlayer()

        else : 
            from src.view.start_view import StartView

            return StartView()

