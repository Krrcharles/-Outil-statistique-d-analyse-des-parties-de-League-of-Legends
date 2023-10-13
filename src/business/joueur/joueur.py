import sqlite3, requests, json, time
import pandas as pd


class Joueur():

    def __init__(
        self,
        nom : str,
        id : str,
        puuid : str,
        rank : str, 
        winrate : float,
        KDA : float,
        Ga15 : float,
        champions_joue : list(str),
        last_games : list(str)
    )-> None :

    ####################################
    #           Attributes             #
    ####################################


    self._nom : str = nom,
    self._id : str = id,
    self._puuid : str = puuid,
    self._rank : str = rank, 
    self._winrate : float = winrate,
    self._KDA : float = KDA,
    self._Ga15 : float = Ga15,
    self._champions_joue : list(str) = champions_joue,
    self._last_games : list(str) = last_games