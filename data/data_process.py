import sqlite3
import pandas as pd

# Connexion à la première base de données
conn = sqlite3.connect('data/database.db')
# Lire la table depuis cette base de données et l'afficher
df = pd.read_sql_query("SELECT * from participant", conn)

# Fermer la connexion à la première base de données
conn.close()


grouped = df.sort_values('teamId').groupby('matchId')
print(grouped)