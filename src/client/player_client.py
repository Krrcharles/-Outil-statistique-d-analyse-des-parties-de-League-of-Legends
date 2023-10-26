import os
import requests

from typing import List, Optional


class PlayerClient(metaclass=Singleton):
    def __init__(self) -> None:
        # Utilisation d'une variable d'environnement définie dans le fichier .env
        self.__HOST = os.environ["HOST_WEBSERVICE"]

    def afficher_parties():
        pass

    def afficher_stats_player():