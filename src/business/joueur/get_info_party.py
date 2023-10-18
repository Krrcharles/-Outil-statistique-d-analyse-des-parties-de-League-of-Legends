"""
InfoDto : gameDuration, EUW1_6627153849

ParticipantDto : assists, championId, championLevel, death , goldEarned, kills, neutralMinionsKilled, puuid, role and lane, summoner1id, summoner2id, totalDamageDealt, win, teamId
"""
import sqlite3
import pandas as pd

api_key = 'RGAPI-2c02a22e-1bdc-43fc-91a6-ecea79c4b0c8'

match_key = 'https://europe.api.riotgames.com/lol/match/v5/matches/EUW1_6627699808?api_key=RGAPI-a8b3f16b-23ed-455a-8fb5-e976ea8225d7'
print(match_key)


