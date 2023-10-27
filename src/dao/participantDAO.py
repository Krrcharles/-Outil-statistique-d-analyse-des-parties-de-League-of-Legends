import psycopg2

from typing import Optional
from src.dao.db_connection import AbstractDAO
from src.utils.singleton import Singleton

class participantDAO(metaclass=Singleton):
    """
    Communicate with the player table
    """

    def find_all_statistics(self) -> list[str]:
        """
        Get all statistics return a list
        
        :return: A list of the statistics of the participant
        :rtype: List of str
        """
        statistics = []  # Pour stocker les statistiques

        with AbstractDAO.connection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                        "SELECT                                          "
                        "       championName,                            "
                        "       COUNT(*) AS total_parties,               "
                        "       SUM(win) AS parties_gagnees,             "
                        "       (SUM(win) * 1.0 / COUNT(*)) AS winrate   "
                        "       FROM participant                         "
                        "       GROUP BY championName ;                  "
                        )

    
# Récupérer les résultats de la requête
            results = cursor.fetchall()

            # Pour chaque résultat, créer une chaîne de statistiques et l'ajouter à la liste
            for result in results:
                champion_name, total_parties, parties_gagnees, winrate = result
                stat_str = f"Champion: {champion_name}, Total Parties: {total_parties}, Parties Gagnées: {parties_gagnees}, Winrate: {winrate}"
                statistics.append(stat_str)

        return statistics  # Retourner la liste des statistiques

if __name__ == "__main__":
    # Créez une instance de participantDAO
    dao = participantDAO()

    # Appelez la fonction find_all_statistics pour obtenir les statistiques
    statistics = dao.find_all_statistics()

    # Affichez les statistiques
    for stat in statistics:
        print(stat)