from InquirerPy import prompt
from InquirerPy.separator import Separator

from src.services.player_service import PlayerService
from src.services.champion_service import ChampionService

from src.view.member_view import MemberView
from src.view.session import Session


class AdminView(MemberView):
    def __init__(self):
        super().__init__()
        self.infos_option.append(Separator("⚙️"))
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
        Session().not_admin == "no"

        if answer['choix'] == "Stats Champion" :
            from src.view.stats_champion import StatsChampion

            return StatsChampion()


        elif answer['choix'] == "Ranking Champion" :
            from src.view.stats_ranking_champion import RankingChampion

            return RankingChampion()

        elif answer['choix'] == "Stats Player" :
            from src.view.stats_player import StatsPlayer
            return StatsPlayer()
            
        elif answer['choix'] == "Stats Account" :
            instance = PlayerService()
            name_account = Session().user_identifiant
            stats_player = instance.afficher_stat_player(name_account)
            print(stats_player)

        elif answer['choix'] == "Modification" :
            from src.services.admin_service import AdminService
            new_player_name = input("Rentrez un nom d'invocateur : ")
            api_key = input("Rentrez votre API KEY : ")
            AdminService().add_player(new_player_name, api_key)
            return AdminView()

        else :
            from src.view.start_view import StartView

            return StartView()


       