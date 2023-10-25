import sqlite3, requests, json, time
import pandas as pd

class User ():


    ####################################
    #           Constructor            #
    ####################################

    
    def __init__(
        self,
        id : str ,
        login : int ,
        password : float ,
        is_admin : bool
    ) -> None : 


    ####################################
    #           Attributes             #
    ####################################

        self._id = id,
        self._login = login,
        self._password = password,
        self._is_admin = is_admin

    ####################################
    #             Methods              #
    ####################################