from InquirerPy import prompt
from InquirerPy.separator import Separator

from src.view.abstract_view import AbstractView
from src.view.session import Session
from src.view.connexion_view import ConnexionView
from src.services.player_service import PlayerService 

class StatsPlayer(AbstractView):
    def __init__(self):
        infos_option = [
            Separator("📰"),
            "Games Infos",
            Separator("👑"),
            "Ranking Champion",
        ]
        self.infos_option = infos_option
        self.__question = [
            {
                "type": "list",
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

        answer = prompt(self.__question)

        if answer['choix'] == "Games Infos" :
            name_player = answer['Name Player']
            

