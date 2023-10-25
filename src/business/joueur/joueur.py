import sqlite3, requests, json, time
import pandas as pd


class Joueur :



    ####################################
    #           Constructor            #
    ####################################

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


    self._nom = nom,
    self._id = id,
    self._puuid  = puuid,
    self._rank = rank, 
    self._winrate = winrate,
    self._KDA = KDA,
    self._Ga15 = Ga15,
    self._champions_joue = champions_joue,
    self._last_games = last_games

    ####################################
    #             Methods              #
    ####################################