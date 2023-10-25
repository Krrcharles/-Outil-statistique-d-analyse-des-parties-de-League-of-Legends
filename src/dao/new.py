import psycopg2

class ChampionDAO:
    def __init__(self, connection_string):
        self.conn = psycopg2.connect(connection_string)
        self.cursor = self.conn.cursor()

    # Récupérer les champions en fonction du nombre de parties jouées
    def get_champions_by_games_played(self, games_played_threshold):
        query = """
            SELECT * 
            FROM champions 
            WHERE wins + losses >= %s
            ORDER BY wins + losses DESC
        """
        with DBConnection().connection as connection :

	       with connection.cursor() as cursor : 
    		cursor.execute(query)
    		res = cursor.fetchall()

        #if res:
            # Etape 5 : on agence les résultats selon la forme souhaitée (liste...)
            
        #return something
                #self.cursor.execute(query, (games_played_threshold,))
                #return self.cursor.fetchall()