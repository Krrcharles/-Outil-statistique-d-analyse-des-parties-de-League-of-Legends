import sqlite3
from typing import List
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
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        #Liste des champions classés par popularité (nombre total de games joués)
        query=  """ SELECT championName as Champion, COUNT(*) AS total_parties       
                    FROM participant                  
                    GROUP BY championName              
                    ORDER BY total_parties DESC   
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



    
#Exemple d'utilisation
particip_dao = participantDAO()
result = particip_dao.find_best_champ()
print(result)
