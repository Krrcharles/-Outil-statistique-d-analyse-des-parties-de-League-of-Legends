from src.business.player.player import Player


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

        affichage = f"{player._name} - Level {player._level} - {player._rank}\n\t{player._win} - {player._losses} ({winrate}%)"

        print(affichage)
