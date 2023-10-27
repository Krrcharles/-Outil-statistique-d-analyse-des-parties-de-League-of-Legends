from src.business.player.player import Player
from src.dao.playerDAO import PlayerDAO
from src.dao.participantDAO import participantDAO

class PlayerService(): 
    def afficher_parties(self, player: Player):
        """
        
        """

        pass

    def afficher_stat_player(self, player):
        """
        """
        #P = PlayerDAO().find_player_by_name(player)
        player_dao = PlayerDAO()
        result = player_dao.find_player_by_name(player)

        winrate = round(result._win / (result._win + result._losses) * 100)
        if result._rank == "I":
            rank = "Challenger"
        
        cote = "|"
        coins = "+"
        
        affichage_top = f"{result._name} - Level {result._level} - {rank}"
        affichage_bot= f"\t{result._win} Victoires / {result._losses} Défaite ({winrate}%)"

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

PlayerService().afficher_stat_player("TwTv Raideru")
