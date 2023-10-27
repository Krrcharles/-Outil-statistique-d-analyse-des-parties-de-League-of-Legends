import psycopg2

from typing import Optional
from src.dao.db_connection import AbstractDAO
from src.utils.singleton import Singleton

class participantDAO(metaclass=Singleton):
    """
    Communicate with the participant table
    """

    def find_best_champ(self) -> list[str]:
        """
<<<<<<< HEAD
        Get all champions by winrate return a list
        
        :return: A list of winrate for champions
        :rtype: List of str
        """
        
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
=======
        Get all statistics return a list

        :return: A list of the statistics of the participant
        :rtype: List of str
        """
        with AbstractDAO.connection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT *                                  "
                    "  FROM data                  "
                )

                # to store raw results
                res = cursor.fetchall()

        # Create an empty list to store formatted results
        participant_stat: list[str] = []

        # if the SQL query returned results (ie. res not None)
        if res:
            for row in res:
                participant_stat.append(row["summonerName"])

                print(row["summonerId"])

        return participant_stat

    def find_id_by_label(self, label: str) -> Optional[int]:
        """
        Get the id_participant from the label
        """
        with connection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT summonerId                  "
                    "  FROM data                       "
                    " WHERE summonerId = %(summonerId)s ",
                    {"participant": label},
                )
                res = cursor.fetchone()

        if res:
            return res["summonerId"]


if __name__ == "__main__":
    # Pour charger les variables d'environnement contenues dans le fichier .env
    import dotenv

    dotenv.load_dotenv(override=True)

    participant= participantDAO().find_all_statistics()
    print(participant)
>>>>>>> a0ad2831ef815b3077e62f8d4c1681e224eaaca4
