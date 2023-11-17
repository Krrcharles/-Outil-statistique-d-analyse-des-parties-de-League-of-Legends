from InquirerPy import prompt
from InquirerPy.separator import Separator

from src.view.abstract_view import AbstractView
from src.view.session import Session
from src.services.champion_service import ChampionService

class StatsChampion(AbstractView):
    def __init__(self):
        pass
    
    def display_info(self):
        pass
    
    def make_choice(self): 
        champ = input("Enter champion name")
        ChampionService().stat_champion(champ)

        choice = prompt(
            [
                {
                    "type": "confirm",
                    "name": "yes",
                    "message": "Do you want to get another information about another champion ?",
                    "default": True,
                }
            ]
        )

        if choice["yes"]:
            from src.view.stats_player import StatsPlayer

            return StatsChampion()

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
    
    