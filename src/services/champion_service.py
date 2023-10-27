from typing import List, Union
from src.utils.singleton import Singleton
from src.dao.participantDAO import participantDAO


class ChampionService(metaclass=Singleton):
    """
    """
    def classement_champion(critère):
        """
        Renvoyer un classement des meilleurs champions

        Critère = ["Per_game","Per_winrate","Per_KDA","Per_gold","Per_lane","Per_other_stat"]
        """
        classement = participantDAO().find_best_champ(critere)
        
        
        print(classement)
        return False

# A=ChampionService
# A.classement_champion("Per_winrate")