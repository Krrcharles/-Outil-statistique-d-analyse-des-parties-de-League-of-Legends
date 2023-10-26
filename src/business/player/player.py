import sqlite3, requests, json, time
import pandas as pd


class Player :



    ####################################
    #           Constructor            #
    ####################################

    def __init__(
        self,
        name : str,
        id : str,
        puuid : str,
        rank : str, 
        win : int,
        losses : int,
        level : int
    )-> None :


    ####################################
    #           Attributes             #
    ####################################


        self._name = name
        self._id = id
        self._puuid  = puuid
        self._rank = rank
        self._win = win
        self._losses = losses
        self._level = level

    ####################################
    #             Methods              #
    ####################################