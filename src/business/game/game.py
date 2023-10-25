import sqlite3, requests, json, time
import pandas as pd


class Game :



    ####################################
    #           Constructor            #
    ####################################

    def __init__(
        self,
        id : str,
        login : str,
        password : str
    )-> None :


    ####################################
    #           Attributes             #
    ####################################


        self._id : str,
        self._login : str,
        self._password : str


    ####################################
    #             Methods              #
    ####################################


    def consulter_stat_player ()