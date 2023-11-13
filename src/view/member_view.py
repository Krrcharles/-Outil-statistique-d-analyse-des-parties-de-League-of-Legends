from InquirerPy import prompt
from InquirerPy.separator import Separator

from src.services.connexion_services import Connexion_services
from src.services.player_service import PlayerService
from src.services.champion_service import ChampionService

from src.view.invite_view import InviteView
from src.view.session import Session


class MemberView(InviteView):
    def __init__(self):
        super().__init__()
        self.infos_option.append(Separator("🔍"))
        self.infos_option.append("Stats Account")
        self.__question = [{
                "type": "list",
                "name": "choix",
                "message": f"Hello {Session().user_identifiant}. What are you looking for",
                "choices": self.infos_option,
            },
        ]


    def display_info(self):
        print(f"") # a def

    def make_choice(self):
        answer = prompt(self.__question)

        if answer['choix'] == "Stats Champion" :
            print("?")

        elif answer['choix'] == "Ranking Champion" :
            from src.view.stats_ranking_champion import RankingChampion

            return RankingChampion()

        elif answer['choix'] == "Stats Player" :
            from src.view.stats_player import StatsPlayer
            # question : est-ce qu'on rédirige vers la vue classique stats_player
            #  ou on en créer une nouvelle afin de revenir sur la vue membre après ? 
            # (de même pour admin)
            return StatsPlayer()
            
        else :
            instance = PlayerService()
            name_account = Session().user_identifiant
            stats_player = instance.afficher_stat_player(name_account)
            print(stats_player)


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



