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
        statpop: List[str] = []  # Pour stocker les statistiques
        # Pour chaque résultat, créer une chaîne de statistiques et l'ajouter à la liste

         # if the SQL query returned results (ie. res not None)
        for row in results:
            print(row)
            champion_name, total_parties = row
            stat_str = f"Champion: {champion_name}, Total Parties: {total_parties}"
            statpop.append(stat_str)

        return statpop

    

    def find_champ_winrate(self) -> list[str]:
        """
        Get all champions by winrate return a list
        
        :return: A list of winrate for champions
        :rtype: List of str
        """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        query=  """SELECT championName, COUNT(*) AS total_parties, SUM(win) AS parties_gagnees, ROUND((SUM(win) * 1.0 / COUNT(*)),3) AS winrate
                   FROM participant                                 
                   GROUP BY championName                             
                   ORDER BY winrate DESC                           
                """
        cursor.execute(query)
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
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        query= """ SELECT lane, COUNT(*) AS total_parties, ROUND((SUM(win) * 1.0 / COUNT(*)),3) AS winrate
                   FROM participant                                    
                   GROUP BY lane                                       
                   ORDER BY total_parties DESC                        
                """
        cursor.execute(query)        
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
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        query=  """ SELECT championName, COUNT(*) AS total_parties, SUM(goldEarned) AS total_gold, SUM(totalMinionsKilled) AS total_minions_killed
                    FROM participant                                    
                    GROUP BY championName                               
                    ORDER BY total_parties DESC                      
                """
        cursor.execute(query)       
        results = cursor.fetchall()   # Récupérer les résultats de la requête
        statother: list[str] = []  # Pour stocker les statistiques
        # Pour chaque résultat, créer une chaîne de statistiques et l'ajouter à la liste
        for result in results:
                champion_name, total_parties, total_gold, total_minions_killed = result
                stat_str = f"Champion: {champion_name}, Total Parties: {total_parties}, Total Golds: {total_gold}, Total minions killed: {total_minions_killed}"
                statother.append(stat_str)

        return statother  # Retourner la liste des statistiques

    
#Exemple d'utilisation
particip_dao = participantDAO()
result = particip_dao.find_champ_other()
print(result)
