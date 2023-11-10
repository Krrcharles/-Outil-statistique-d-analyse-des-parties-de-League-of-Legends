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

    def __str__(self):
        """
        Affichage d'un joueur
        """
        return f"Player: {self._name}, ID: {self._id}, Rank: {self._rank}, PUUID : {self._puuid}, \n win : {self._win}, loses : {self._losses}, level : {self._level}"
