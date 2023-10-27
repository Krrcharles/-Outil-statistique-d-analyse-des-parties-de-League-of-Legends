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
        self.critere_affichage=["Per_game","Per_winrate","Per_KDA","Per_gold","Per_lane","Per_other_stat"]

    def find_best_champ(self,critere) -> List[str]:
        """
        Get all champions by winrate return a list
        
        :return: A list of winrate for champions
        :rtype: List of str
        """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        if critere==self.critere_affichage[0]:   
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
                #print(row)
                champion_name, total_parties = row
                stat_str = f"Champion: {champion_name}, Total Parties: {total_parties}"
                statpop.append(stat_str)

            return statpop

        #Liste des champions classés par winrate (nombre de parties gagnées/nombre de parties jouées)
        elif critere==self.critere_affichage[1]:
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

        #Liste des champions suivant l'ordre décroissant de leur KDA (kills+assists)/deaths sur toutes leurs parties jouées
        elif critere==self.critere_affichage[2]:
            query= """SELECT championName , ROUND((kills + assists) / deaths,1) AS kda
                    FROM participant 
                    GROUP BY championName 
                    ORDER BY kda DESC 
                """
            cursor.execute(query)       
            results = cursor.fetchall()   # Récupérer les résultats de la requête
            statKDA: list[str] = []  # Pour stocker les statistiques
            # Pour chaque résultat, créer une chaîne de statistiques et l'ajouter à la liste
            for result in results:
                    champion_name, kda= result
                    stat_str = f"Champion: {champion_name}, KDA: {kda}"
                    statKDA.append(stat_str)

            return statKDA  # Retourner la liste des statistiques
        
        #Liste des champions suivant l'ordre décroissant de leur gold par minute
        elif critere==self.critere_affichage[3]:
            query= """ SELECT championName, ROUND(goldEarned / gameDuration,2) AS golds_per_minute
                    FROM participant
                    GROUP BY championName 
                    ORDER BY golds_per_minute DESC
                """
            cursor.execute(query)       
            results = cursor.fetchall()   # Récupérer les résultats de la requête
            statgold: list[str] = []  # Pour stocker les statistiques
            # Pour chaque résultat, créer une chaîne de statistiques et l'ajouter à la liste
            for result in results:
                    champion_name, golds_per_minute= result
                    stat_str = f"Champion: {champion_name}, Golds_per_minute: {golds_per_minute}"
                    statgold.append(stat_str)

            return statgold  # Retourner la liste des statistiques
        
        #Liste des lane suivant l'ordre décroissant du winrate par lane
        elif critere==self.critere_affichage[4]:
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
        
        #Liste des champions et leur gold, totalminionkilled et l'ordre décroissant de leur total_games joués
        elif critere==self.critere_affichage[5]:
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
particip_dao = participantDAO(critere_affichage="Per_lane")
result = particip_dao.find_best_champ("Per_lane")
print(result)