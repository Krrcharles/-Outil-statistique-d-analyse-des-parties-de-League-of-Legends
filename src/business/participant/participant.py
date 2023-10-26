import sqlite3, requests, json, time
import pandas as pd


class Participant :



    ####################################
    #           Constructor            #
    ####################################

    def __init__(
        self,
        id_game : str,
        puuid : str,
        teamID : int,
        totalDamageDealtToChampions : int,
        win : bool,
        lane : str,
        role : str,
        totalMinionsKilled : int,
        championName : str,
        goldEarned : int,
        death : int,
        assists : int,
        kills : int,
        gameDuration : int
    )-> None :


    ####################################
    #           Attributes             #
    ####################################

        self._id_game = id_game,
        self._puuid = puuid,
        self._teamID = teamID,
        self._totalDamageDealtToChampions = totalDamageDealtToChampions,
        self._win = win,
        self._lane = lane,
        self._role = role,
        self._totaleMinionsKilled = totalMinionsKilled,
        self._championName = championName,
        self._goldEarned = goldEarned,
        self._death = death,
        self._assists = assists,
        self._kills = kills,
        self._gameDuration = gameDuration
        

    ####################################
    #             Methods              #
    ####################################


