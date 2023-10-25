import os
import requests

from typing import List, Optional
from utils.singleton import Singleton

END_POINT = "/attack"


class AdminClient(metaclass=Singleton):
    def __init__(self) -> None:
        

    def update_infos(self, attack: AbstractAttack) -> bool:
        """ Informations update à déterminer """

    def delete_infos(self, attack: AbstractAttack) -> bool:
        """ Informations delete à déterminer"""


if __name__ == "__main__":
    # Pour charger les variables d'environnement contenues dans le fichier .env
    import dotenv

    dotenv.load_dotenv(override=True)

    attack_client = AttackClient()

    attack_id = 1
    attack_client.get_attack(attack_id)
