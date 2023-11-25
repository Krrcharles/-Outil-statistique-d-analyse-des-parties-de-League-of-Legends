"""
Module docstring: This module provides database access functions for managing participant data.
"""

import sqlite3
from typing import List
from src.utils.singleton import Singleton
from src.dao.playerDAO import PlayerDAO
from src.business.participant.participant import Participant

class ParticipantDAO(metaclass=Singleton):
    """
    DAO class for interacting with the participant table in the database.
    Utilizes the Singleton design pattern.
    """

    def __init__(self, db_file='data/database.db'):
        """
        Initialize the class with the name of the SQLite database file.

        Parameters:
        db_file (str): Name of the SQLite database file.
        """
        self.db_file = db_file

    def find_best_champ(self, criteria) -> List[str]:
        """
        Get all champions by a specified criteria and return a list.

        :param criteria: Criteria for selecting champions.
        :type criteria: str
        :return: A list of statistics for champions.
        :rtype: List of str
        """
        criteria_display = ["Per_game", "Per_winrate", "Per_KDA", "Per_gold", "Per_lane", "Per_other_stat"]
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        if criteria == criteria_display[0]:
            # List of champions ranked by popularity (total number of games played)
            query = """
                SELECT championName as Champion, COUNT(*) AS total_parties       
                FROM participant                  
                GROUP BY championName              
                ORDER BY total_parties DESC   
            """
            cursor.execute(query)
            results = cursor.fetchall()
            return results

        if criteria == criteria_display[1]:
            # List of champions ranked by winrate
            query = """
                SELECT championName, COUNT(*) AS total_parties, 
                SUM(win) AS parties_gagnees, ROUND((SUM(win) * 1.0 / COUNT(*)),2)*100 AS winrate
                FROM participant                                 
                GROUP BY championName                             
                ORDER BY winrate DESC                           
            """
            cursor.execute(query)
            results = cursor.fetchall()
            return results

        if criteria == criteria_display[2]:
            # Champions list in descending order of KDA
            query = """
                SELECT championName, ROUND(AVG((kills + assists) / deaths), 2) AS kda
                FROM participant 
                GROUP BY championName 
                ORDER BY kda DESC  
            """
            cursor.execute(query)
            results = cursor.fetchall()
            return results

        if criteria == criteria_display[3]:
            # List of champions in descending order of gold per minute per game
            query = """
                SELECT championName, ROUND(AVG(goldEarned / gameDuration),2) AS golds_per_minute
                FROM participant
                GROUP BY championName 
                ORDER BY golds_per_minute DESC
            """
            cursor.execute(query)
            results = cursor.fetchall()
            return results

        if criteria == criteria_display[4]:
            # List of lanes in descending order of total games played per lane
            query = """
                SELECT lane, COUNT(*) AS total_parties, ROUND((SUM(win) * 1.0 / COUNT(*)),2)*100 AS winrate
                FROM participant                                    
                GROUP BY lane                                       
                ORDER BY total_parties DESC                        
            """
            cursor.execute(query)
            results = cursor.fetchall()
            return results

        if criteria == criteria_display[5]:
            # Champions list and their gold, totalminionkilled and descending order of total_games played
            query = """
                SELECT championName, COUNT(*) AS total_parties, SUM(goldEarned) AS total_gold, SUM(totalMinionsKilled) AS total_minions_killed
                FROM participant                                    
                GROUP BY championName                               
                ORDER BY total_parties DESC                      
            """
            cursor.execute(query)
            results = cursor.fetchall()
            return results

    def stat_champ_by_name(self, name: str):
        """
        Retrieves the statistics of a champion given their name.

        :param name: Name of the champion.
        :type name: str
        :return: Champion's statistics including total games played, winrate, kda, and golds per minute.
        """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        query = """
            SELECT 
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

    def getpartie(self, name_player):
        """
        Displays all the games played by a player with statistics for each game.

        :param name_player: Name of the player.
        :type name_player: str
        :return: A list of Participant instances representing the games played.
        """
        player = PlayerDAO().find_player_by_name(name_player)
        if player is None:
            return None
        puuid = player._puuid

        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        query = """
            SELECT *
            FROM participant
            WHERE puuid = ?
            LIMIT 10;
        """

        cursor.execute(query, (puuid,))
        res = cursor.fetchall()
        parties = []

        for participant in res:
            participant_instance = Participant(
                id_game=participant[1],
                puuid=participant[0],
                teamID=participant[3],
                totalDamageDealtToChampions=participant[4],
                win=participant[5],
                lane=participant[7],
                role=participant[8],
                totalMinionsKilled=participant[6],
                championName=participant[9],
                goldEarned=participant[10],
                death=participant[11],
                assists=participant[12],
                kills=participant[13],
                gameDuration=participant[2])
            parties.append(participant_instance)
        return parties

    def add_participant(self, participant: Participant):
        """
        Adds a participant entry to the database.

        :param participant: The participant instance to add.
        :type participant: Participant
        """
        participant_list = [
            participant._puuid,
            participant._id_game,
            participant._gameDuration,
            participant._teamID,
            participant._totalDamageDealtToChampions,
            participant._win,
            participant._totalMinionsKilled,
            participant._lane,
            participant._role,
            participant._championName,
            participant._goldEarned,
            participant._death,
            participant._assists,
            participant._kills
        ]

        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO participant VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', participant_list)
        conn.commit()
        conn.close()
