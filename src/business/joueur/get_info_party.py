import sqlite3
import pandas as pd
import json


with open('src/business/joueur/infos_partie.json', 'r') as fichier_json:
    infos_partie = json.load(fichier_json)
    
info = infos_partie.get("info")

# Accéder aux informations spécifiques pour chaque participant
participants = info.get("participants", [])

# Créer un dictionnaire pour stocker les informations par puuid
participant_info = {}

for participant in participants:
    puuid = participant["puuid"]
    # Créer une liste avec les informations spécifiques pour ce participant
    participant_data = [
        info["gameDuration"],
        participant["assists"],
        participant["championId"],
        participant["champLevel"],
        participant["deaths"],
        participant["goldEarned"],
        participant["kills"],
        participant["neutralMinionsKilled"],
        participant["role"],
        participant["lane"],
        participant["summoner1Id"],
        participant["summoner2Id"],
        participant["totalDamageDealt"],
        participant["win"],
        participant["teamId"]
    ]
    
    # Assigner la liste d'informations au puuid dans le dictionnaire
    participant_info[puuid] = participant_data

print(participant_info)