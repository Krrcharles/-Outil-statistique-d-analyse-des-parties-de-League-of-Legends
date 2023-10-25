import sqlite3, requests, json, time
import pandas as pd


class Participant :



    ####################################
    #           Constructor            #
    ####################################

    def __init__(
        self,
        id_player : str,
        id_game : str,
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