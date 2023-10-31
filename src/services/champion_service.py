from typing import List, Union
from src.utils.singleton import Singleton
from src.dao.participantDAO import participantDAO


class ChampionService(metaclass=Singleton) : 

    def classement_champion(self, critere):
        """
        Renvoyer un classement des meilleurs champions
        Critère = ["Per_game","Per_winrate","Per_KDA","Per_gold","Per_lane","Per_other_stat"]
        """
        if critere == "Per_game":
            classement = participantDAO().find_best_champ()
            affichage = "| Voici le classement des champions par parties jouées |"

            separateur = "+" + "-" * (len(affichage) - 2) + "+"
            affichage_finale = f"{separateur}\n{affichage}\n{separateur}"

            for i in range(0,9):
                champion_info = classement[i].split(', ')
                champion_nom = champion_info[0].split(': ')[1]
                champion_critere = champion_info[1].split(': ')[1]

                espaces_debut = (len(affichage) - len(f"| {champion_nom} : {champion_critere} parties jouées")) // 2
                espaces_fin = len(affichage) - len(f"| {champion_nom} : {champion_critere} parties jouées") - espaces_debut
                nouvelle_ligne = f"|{' ' * espaces_debut}{champion_nom} : {champion_critere} parties jouées{' ' * espaces_fin}|"
                affichage_finale = f"{affichage_finale}\n{nouvelle_ligne}"

            affichage_finale = f"{affichage_finale}\n{separateur}"

        elif critere == "Per_winrate":
            classement = participantDAO().find_champ_winrate()
            affichage = "| Voici le classement des champions par winrate |"

            separateur = "+" + "-" * (len(affichage) - 2) + "+"
            affichage_finale = f"{separateur}\n{affichage}\n{separateur}"

            for i in range(0,9):
                champion_info = classement[i].split(', ')
                champion_nom = champion_info[0].split(': ')[1]
                champion_critere = champion_info[3].split(': ')[1]

                espaces_debut = (len(affichage) - len(f"| {champion_nom} : {champion_critere}% de parties gagnés")) // 2
                espaces_fin = len(affichage) - len(f"| {champion_nom} : {champion_critere}% de parties gagnés") - espaces_debut
                nouvelle_ligne = f"|{' ' * espaces_debut}{champion_nom} : {champion_critere}% de parties gagnés{' ' * espaces_fin}|"
                affichage_finale = f"{affichage_finale}\n{nouvelle_ligne}"
            affichage_finale = f"{affichage_finale}\n{separateur}"

        elif critere == "Per_gold":
            classement = participantDAO().find_champ_other()
            affichage = "| Voici le classement des champions par gold gagnés |"

            separateur = "+" + "-" * (len(affichage) - 2) + "+"
            affichage_finale = f"{separateur}\n{affichage}\n{separateur}"

            for i in range(0,9):
                champion_info = classement[i].split(', ')
                champion_nom = champion_info[0].split(': ')[1]
                champion_critere = champion_info[2].split(': ')[1]

                espaces_debut = (len(affichage) - len(f"| {champion_nom} : {champion_critere} gold gagnés")) // 2
                espaces_fin = len(affichage) - len(f"| {champion_nom} : {champion_critere} gold gagnés") - espaces_debut
                nouvelle_ligne = f"|{' ' * espaces_debut}{champion_nom} : {champion_critere} gold gagnés{' ' * espaces_fin}|"
                affichage_finale = f"{affichage_finale}\n{nouvelle_ligne}"
            affichage_finale = f"{affichage_finale}\n{separateur}"

        else:
            print("Mauvais critère")
            return False

        print(affichage_finale)
        return False

#ChampionService().classement_champion("Per_game")
#ChampionService().classement_champion("Per_winrate")
#ChampionService().classement_champion("Per_gold")