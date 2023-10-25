import sqlite3, requests, json, time
import pandas as pd

api_key = input('API Key : ')

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
    matches_url = 'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/' + puuid_joueur +'/ids?type=ranked&start=0&count=20&api_key=' + api_key
    matches_id = requests.get(matches_url).json()
    matches.append(matches_id)
    time.sleep(1.2)
    
joueurs['matches'] = matches

# Connect to a database (or create one)
conn = sqlite3.connect('data/database.db')
joueurs['matches'] = joueurs['matches'].apply(json.dumps)
joueurs.to_sql('joueur', conn, if_exists='replace', index=False)
conn.close()