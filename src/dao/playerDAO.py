from src.business.player.player import Player
from src.dao.db_connection import AbstractDAO


class PlayerDAO():
    """
    """
    def find_player(self, name: str) -> Player:
        with AbstractDAO().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM joueur WHERE summonerName = ?", (name,)
                )
                res = cursor.fetchone()

            player = None

        if res:
            player = Player(
                name = res["summonerName"],
                id = res["summonerId"],
                puuid = res["puuid"],
                rank = res["rank"],
                win = res["wins"],
                losses = res["losses"],
                level = res["level"]
                )

        return player