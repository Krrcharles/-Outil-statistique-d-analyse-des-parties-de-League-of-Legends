import sqlite3

class ChampionDAO:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

        # Étape 2 : Exécuter une requête SQL pour ajouter la nouvelle colonne
        games_played = 'sum_column'
        self.cursor.execute('ALTER TABLE db_file ADD COLUMN {} INTEGER'.format(games_played))
        self.conn.commit()

    # Étape 3 : Mettre à jour les enregistrements existants avec la somme des deux autres colonnes
    def update_conn_with_sum_column(self):
        self.cursor.execute('UPDATE conn SET {} = wins + losses'.format(games_played))
        self.conn.commit()

    # Afficher la liste des champions suivant le nombre de games joués
    def get_conn_by_games_played(self):
        self.cursor.execute('SELECT * FROM conn ORDER BY {}'.format(games_played))
        return self.cursor.fetchall()


# Exemple d'utilisation
if __name__ == '__main':
    db_file = 'data/database.db'
    champion_dao = ChampionDAO(db_file)

    # Étape 2 : Ajouter la nouvelle colonne et mettre à jour les enregistrements existants
    champion_dao.update_conn_with_sum_column()

    # Étape 3 : Récupérer la liste des champions triés par la nouvelle colonne
    champions = champion_dao.get_conn_by_games_played()
    for champion in champions:
        print(champion)

    champion_dao.conn.close()

