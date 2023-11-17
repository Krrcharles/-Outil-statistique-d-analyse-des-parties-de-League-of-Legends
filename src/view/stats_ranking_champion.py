from InquirerPy import prompt
from InquirerPy.separator import Separator

from src.view.abstract_view import AbstractView
from src.view.session import Session
from src.view.connexion_view import ConnexionView
from src.services.champion_service import ChampionService

class RankingChampion(AbstractView):
    def __init__(self):
        self.ranking_option = [
             Separator("📰"),
            "Per_game",
            Separator("👑"),
            "Per_winrate",
            Separator("🔪"),
            "Per_KDA",
            Separator("💰"),
            "Per_gold",        
        ]
        self.__question = [
            {
                "type": "list",
                "name": "type info",
                "message": "Which ranking are you looking for",
                "choices": self.ranking_option
            }
        ]

    def display_info(self):
        print(f"") # a def

    def make_choice(self): 
        
        answer = prompt(self.__question)
        choice = answer['type info']

        instance = ChampionService()

        print(instance.classement_champion(choice))

        choice = prompt(
            [
                {
                    "type": "confirm",
                    "name": "yes",
                    "message": "Do you want to get another information about a champion ?",
                    "default": True,
                }
            ]
        )


        if choice["yes"]:
            from src.view.stats_ranking_champion import RankingChampion

            return RankingChampion()

        else:
            if Session().user_identifiant != "unknown" :
                if Session().not_admin == "no" :
                    from src.view.admin_view import AdminView
                    Session().user_identifiant

                    return AdminView()
                
                else :
                    from src.view.member_view import MemberView
                    Session().user_identifiant

                    return MemberView()
            
            else :
                from src.view.invite_view import InviteView
                
                return InviteView()


        