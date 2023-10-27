from typing import List, Union
from utils.singleton import Singleton
from src.dao.participantDAO import participantDAO


class ChampionService(metaclass=Singleton):
    """
    """
    def classement_champion():
        """
        Renvoyer un classement des meilleurs champions
        """
        critere_affichage=["Per_game","Per_winrate","Per_KDA","Per_gold","Per_lane","Per_other_stat"]
        classement = participantDAO().find_best_champ("Per_winrate")
        
        
        
        
        pass

