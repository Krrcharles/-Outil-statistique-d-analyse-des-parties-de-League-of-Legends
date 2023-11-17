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

        elif type(liste_parties) is tuple:
            kda = (float(liste_parties[3]) + float(liste_parties[5])) / float(liste_parties[4])
            if liste_parties[2] == 1:
                win = "Victoire"
            else:
                win = "Défaite"

            affichage_top = f"{liste_parties[0]} - {liste_parties[1]} - {win}"
            affichage_mid = f"{liste_parties[3]}/{liste_parties[4]}/{liste_parties[5]} ({kda} KDA) - {liste_parties[6]} dégats"
            affichage_bot = f"{liste_parties[7]} gold par minutes"

            max_lenght = max(len(affichage_top), len(affichage_mid), len(affichage_bot))

            separateur = "+" + "-" * max_lenght + "+"
            affichage_top = "|" + affichage_top + " " * (max_lenght - len(affichage_top)) + "|"
            affichage_mid = "|" + affichage_mid + " " * (max_lenght - len(affichage_mid)) + "|"
            affichage_bot = "|" + affichage_bot + " " * (max_lenght - len(affichage_bot)) + "|"

            affichage_finale = f"{separateur}\n{affichage_top}\n{affichage_mid}\n{affichage_bot}\n{separateur}"

        else:
            affichage_finale = ""

            for partie in liste_parties:
                kda = round((float(partie[3]) + float(partie[5])) / float(partie[4]), 2)
                if partie[2] == 1:
                    win = "Victoire"
                else:
                    win = "Défaite"

                affichage_top = f"{partie[0]} - {partie[1]} - {win}"
                affichage_mid = f"{partie[3]}/{partie[4]}/{partie[5]} ({kda} KDA) - {partie[6]} dégats"
                affichage_bot = f"{partie[7]} gold par minutes"

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
        print(affichage_finale)
        return False

