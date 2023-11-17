from src.business.player.player import Player
from src.dao.playerDAO import PlayerDAO
from src.dao.participantDAO import ParticipantDAO


class PlayerService():
    def afficher_parties(self, player):
        """
        Affiche les informations des parties d'un joueur.

        Parameters
        ----------
        player : str
            Le nom du joueur.
        """
        if not isinstance(player, str):
            print("Le critère n'est pas une chaine de caractère")
            return False

        liste_parties = ParticipantDAO().getpartie(player)

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
        if not isinstance(player, str):
            print("Le critère n'est pas une chaine de caractère")
            return False

        P = PlayerDAO().find_player_by_name(player)

        if P is None:
            print("Le pseudo n'est pas dans la base de données.")
            return False

        winrate = round(P._win / (P._win + P._losses) * 100)
        if P._rank == "I":
            rank = "Challenger"

        affichage_top = f"{P._name} - Level {P._level} - {rank}"
        affichage_bot = f"\t{P._win} Victoires / {P._losses} Défaite ({winrate}%)"

        max_lenght = max(len(affichage_top), len(affichage_bot) + 8)
        separateur = "+" + "-" * max_lenght + "+"
        affichage_top = "|" + affichage_top + " " * (max_lenght - len(affichage_top)) + "|"
        affichage_bot = "|" + affichage_bot + " " * (max_lenght - len(affichage_bot) - 6) + "|"

        affichage_finale = f"{separateur}\n{affichage_top}\n{affichage_bot}\n{separateur}"
        return(affichage_finale)
