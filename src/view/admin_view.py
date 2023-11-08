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
        self.infos_option.append("Modification") 
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

        elif answer['choix'] == "Stats Champion" :
            from src.view.stats_champion import StatsChampion
            return StatsChampion()

        else :
            from src.view.modification import Modification

            return Modification()


       