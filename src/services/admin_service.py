import pandas as pd

class AdminService():
    
    def add_games_from_players():
        # Connect to the SQLite database
        conn = sqlite3.connect('data/database.db')

        # Read the table into a dataframe
        df_joueur = pd.read_sql('SELECT * FROM joueur', conn)
        df_participant = pd.read_sql('SELECT mathId FROM participant', conn).unique()

        df_joueur_aplatie = df_joueur.explode('matches')['matches'].unique()


        # Création des dataframes exemple
        data1 = {'colonne': [1, 2, 3, 4, 5]}
        data2 = {'colonne': [3, 4, 5, 6, 7]}

        df1 = pd.DataFrame(data1)
        df2 = pd.DataFrame(data2)

        # Trouver les lignes qui sont dans df1 mais pas dans df2
        merged = df_joueur.merge(df_, on='colonne', how='outer', indicator=True)
        result = merged[merged['_merge'] == 'left_only']

        # Suppression de la colonne _merge
        result = result.drop(columns=['_merge'])

        print(result)



