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