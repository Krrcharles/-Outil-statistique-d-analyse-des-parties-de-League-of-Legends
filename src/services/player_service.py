from src.business.player.player import Player
from src.dao.playerDAO import PlayerDAO


class PlayerService(): 
    def afficher_parties(self, player: Player):
        """
        """

        pass

    def afficher_stat_player(self, player):
        """
        """
        P = PlayerDAO().find_player(player)

        winrate = round(P._win / (P._win + P._losses) * 100)
        if P._rank == "I":
            rank = "Challenger"
        
        cote = "|"
        coins = "+"
        
        affichage_top = f"{P._name} - Level {P._level} - {rank}"
        affichage_bot= f"\t{P._win} Victoires / {P._losses} Défaite ({winrate}%)"

        max_lenght = max(len(affichage_top), len(affichage_bot) + 8)
        separateur = coins + "-" * max_lenght + coins
        affichage_top = cote + affichage_top + " " * (max_lenght - len(affichage_top)) + cote
        affichage_bot = cote + affichage_bot + " " * (max_lenght - len(affichage_bot) - 6) + cote

        print(separateur)
        print(affichage_top)
        print(affichage_bot)
        print(separateur)
        #affichage_finale = f"{separateur}\n{affichage_top}\n{affichage_bot}\n{separateur}"
        #return affichage_finale

PlayerService().afficher_stat_player("T1 FSZ")
PlayerService().afficher_stat_player("BurgerMäker")
