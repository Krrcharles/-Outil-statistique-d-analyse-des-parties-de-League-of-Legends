from src.business.player.player import Player
import sqlite3

class PlayerDAO:

    def __init__(self, db_name='data/database.db'):

        """
        Initialize the class with the name of the SQLite database file.

        Parameters:
        db_name (str): Name of the SQLite database file.
        """
        self.db_name = db_name

    def find_player_by_name(self, name: str) -> Player:
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Using a parameterized query to avoid SQL injection
        # precise the name of the columns in the case that the order change so ze can still use the integer from line 35 to 41
        query = """SELECT summonerName AS name, summonerId AS id, puuid, rank, wins, losses, level 
                    FROM joueur 
                    WHERE summonerName = ?
                    """
      
        cursor.execute(query, (name,))
        
        res = cursor.fetchone()

        player = None

        if res:
            # Create a Player object with the fetched data
            player = Player(
                name=res[0],  # Assuming 'summonerName' is the first column
                id=res[1],    # Assuming 'summonerId' is the second column
                puuid=res[2], # Assuming 'puuid' is the third column
                rank=res[3],  # Assuming 'rank' is the fourth column
                win=res[4],   # Assuming 'wins' is the fifth column
                losses=res[5],  # Assuming 'losses' is the sixth column
                level=res[6]  # Assuming 'level' is the seventh column
            )

        return player

# Example usage:
"""player_name = "TwTv Raideru"
player_dao = PlayerDAO()
result = player_dao.find_player_by_name(player_name)
print(result)"""
