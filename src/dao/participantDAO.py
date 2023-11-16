import sqlite3
from typing import List
from src.utils.singleton import Singleton
from tabulate import tabulate
import pandas as pd
import os

class ParticipantDAO(metaclass=Singleton):
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


    def find_best_champ(self, critere) -> List[str]:
        """
        Get all champions by winrate return a list
        
        :return: A list of winrate for champions
        :rtype: List of str
        """
        critere_affichage=["Per_game", "Per_winrate", "Per_KDA",  "Per_gold", "Per_lane", "Per_other_stat"]
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        if critere==critere_affichage[0]:   
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
        elif critere==critere_affichage[1]:
            query=  """SELECT championName, COUNT(*) AS total_parties, SUM(win) AS parties_gagnees, ROUND((SUM(win) * 1.0 / COUNT(*)),2)*100 AS winrate
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
        elif critere==critere_affichage[2]:
            query= """SELECT championName , ROUND(AVG((kills + assists) / deaths), 2) AS kda
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
        
        #Liste des champions suivant l'ordre décroissant de leur gold par minute par partie 
        elif critere==critere_affichage[3]:
            query= """ SELECT championName, ROUND(goldEarned / gameDuration,3) AS golds_per_minute
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
        elif critere==critere_affichage[4]:
            query= """ SELECT lane, COUNT(*) AS total_parties, ROUND((SUM(win) * 1.0 / COUNT(*)),2)*100 AS winrate
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
        elif critere==critere_affichage[5]:
            query=  """ SELECT championName, COUNT(*) AS total_parties, SUM(goldEarned) AS total_gold, SUM(totalMinionsKilled) AS total_minions_killed
                        FROM participant                                    
                        GROUP BY championName                               
                        ORDER BY total_parties DESC                      
                    """
            cursor.execute(query)       
            results = cursor.fetchall()   # Récupérer les résultats de la requête
            
            #statother: list[str] = []  # Pour stocker les statistiques
            # Pour chaque résultat, créer une chaîne de statistiques et l'ajouter à la liste
            """
            for result in results:
                
                    champion_name, total_parties, total_gold, total_minions_killed = result
                    stat_str = f"Champion: {champion_name}, Total Parties: {total_parties}, Total Golds: {total_gold}, Total minions killed: {total_minions_killed}"
                    statother.append(stat_str)
                
            return statother  # Retourner la liste des statistiques
            """
            df=pd.DataFrame(columns=["Champion", "Total_games", "Total_gold", "Total_minions_killed"])
            for res in results:
                data = [
                    res[0],
                    res[1],
                    res[2],
                    res[3]
                ]
                df=df.append(pd.Series(data, index=df.columns), ignore_index=True)
                #statother=df.transpose()


            print(tabulate(df, headers="keys", tablefmt="pretty"))

    

    def stat_champ_by_name(self, name:str):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        query = """SELECT 
                        championName AS name,
                        COUNT(*) AS total_games,
                        ROUND((SUM(win) * 1.0 / COUNT(*)),3)*100 AS winrate,
                        ROUND((kills + assists) / deaths,2) AS kda,
                        ROUND(goldEarned / gameDuration,2) AS golds_per_minute
                    FROM participant
                    WHERE championName = ?
                    """
      
        cursor.execute(query, (name,))
        
        res = cursor.fetchone()

        if res:
            data = [
                [res[0]],
                [res[1]],
                [res[2]],
                [res[3]],
                [res[4]]
            ]
            df=pd.DataFrame(data)
            participant=df.transpose()


            print(tabulate(participant, headers=["Champion","Total_games","Winrate","KDA","Golds_per_minute"], tablefmt="pretty"))

        else:
            print("Champion not found.")

    def getpartie(self, player):
        """
        """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        query = """ SELECT championName, lane, win, kills, deaths, assists,
                            totalDamageDone, ROUND(goldEarned/gameDuration, 2) AS gold_min
                    FROM participant
                    JOIN joueur ON joueur.puuid = participant.puuid
                    WHERE joueur.summonerName = ?
                    ORDER BY participant.gameDuration DESC
                    LIMIT 10;"""

        cursor.execute(query, (player,))
        res = cursor.fetchone()

        return res

"""#Exemple d'utilisation
particip_dao = ParticipantDAO()
result = particip_dao.find_best_champ("Per_other_stat")
print(result)"""
"""
champion_name = "Sylas"
participant_dao = ParticipantDAO()
result = participant_dao.stat_champ_by_name(champion_name)
"""
particip_dao = ParticipantDAO()
result = particip_dao.getpartie("VIVE Serendrip")
print(result)
