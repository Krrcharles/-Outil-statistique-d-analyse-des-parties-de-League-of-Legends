import sqlite3
from typing import List
from src.utils.singleton import Singleton
from tabulate import tabulate
import pandas as pd
from src.dao.playerDAO import PlayerDAO

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

            df=pd.DataFrame(columns=["Champion", "Total Parties"])
            for res in results:
                data = [
                    res[0],
                    res[1]
                ]
                new_row = pd.Series(data, index=df.columns)
                df = pd.concat([df, new_row.to_frame().transpose()], ignore_index=True)

            print(tabulate(df, headers="keys", tablefmt="pretty"))
            

        #Liste des champions classés par winrate (nombre de parties gagnées/nombre de parties jouées)
        elif critere==critere_affichage[1]:
            query=  """SELECT championName, COUNT(*) AS total_parties, SUM(win) AS parties_gagnees, ROUND((SUM(win) * 1.0 / COUNT(*)),2)*100 AS winrate
                    FROM participant                                 
                    GROUP BY championName                             
                    ORDER BY winrate DESC                           
                    """
            cursor.execute(query)
            results = cursor.fetchall()   # Récupérer les résultats de la requête

            df=pd.DataFrame(columns=["Champion", "Total Parties", "Parties gagnées", "Winrate"])
            for res in results:
                data = [
                    res[0],
                    res[1],
                    res[2],
                    res[3]
                ]
                new_row = pd.Series(data, index=df.columns)
                df = pd.concat([df, new_row.to_frame().transpose()], ignore_index=True)

            print(tabulate(df, headers="keys", tablefmt="pretty"))
            
        #Liste des champions suivant l'ordre décroissant de leur KDA (kills+assists)/deaths sur toutes leurs parties jouées
        elif critere==critere_affichage[2]:
            query= """SELECT championName , ROUND(AVG((kills + assists) / deaths), 2) AS kda
                    FROM participant 
                    GROUP BY championName 
                    ORDER BY kda DESC  
                """
            cursor.execute(query)       
            results = cursor.fetchall()   # Récupérer les résultats de la requête

            df=pd.DataFrame(columns=["Champion", "KDA"])
            for res in results:
                data = [
                    res[0],
                    res[1]
                ]
                new_row = pd.Series(data, index=df.columns)
                df = pd.concat([df, new_row.to_frame().transpose()], ignore_index=True)

            print(tabulate(df, headers="keys", tablefmt="pretty"))

        #Liste des champions suivant l'ordre décroissant de leur gold par minute par partie 
        elif critere==critere_affichage[3]:
            query= """ SELECT championName, ROUND(AVG(goldEarned / gameDuration),2) AS golds_per_minute
                    FROM participant
                    GROUP BY championName 
                    ORDER BY golds_per_minute DESC
                """
            cursor.execute(query)       
            results = cursor.fetchall()   # Récupérer les résultats de la requête
            
            df=pd.DataFrame(columns=["Champion", "Gold per minutes"])
            for res in results:
                data = [
                    res[0],
                    res[1]
                ]
                new_row = pd.Series(data, index=df.columns)
                df = pd.concat([df, new_row.to_frame().transpose()], ignore_index=True)

            print(tabulate(df, headers="keys", tablefmt="pretty"))

        #Liste des lane suivant l'ordre décroissant du winrate par lane
        elif critere==critere_affichage[4]:
            query= """ SELECT lane, COUNT(*) AS total_parties, ROUND((SUM(win) * 1.0 / COUNT(*)),2)*100 AS winrate
                    FROM participant                                    
                    GROUP BY lane                                       
                    ORDER BY total_parties DESC                        
                    """
            cursor.execute(query)        
            results = cursor.fetchall()   # Récupérer les résultats de la requête

            df=pd.DataFrame(columns=["Lane", "Total Parties", "Winrate"])
            for res in results:
                data = [
                    res[0],
                    res[1],
                    res[2]
                ]
                new_row = pd.Series(data, index=df.columns)
                df = pd.concat([df, new_row.to_frame().transpose()], ignore_index=True)

            print(tabulate(df, headers="keys", tablefmt="pretty"))

        
        #Liste des champions et leur gold, totalminionkilled et l'ordre décroissant de leur total_games joués
        elif critere==critere_affichage[5]:
            query=  """ SELECT championName, COUNT(*) AS total_parties, SUM(goldEarned) AS total_gold, SUM(totalMinionsKilled) AS total_minions_killed
                        FROM participant                                    
                        GROUP BY championName                               
                        ORDER BY total_parties DESC                      
                    """
            cursor.execute(query)       
            results = cursor.fetchall()   # Récupérer les résultats de la requête

            df=pd.DataFrame(columns=["Champion", "Total_games", "Total_gold", "Total_minions_killed"])
            for res in results:
                data = [
                    res[0],
                    res[1],
                    res[2],
                    res[3]
                ]
                new_row = pd.Series(data, index=df.columns)
                df = pd.concat([df, new_row.to_frame().transpose()], ignore_index=True)

            print(tabulate(df, headers="keys", tablefmt="pretty"))

    

    def stat_champ_by_name(self, name:str):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        query = """SELECT 
                        championName AS name,
                        COUNT(*) AS total_games,
                        ROUND((SUM(win) * 1.0 / COUNT(*)), 3)*100 AS winrate,
                        ROUND(AVG((kills + assists) / deaths),2) AS kda,
                        ROUND(AVG(goldEarned / gameDuration),2) AS golds_per_minute
                    FROM participant
                    WHERE championName = ?
                    """
      
        cursor.execute(query, (name,))
        res = cursor.fetchone()

        return res

    def getpartie(self, player):
        """
        """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        puuid = PlayerDAO().find_player_by_name(player)._puuid
        print(puuid)
        query = """ SELECT championName, lane, win, kills, deaths, assists,
                            totalDamageDone, goldEarned/gameDuration
                    FROM participant
                    WHERE puuid = ?
                    LIMIT 10;
                    """

        cursor.execute(query, (puuid,))
        res = cursor.fetchall()

        return res

#Exemple d'utilisation
"""
particip_dao = ParticipantDAO()
result = particip_dao.find_best_champ("Per_gold")
print(result)
"""
"""
champion_name = "Sylo"
participant_dao = ParticipantDAO()
result = participant_dao.stat_champ_by_name(champion_name)
"""
"""
particip_dao = ParticipantDAO()
result = particip_dao.getpartie("VIVE Serendrip")
print(result)
"""
