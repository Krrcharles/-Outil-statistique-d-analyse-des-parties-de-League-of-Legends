from InquirerPy import prompt

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
            Separator("📰"),
            "Per_KDA",
            Separator("👑"),
            "Per_gold",    
            Separator("👑"),
            "Per_lane",   
            Separator("👑"),
            "Per_other_stat",    
        ]
        self.__question = [
            {
                "type": "input",
                "name": "Name Champion",
                "message": "Which champion are you looking for",
            },
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
            from src.view.stats_ranking_champions import RankingChampion

            return RankingChampion()

        else:
            from src.view.invite_view import InviteView

            return InviteView()