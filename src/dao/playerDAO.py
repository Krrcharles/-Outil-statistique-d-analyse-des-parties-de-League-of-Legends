import sqlite3
import json
from src.business.player.player import Player

class PlayerDAO:
    """
    Data Access Object (DAO) class for handling player data in the database.
    Provides functionality to find and add player records.
    """

    def __init__(self, db_name='data/database.db'):
        """
        Initialize the class with the name of the SQLite database file.

        Parameters:
        db_name (str): Name of the SQLite database file.
        """
        self.db_name = db_name

    def find_player_by_name(self, name: str) -> Player:
        """
        Find a player by their name.

        Parameters:
        name (str): The name of the player to search for.

        Returns:
        Player: The found Player object, or None if not found.
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        query = """
            SELECT summonerName AS name, summonerId AS id, puuid, rank, wins, losses, level 
            FROM joueur 
            WHERE summonerName = ?
        """
      
        cursor.execute(query, (name,))
        res = cursor.fetchone()

        if res:
            # Create a Player object with the fetched data
            return Player(
                name=res[0],
                id=res[1],
                puuid=res[2],
                rank=res[3],
                win=res[4],
                losses=res[5],
                level=res[6]
            )

        return None

    def add_player(self, player: Player, matches_id: list):
        """
        Add a player to the database or update their record if they already exist.

        Parameters:
        player (Player): The Player object to be added or updated.
        matches_id (list): List of match IDs associated with the player.
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        if self.find_player_by_name(player._name):
            cursor.execute('DELETE FROM joueur WHERE summonerName = ?', (player._name,))

        cursor.execute(
            'INSERT INTO joueur (summonerId, summonerName, rank, wins, losses, puuid, level, matches) VALUES (?,?,?,?,?,?,?,?)',
            (player._id, player._name, player._rank, player._win, player._losses, player._puuid, player._level, json.dumps(matches_id))
        )
        conn.commit()
