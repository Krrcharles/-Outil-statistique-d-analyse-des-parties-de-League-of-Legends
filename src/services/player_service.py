from src.dao.playerDAO import PlayerDAO
from src.dao.participantDAO import ParticipantDAO

class PlayerService:
    """
    Service class for displaying player-related information such as game details and statistics.
    """

    def afficher_parties(self, player):
        """
        Displays the information of the games played by a player.

        Parameters
        ----------
        player : str
            The name of the player.
        
        Returns
        -------
        str
            Formatted string of game information for the player.
        """
        if not isinstance(player, str):
            return "Le joueur n'est pas une chaine de caractère"

        liste_parties = ParticipantDAO().getpartie(player)
        if liste_parties is None:
            return "Ce joueur n'a pas de partie dans la base de données"

        affichage_finale = ""
        for partie in liste_parties:
            kda = ("Perfect" if partie._death == 0 else 
                   round((float(partie._kills) + float(partie._assists)) / float(partie._death), 2))
            gold_min = round(partie._goldEarned / partie._gameDuration, 2)
            win = "Victoire" if partie._win == 1 else "Défaite"

            affichage_top = f"{partie._championName} - {partie._lane} - {win}"
            affichage_mid = f"{partie._kills}/{partie._death}/{partie._assists} ({kda} KDA) - {partie._totalDamageDealtToChampions} dégats"
            affichage_bot = f"{gold_min} gold par minutes"

            max_length = max(len(affichage_top), len(affichage_mid), len(affichage_bot))
            separateur = "+" + "-" * max_length + "+"
            affichage_top = "|" + affichage_top.ljust(max_length) + "|"
            affichage_mid = "|" + affichage_mid.ljust(max_length) + "|"
            affichage_bot = "|" + affichage_bot.ljust(max_length) + "|"

            affichage_finale += f"{separateur}\n{affichage_top}\n{affichage_mid}\n{affichage_bot}\n{separateur}\n"

        return affichage_finale

    def afficher_stat_player(self, player):
        """
        Displays the statistics of a player.

        Parameters
        ----------
        player : str
            The name of the player.
        
        Returns
        -------
        str
            Formatted string of the player's statistics.
        """
        if not isinstance(player, str):
            return "Le critère n'est pas une chaine de caractère"

        P = PlayerDAO().find_player_by_name(player)
        if P is None:
            return "Le pseudo n'est pas dans la base de données."

        winrate = round(P._win / (P._win + P._losses) * 100)
        rank = "Challenger" if P._rank == "I" else P._rank

        affichage_top = f"{P._name} - Level {P._level} - {rank}"
        affichage_bot = f"\t{P._win} Victoires / {P._losses} Défaite ({winrate}%)"

        max_length = max(len(affichage_top), len(affichage_bot) + 8)
        separateur = "+" + "-" * max_length + "+"
        affichage_top = "|" + affichage_top.ljust(max_length) + "|"
        affichage_bot = "|" + affichage_bot.ljust(max_length - 6) + "|"

        affichage_finale = f"{separateur}\n{affichage_top}\n{affichage_bot}\n{separateur}"
        return affichage_finale
