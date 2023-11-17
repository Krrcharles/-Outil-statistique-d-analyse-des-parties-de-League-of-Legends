import sqlite3
import requests
import json
import time
import hashlib
import pandas as pd
from data.components import extract_participant_info

def fill():
    api_key = input('API Key: ')

    # UTILISATEUR
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO utilisateur (id, login, password, isadmin) VALUES (?, ?, ?, ?)',
        (
            0, 'teemo',
            hashlib.pbkdf2_hmac('sha256', '1234'.encode('utf-8'), 'teemo'.encode('utf-8'), 100),
            0
        )
    )
    conn.commit()

    cursor.execute(
        'INSERT INTO utilisateur (id, login, password, isadmin) VALUES (?, ?, ?, ?)',
        (
            1, 'admin',
            hashlib.pbkdf2_hmac('sha256', 'admin'.encode('utf-8'), 'admin'.encode('utf-8'), 100),
            1
        )
    )
    conn.commit()

    # JOUEUR
    challengers_url = 'https://euw1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5'
    final_challengers_url = challengers_url + '?api_key=' + api_key

    challengers_data = requests.get(final_challengers_url)
    time.sleep(1.2)

    joueurs = pd.DataFrame(challengers_data.json()['entries'])

    puuid = []
    level = []
    for id_joueur in joueurs['summonerId']:
        summoner_url = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/' + id_joueur + '?api_key=' + api_key
        summoner_data = requests.get(summoner_url).json()
        puuid.append(summoner_data['puuid'])
        level.append(summoner_data['summonerLevel'])
        time.sleep(1.2)

    joueurs['puuid'] = puuid
    joueurs['level'] = level

    matches = []
    for puuid_joueur in joueurs['puuid']:
        matches_url = 'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/' + puuid_joueur + '/ids?type=ranked&start=0&count=20&api_key=' + api_key
        matches_id = requests.get(matches_url).json()
        matches.append(matches_id)
        time.sleep(1.2)

    joueurs['matches'] = matches

    # Connect to a database
    conn = sqlite3.connect('data/database.db')
    joueurs['matches'] = joueurs['matches'].apply(json.dumps)
    joueurs.to_sql('joueur', conn, if_exists='replace', index=False)
    conn.close()

    # PARTICIPANT
    conn = sqlite3.connect('data/database.db')
    df = pd.read_sql('SELECT * FROM joueur', conn)
    df['matches'] = df['matches'].apply(json.loads)
    conn.close()

    df['matches'] = df['matches'].apply(lambda x: x[:10])
    liste_aplatie = df.explode('matches')['matches'].unique().tolist()

    for matchId in liste_aplatie:
        print(matchId)
        match_url = "https://europe.api.riotgames.com/lol/match/v5/matches/" + matchId + '?api_key=' + api_key
        match_data = requests.get(match_url).json()
        time.sleep(1.2)
        participants = extract_participant_info(match_data)

        conn = sqlite3.connect('data/database.db')
        cursor = conn.cursor()
        for participant in participants:
            cursor.execute('INSERT INTO participant VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', participant)
            conn.commit()
        conn.close()
