from src.business.player.player import Player
from src.dao.playerDAO import PlayerDAO
from src.dao.participantDAO import participantDAO

class PlayerService():
    """
    Cette classe fournit des services pour afficher les informations des parties et des statistiques d'un joueur.
    """
    def afficher_parties(self, player: Player):
        """
        Affiche les informations des parties d'un joueur.

        Parameters
        ----------
        player : Player
            Un objet Player représentant le joueur.
        """
        # Listes de participant
        liste_parties = participantDAO().getpartie(player.summonerID)

        for partie in liste_parties:
            kda = (partie.kills + partie.assists) / partie.deaths
            po = partie.goldEarned / partie.gameDuration

            affichage_top = f"{partie.championName} - {partie.lane} - {partie.win}"
            affichage_mid = f"{partie.kills}/{partie.deaths}/{partie.assists} ({kda} KDA) - {partie.totalDamageDone} dégats"
            affichage_bot = f"{po} gold par minutes"

            max_lenght = max(len(affichage_top), len(affichage_mid), len(affichage_bot))
            separateur = "+" + "-" * max_lenght + "+"
            affichage_top = "|" + affichage_top + " " * (max_lenght - len(affichage_top)) + "|"
            affichage_mid = "|" + affichage_mid + " " * (max_lenght - len(affichage_mid)) + "|"
            affichage_bot = "|" + affichage_bot + " " * (max_lenght - len(affichage_bot) - 6) + "|"

            affichage_finale = f"{affichage_finale}\n{separateur}\n{affichage_top}\n{affichage_mid}\n{affichage_bot}\n{separateur}"

        print(affichage_finale)
        return False

    def afficher_stat_player(self, player):
        """
        Affiche les statistiques d'un joueur.

        Parameters
        ----------
        player : str
            Le nom du joueur.
        """
        P = PlayerDAO().find_player_by_name(player)

        winrate = round(P._win / (P._win + P._losses) * 100)
        if P._rank == "I":
            rank = "Challenger"

        affichage_top = f"{P._name} - Level {P._level} - {rank}"
        affichage_bot= f"\t{P._win} Victoires / {P._losses} Défaite ({winrate}%)"

        max_lenght = max(len(affichage_top), len(affichage_bot) + 8)
        separateur = "+" + "-" * max_lenght + "+"
        affichage_top = "|" + affichage_top + " " * (max_lenght - len(affichage_top)) + "|"
        affichage_bot = "|" + affichage_bot + " " * (max_lenght - len(affichage_bot) - 6) + "|"

        
        affichage_finale = f"{separateur}\n{affichage_top}\n{affichage_bot}\n{separateur}"
        print(affichage_finale)
        return False

#PlayerService().afficher_stat_player("TwTv Raideru")
