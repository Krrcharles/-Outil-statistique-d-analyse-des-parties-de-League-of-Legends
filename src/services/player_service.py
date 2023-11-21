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

        if liste_parties is None:
            print("Ce joueur n'a pas de partie dans la base de données")
            return False

        affichage_finale = ""

        for partie in liste_parties:
            kda = round((float(partie._kills[0]) + float(partie._assists[0])) / float(partie._death[0]), 2)
            gold_min = round(partie._goldEarned[0] / partie._gameDuration, 2)
            if partie._win[0] == 1:
                win = "Victoire"
            else:
                win = "Défaite"

            affichage_top = f"{partie._championName[0]} - {partie._lane[0]} - {win}"
            affichage_mid = f"{partie._kills[0]}/{partie._death[0]}/{partie._assists[0]} ({kda} KDA) - {partie._totalDamageDealtToChampions[0]} dégats"
            affichage_bot = f"{gold_min} gold par minutes"

            max_lenght = max(len(affichage_top), len(affichage_mid), len(affichage_bot))

            separateur = "+" + "-" * max_lenght + "+"
            affichage_top = "|" + affichage_top + " " * (max_lenght - len(affichage_top)) + "|"
            affichage_mid = "|" + affichage_mid + " " * (max_lenght - len(affichage_mid)) + "|"
            affichage_bot = "|" + affichage_bot + " " * (max_lenght - len(affichage_bot)) + "|"

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
            return "Le critère n'est pas une chaine de caractère"

        P = PlayerDAO().find_player_by_name(player)

        if P is None:
            return "Le pseudo n'est pas dans la base de données."

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
        return affichage_finale
