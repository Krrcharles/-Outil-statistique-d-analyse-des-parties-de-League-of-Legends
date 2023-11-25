class Participant:

    ####################################
    #           Constructor            #
    ####################################

    def __init__(
        self,
        id_game: str,
        puuid: str,
        teamID: int,
        totalDamageDealtToChampions: int,
        win: bool,
        lane: str,
        role: str,
        totalMinionsKilled: int,
        championName: str,
        goldEarned: int,
        death: int,
        assists: int,
        kills: int,
        gameDuration: int
    ) -> None:

        ####################################
        #           Attributes             #
        ####################################

        self._id_game = id_game
        self._puuid = puuid
        self._teamID = teamID
        self._totalDamageDealtToChampions = totalDamageDealtToChampions
        self._win = win
        self._lane = lane
        self._role = role
        self._totalMinionsKilled = totalMinionsKilled
        self._championName = championName
        self._goldEarned = goldEarned
        self._death = death
        self._assists = assists
        self._kills = kills
        self._gameDuration = gameDuration

    ####################################
    #             Methods              #
    ####################################
    def __str__(self):
        return (
            f"ID: {self._id_game}, "
            f"PUUID: {self._puuid}, "
            f"Team ID: {self._team_id}, "
            f"Win: {self._win}, "
            f"Total Damage Dealt to Champions: {self._total_damage_dealt_to_champions}, "
            f"Lane: {self._lane}, "
            f"Role: {self._role}, "
            f"Total Minions Killed: {self._total_minions_killed}, "
            f"Champion Name: {self._champion_name}, "
            f"Gold Earned: {self._gold_earned}, "
            f"Death: {self._death}, "
            f"Assists: {self._assists}, "
            f"Kills: {self._kills}, "
            f"Game Duration: {self._game_duration}"
        )
