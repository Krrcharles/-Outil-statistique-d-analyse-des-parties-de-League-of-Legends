import psycopg2

from typing import List, Optional
from src.dao.db_connection import AbstractDAO
from src.utils.singleton import Singleton

class participantDAO(metaclass=Singleton):
    """
    Communicate with the participant table
    """

    def __init__(self, db_name='data/database.db'):

        """
        Initialize the class with the name of the SQLite database file.

        Parameters:
        db_name (str): Name of the SQLite database file.
        """
        self.db_name = db_name


    def find_best_champ(self) -> list[str]:
        """
        Get all champions by winrate return a list
        
        :return: A list of winrate for champions
        :rtype: List of str
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        with AbstractDAO().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                     #Liste des champions classés par popularité (nombre total de games joués)
                        " SELECT                             "
                        "    championName,                   " 
                        "    COUNT(*) AS total_parties       " 
                        " FROM participant                   "
                        " GROUP BY championName              "
                        " ORDER BY total_parties  DESC;      "
                        )
                results = cursor.fetchall()   # Récupérer les résultats de la requête
            statpop: list[str] = []  # Pour stocker les statistiques
            # Pour chaque résultat, créer une chaîne de statistiques et l'ajouter à la liste
        for result in results:
                champion_name, total_parties=result
                stat_str = f"Champion: {champion_name}, Total Parties: {total_parties}"
                statpop.append(stat_str)

        return statpop  # Retourner la liste des statistiques



    def find_champ_winrate(self) -> list[str]:
        """
        Get all champions by winrate return a list
        
        :return: A list of winrate for champions
        :rtype: List of str
        """

        with AbstractDAO().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                        "SELECT                                                   "
                        "       championName,                                     "
                        "       COUNT(*) AS total_parties,                        "
                        "       SUM(win) AS parties_gagnees,                      "
                        "       ROUND((SUM(win) * 1.0 / COUNT(*)),3) AS winrate   "
                        "       FROM participant                                  "
                        "       GROUP BY championName                             "
                        "       ORDER BY winrate DESC;                            "
                    )

                results = cursor.fetchall()   # Récupérer les résultats de la requête
            statwin: list[str] = []  # Pour stocker les statistiques
            # Pour chaque résultat, créer une chaîne de statistiques et l'ajouter à la liste
        for result in results:
                champion_name, total_parties, parties_gagnees, winrate = result
                stat_str = f"Champion: {champion_name}, Total Parties: {total_parties}, Parties Gagnées: {parties_gagnees}, Winrate: {winrate}"
                statwin.append(stat_str)

        return statwin  # Retourner la liste des statistiques

    
    
    def find_champ_lane(self) -> list[str]:
        """
        Get all lane by total games played in the lane and winrate return a list
        
        :return: A list of winrate and total games played by lane
        :rtype: List of str
        """

        with AbstractDAO().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    " SELECT                                              "
                    "    lane,                                            "
                    "   COUNT(*) AS total_parties,                        "
                    "   ROUND((SUM(win) * 1.0 / COUNT(*)),3) AS winrate   "
                    " FROM participant                                    "
                    " GROUP BY lane                                       " 
                    " ORDER BY total_parties DESC;                        "
                )
                
                results = cursor.fetchall()   # Récupérer les résultats de la requête
            statlane: list[str] = []  # Pour stocker les statistiques
            # Pour chaque résultat, créer une chaîne de statistiques et l'ajouter à la liste
        for result in results:
                lane, total_parties, winrate = result
                stat_str = f"Lane: {lane}, Total Parties: {total_parties}, Winrate: {winrate}"
                statlane.append(stat_str)

        return statlane  # Retourner la liste des statistiques


    
    def find_champ_other(self) -> list[str]:
        """
        Get all champions by total games played, total golds and total minions killed return a list
        
        :return: A list of champions and total games played, total golds and total minions killed
        :rtype: List of str
        """

        with AbstractDAO().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    " SELECT                                              "
                    "   championName,                                     "
                    "   COUNT(*) AS total_parties,                        "
                    "   SUM(goldEarned) AS total_gold,                    "
                    "    SUM(totalMinionsKilled) AS total_minions_killed  "
                    " FROM participant                                    "
                    " GROUP BY championName                               "
                    " ORDER BY total_parties DESC;                        "
                )
                
                results = cursor.fetchall()   # Récupérer les résultats de la requête
            statother: list[str] = []  # Pour stocker les statistiques
            # Pour chaque résultat, créer une chaîne de statistiques et l'ajouter à la liste
        for result in results:
                champion_name, total_parties, total_gold, total_minions_killed = result
                stat_str = f"Champion: {champion_name}, Total Parties: {total_parties}, Total Golds: {total_gold}, Total minions killed: {total_minions_killed}"
                statother.append(stat_str)

        return statother  # Retourner la liste des statistiques


if __name__ == '__main':
    # Pour charger les variables d'environnement contenues dans le fichier .env
    import dotenv

    dotenv.load_dotenv(override=True)

    # Créez une instance de participantDAO
    my_dao = participantDAO()

    # Appelez la méthode find_best_champ pour obtenir la liste des champions par popularité
    champions_popularity = my_dao.find_best_champ()
    
     # Affichez les résultats
    for champ_stats in champions_popularity:
        print(champ_stats)
