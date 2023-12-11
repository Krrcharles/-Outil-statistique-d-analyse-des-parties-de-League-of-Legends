from src.utils.singleton import Singleton
from src.dao.participantDAO import ParticipantDAO

class ChampionService(metaclass=Singleton):
    """
    Service class for generating champion rankings based on different criteria.
    Implements the Singleton design pattern.
    """

    def classement_champion(self, critere):
        """
        Returns a ranking of the best champions based on a specified criterion.

        Parameters
        ----------
        critere : str
            Criterion selectable among "Per_game", "Per_winrate", "Per_KDA",
            "Per_gold", "Per_lane", "Per_other_stat".
        
        Returns
        -------
        str
            Formatted ranking string based on the criterion.
        """
        if not isinstance(critere, str):
            return "Le critère n'est pas une chaine de caractère"

        classement = ParticipantDAO().find_best_champ(critere)
        if not classement:
            return "Mauvais critère"

        # Base display setup
        affichage = f"| Voici le classement des champions par {critere} |"
        separateur = "+" + "-" * (len(affichage) - 2) + "+"
        affichage_finale = f"{separateur}\n{affichage}\n{separateur}"

        for i in range(min(10, len(classement))):
            champion_nom = classement[i][0]
            champion_critere = classement[i][1]

            ligne = f"| {champion_nom} : {champion_critere} "
            if critere == "Per_game":
                ligne += "parties jouées"
            elif critere == "Per_winrate":
                ligne += "% de parties gagnées"
            elif critere == "Per_KDA":
                ligne += "de KDA"
            elif critere == "Per_gold":
                ligne += "golds par minute"
            
            ligne = ligne.ljust(len(affichage) - 2) + "|"
            affichage_finale += f"\n{ligne}"

        affichage_finale += f"\n{separateur}"
        return affichage_finale

    def stat_champion(self, champ):
        """
        Print and return the statistics of a specific champion.

        Parameters
        ----------
        champ : str
            Name of the champion.
        
        Returns
        -------
        bool
            False always, indicating the end of the method.
        """
        if not isinstance(champ, str):
            print("Le champion n'est pas une chaine de caractère")
            return False

        champion = ParticipantDAO().stat_champ_by_name(champ)
        if champion[0] is None:
            print("Le champion n'éxiste pas")
            return False

        affichage = f"| {champion[0]} {round(champion[2], 2)}% WIN - {champion[3]} KDA - {champion[4]} Golds/min |"
        separateur = "+" + "-" * (len(affichage) - 2) + "+"
        affichage_finale = f"{separateur}\n{affichage}\n{separateur}"

        print(affichage_finale)
        return False
