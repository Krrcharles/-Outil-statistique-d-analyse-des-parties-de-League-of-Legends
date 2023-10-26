<<<<<<< HEAD
from src.business.player.player import Player

=======
from typing import List, Union
from src.business.player import Player
from utils.singleton import Singleton
>>>>>>> 8c26e7cb55eaadfe97d78e6778e37d9b89e4495d

class PlayerService(): 

    #def afficher_parties(self, player: Player):
    #    pass

    def afficher_stat_player(self, player):
        """
        """
        # Demander nom du player à la DAO
        P = Player('Teemo_du_666', '12', '13', 'gold', 12, 13, 178)
        PS = PlayerService()
        PS.afficher_stat_player(P)
        winrate = round(player._win / (player._win + player._losses) * 100)

<<<<<<< HEAD
        affichage = f"{player._name} - Level {player._level} - {player._rank}\n\t{player._win} - {player._losses} ({winrate}%)"
=======

    """ Il s'agit de la classe qui permet de récuperer les informations concernant un joueur """


    def afficher_parties_from_websites(self, name) : 
        """ 
        Fonction qui prend le nom d'un joueur et affiche ses dernières parties

        Parameters
        ----------
        name : nom du joueur 

        Return
        ------

        """
        
>>>>>>> 8c26e7cb55eaadfe97d78e6778e37d9b89e4495d

        print(affichage)
