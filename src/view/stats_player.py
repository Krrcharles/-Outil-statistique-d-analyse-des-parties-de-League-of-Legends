from InquirerPy import prompt
from InquirerPy.separator import Separator

from src.view.abstract_view import AbstractView
from src.view.session import Session
from src.view.connexion_view import ConnexionView
from src.services.player_service import PlayerService 
from src.business.player.player import Player

class StatsPlayer(AbstractView):
    def __init__(self):
        infos_option = [
            Separator("📰"),
            "Games Infos",
            Separator("👑"),
            "Stats Player",
        ]
        self.infos_option = infos_option
        self.__questions = [
            {
                "type": "input",
                "name": "Name Player",
                "message": "Who are you looking for",
            },
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
        
        answer = prompt(self.__questions)

        if answer['choix'] == "Games Infos" :
            name_player = answer['Name Player']
            instance = PlayerService()
            player = Player(name_player)

            print(instance.afficher_parties(player))
        
        else :
            # problème : comment créer une instance de Player avec les données d'un player de la base
            name_player = answer['Name Player']
            instance = PlayerService()

            print(instance.afficher_stat_player(name_player))

        choice = prompt(
            [
                {
                    "type": "confirm",
                    "name": "yes",
                    "message": "Do you want to get another information about this player ?",
                    "default": True,
                }
            ]
        )

        if choice["yes"]:
            from src.view.stats_player import StatsPlayer

            return StatsPlayer()

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




