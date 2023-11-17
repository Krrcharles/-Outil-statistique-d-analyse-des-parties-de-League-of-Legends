from typing import List, Union

from utils.singleton import Singleton
    
    
    
class StatsGames(metaclass = Singleton) : 
    
    def consult_game_stat (self, id_player,id_game) -> dict :
        pass