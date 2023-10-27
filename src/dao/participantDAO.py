#import psycopg2
import sqlite3
from typing import List
#from src.dao.db_connection import AbstractDAO
from src.utils.singleton import Singleton
import os

class participantDAO(metaclass=Singleton):
    """
    Communicate with the participant table
    """

    def __init__(self, db_file='data/database.db'):

        """
        Initialize the class with the name of the SQLite database file.

        Parameters:
        db_name (str): Name of the SQLite database file.
        """
        self.db_file = db_file


    def find_best_champ(self) -> List[str]:
        """
        Get all champions by winrate return a list
        
        :return: A list of winrate for champions
        :rtype: List of str
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        #Liste des champions classés par popularité (nombre total de games joués)
        query=  """ SELECT championName as Champion, COUNT(*) AS total_parties       
                    FROM participant                  
                    GROUP BY championName              
                    ORDER BY total_parties  DESC;    
                """ 
        cursor.execute(query)
        results = cursor.fetchall()   # Récupérer les résultats de la requête
        print(results)
        statpop: List[str] = []  # Pour stocker les statistiques
        # Pour chaque résultat, créer une chaîne de statistiques et l'ajouter à la liste
        
        
         # if the SQL query returned results (ie. res not None)
        for row in results:
            print(row)
            champion_name, total_parties = row
            stat_str = f"Champion: {champion_name}, Total Parties: {total_parties}"
            statpop.append(stat_str)

        return statpop


if __name__ == '__main':
    # Pour charger les variables d'environnement contenues dans le fichier .env
    import dotenv

    dotenv.load_dotenv(override=True)

    # Créez une instance de participantDAO
    my_dao = participantDAO()

    # Appelez la méthode find_best_champ pour obtenir la liste des champions par popularité
    champions_popularity = my_dao.find_best_champ()
    
     # Affichez les résultats
    # for champ_stats in champions_popularity:
    #     print(champ_stats)
