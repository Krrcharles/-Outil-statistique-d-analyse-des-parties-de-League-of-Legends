from src.utils.singleton import Singleton
from src.dao.participantDAO import ParticipantDAO


class ChampionService(metaclass=Singleton):
    def classement_champion(self, critere):
        """
        Renvoie un classement des meilleurs champions selon un critère.

        Parameters
        ----------
        critere : str
            Critère selectionable parmis "Per_game", "Per_winrate", "Per_KDA",
            "Per_gold","Per_lane","Per_other_stat"
        """
        if not isinstance(critere, str):
            print("Le critère n'est pas une chaine de caractère")
            return False

        if critere == "Per_game":
            classement = ParticipantDAO().find_best_champ(critere)
            affichage = "| Voici le classement des champions par parties jouées |"

            separateur = "+" + "-" * (len(affichage) - 2) + "+"
            affichage_finale = f"{separateur}\n{affichage}\n{separateur}"

            for i in range(0, 9):
                champion_info = classement[i].split(', ')
                champion_nom = champion_info[0].split(': ')[1]
                champion_critere = champion_info[1].split(': ')[1]

                espaces_debut = (len(affichage) - len(f"| {champion_nom} : {champion_critere} parties jouées")) // 2
                espaces_fin = len(affichage) - len(f"| {champion_nom} : {champion_critere} parties jouées") - espaces_debut
                nouvelle_ligne = f"|{' ' * espaces_debut}{champion_nom} : {champion_critere} parties jouées{' ' * espaces_fin}|"
                affichage_finale = f"{affichage_finale}\n{nouvelle_ligne}"

            affichage_finale = f"{affichage_finale}\n{separateur}"

        elif critere == "Per_winrate":
            classement = ParticipantDAO().find_best_champ(critere)
            affichage = "| Voici le classement des champions par winrate |"

            separateur = "+" + "-" * (len(affichage) - 2) + "+"
            affichage_finale = f"{separateur}\n{affichage}\n{separateur}"

            for i in range(0, 9):
                champion_info = classement[i].split(', ')
                champion_nom = champion_info[0].split(': ')[1]
                champion_critere = champion_info[3].split(': ')[1]

                espaces_debut = (len(affichage) - len(f"| {champion_nom} : {champion_critere}% de parties gagnés")) // 2
                espaces_fin = len(affichage) - len(f"| {champion_nom} : {champion_critere}% de parties gagnés") - espaces_debut
                nouvelle_ligne = f"|{' ' * espaces_debut}{champion_nom} : {champion_critere}% de parties gagnés{' ' * espaces_fin}|"
                affichage_finale = f"{affichage_finale}\n{nouvelle_ligne}"
            affichage_finale = f"{affichage_finale}\n{separateur}"

        elif critere == "Per_KDA":
            classement = ParticipantDAO().find_best_champ(critere)
            affichage = "| Voici le classement des champions par KDA |"

            separateur = "+" + "-" * (len(affichage) - 2) + "+"
            affichage_finale = f"{separateur}\n{affichage}\n{separateur}"

            for i in range(0, 9):
                champion_info = classement[i].split(', ')
                champion_nom = champion_info[0].split(': ')[1]
                champion_critere = champion_info[1].split(': ')[1]

                espaces_debut = (len(affichage) - len(f"| {champion_nom} : {champion_critere} de KDA")) // 2
                espaces_fin = len(affichage) - len(f"| {champion_nom} : {champion_critere} de KDA") - espaces_debut
                nouvelle_ligne = f"|{' ' * espaces_debut}{champion_nom} : {champion_critere} de KDA{' ' * espaces_fin}|"
                affichage_finale = f"{affichage_finale}\n{nouvelle_ligne}"
            affichage_finale = f"{affichage_finale}\n{separateur}"

        elif critere == "Per_gold":
            classement = ParticipantDAO().find_best_champ(critere)
            affichage = "| Voici le classement des champions par gold gagnés |"

            separateur = "+" + "-" * (len(affichage) - 2) + "+"
            affichage_finale = f"{separateur}\n{affichage}\n{separateur}"

            for i in range(0, 9):
                champion_info = classement[i].split(', ')
                champion_nom = champion_info[0].split(': ')[1]
                champion_critere = champion_info[1].split(': ')[1]

                espaces_debut = (len(affichage) - len(f"| {champion_nom} : {champion_critere} golds par minute")) // 2
                espaces_fin = len(affichage) - len(f"| {champion_nom} : {champion_critere} golds par minute") - espaces_debut
                nouvelle_ligne = f"|{' ' * espaces_debut}{champion_nom} : {champion_critere} golds par minute{' ' * espaces_fin}|"
                affichage_finale = f"{affichage_finale}\n{nouvelle_ligne}"
            affichage_finale = f"{affichage_finale}\n{separateur}"

        else:
            print("Mauvais critère")
            return False

        print(affichage_finale)
        return False

# ChampionService().classement_champion("Per_game")
# ChampionService().classement_champion("Per_winrate")
# ChampionService().classement_champion("Per_KDA")
# ChampionService().classement_champion("Per_gold")
