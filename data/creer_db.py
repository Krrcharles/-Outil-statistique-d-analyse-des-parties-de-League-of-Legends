import sqlite3

# Connexion à la base de données SQLite (cela créera un fichier 'databse.db' s'il n'existe pas)
conn = sqlite3.connect('data/database_test.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS participant (
    puuid TEXT,
    matchId TEXT,
    gameDuration INTEGER,
    teamId INTEGER,
    totalDamageDone INTEGER,
    win BOOL,
    totalMinionsKilled INTEGER,
    lane TEXT,
    role TEXT,
    championName TEXT,
    goldEarned INTEGER,
    deaths INTEGER,
    assists INTEGER,
    kills INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS joueur (
    summonerId TEXT,
    summonerName TEXT,
    leaguePoints INTEGER,
    rank TEXT,
    wins INTEGER,
    losses INTEGER,
    veteran INTEGER,
    inactive INTEGER,
    freshBlood INTEGER,
    hotStreak INTEGER,
    puuid TEXT,
    level INTEGER,
    matches TEXT
)
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS utilisateur (
        id INTEGER SERIAL PRIMARY KEY,
        login TEXT,
        password INTEGER,
        isadmin INTEGER
    )
''')

conn.commit()
conn.close()