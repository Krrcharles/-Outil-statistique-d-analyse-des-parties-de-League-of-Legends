import psycopg2
from typing import Optional
from src.dao.db_connection import AbstractDAO
from src.utils.singleton import Singleton

class PlayerDAO(metaclass=Singleton):
    """
    Communicate with the player table
    """

    def Trouver_infos_player_by_id(self, id) -> Optional[list[str]]:
        """
        Retourne une liste des informations d'un joueur à partir de son id joueur

        :param id: L'identifiant du joueur à rechercher
        :type id: str
        :return: Une liste des informations du joueur
        :rtype: List of str or None
        """
        # Accédez à la propriété 'connection' sans l'appeler comme une méthode
        with AbstractDAO().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "FROM joueur "
                    "WHERE summonerID = %s",
                    (id,)
                )

                # Enregistrez la ligne obtenue
                res = cursor.fetchone()

        return res

