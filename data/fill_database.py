import sqlite3, requests, json, time
import pandas as pd
#RGAPI-0282fe35-e799-4f1a-b81f-713b8c4b7d7b
api_key = input('API Key : ')

#####JOUEUR#####
challengers_url = 'https://euw1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5'
final_challengers_url = challengers_url + '?api_key=' + api_key

challengers_data = requests.get(final_challengers_url)
time.sleep(1.2)

joueurs = pd.DataFrame(challengers_data.json()['entries'])[:5]

puuid = []
level = []
for id_joueur in joueurs['summonerId']:
    summoner_url = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/' + id_joueur + '?api_key=' + api_key
    summoner_data = requests.get(summoner_url).json()
    puuid.append(summoner_data['puuid'])
    level.append(summoner_data['summonerLevel'])
    time.sleep(1.2)
    print("ca avance 1")

joueurs['puuid'] = puuid
joueurs['level'] = level

matches = []
for puuid_joueur in joueurs['puuid']:
    matches_url = 'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/' + puuid_joueur +'/ids?type=ranked&start=0&count=20&api_key=' + api_key
    matches_id = requests.get(matches_url).json()
    matches.append(matches_id)
    time.sleep(1.2)
    
joueurs['matches'] = matches

#####PARTICIPANT#####

# Connect to a database (or create one)
conn = sqlite3.connect('data/database_test.db')
joueurs['matches'] = joueurs['matches'].apply(json.dumps)
joueurs.to_sql('joueur', conn, if_exists='replace', index=False)
conn.close()

# Connect to the SQLite database
conn = sqlite3.connect('../data/database.db')

# Read the table into a dataframe
df = pd.read_sql('SELECT * FROM joueur', conn)

# Convert the 'Scores' column back to a list
df['matches'] = df['matches'].apply(json.loads)

# Close the connection
conn.close()

# Extraire les deux premiers éléments de chaque liste
df['matches'] = df['matches'].apply(lambda x: x[:2])

# Aplatir la colonne
liste_aplatie = df.explode('matches')['matches'].unique().tolist()


