import sqlite3, requests, json, time
import pandas as pd

class User ():


    ####################################
    #           Constructor            #
    ####################################

    
    def __init__(
        self,
        nom : str ,
        nbr_games : int ,
        winrate : float ,
        Ga15 : float
    ) -> None : 


    ####################################
    #           Attributes             #
    ####################################

    self._nom = nom,
    self._nbr_games  = nbr_games,
    self._winrate = winrate,
    self._Ga15 = Ga15,    