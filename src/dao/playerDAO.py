<<<<<<< HEAD
from src.business.player.player import Player
from src.dao.db_connection import AbstractDAO

class PlayerDAO():
    """
    """
    def find_player(self, name: str) -> Player:
        with AbstractDAO().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *                                                        "
                    "  FROM              "
                    " WHERE                                         ",
                    {"name": name},
                )
                res = cursor.fetchone()

            pokemon = None
            pkmn_factory = PokemonFactory()

        if res:
            attacks = AttackDao().find_all_attacks_by_id_pokemon(res["id_pokemon"])

            pokemon = pkmn_factory.instantiate_pokemon(
                type=res["pokemon_type_name"],
                id=res["id_pokemon"],
                hp=res["hp"],
                attack=res["attack"],
                defense=res["defense"],
                sp_atk=res["spe_atk"],
                sp_def=res["spe_def"],
                speed=res["speed"],
                level=res["level"],
                name=res["name"],
                common_attacks=attacks,
            )

        return pokemon
=======
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

>>>>>>> 8c26e7cb55eaadfe97d78e6778e37d9b89e4495d
