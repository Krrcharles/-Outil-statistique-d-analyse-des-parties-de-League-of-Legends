import psycopg2
import sqlite3

class championDAO:
    
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    # Afficher la liste des champions suivant le nombre de games joués
    def get_conn_by_games_played(self):
        request='SELECT * '
                ' FROM conn '
                ' ORDER BY {}'.format(wins+losses)

    # Etape 1 : On récupère une connexion en utilisant la classe DBConnection.
    with DBConnection().connection as connection :

    # Etape 2 : à partir de la connexion on fait un curseur pour la requête 
        with connection.cursor() as cursor : 
        
        # Etape 3 : on exécute notre requête SQL.
                cursor.execute(request)
        
        # Etape 4 : on stocke le résultat de la requête
                res = cursor.fetchall()

        # Étape 2 : Exécuter une requête SQL pour ajouter la nouvelle colonne
        #games_played = 'sum_column'
        #self.cursor.execute('ALTER TABLE db_file ADD COLUMN {} INTEGER'.format(games_played))
        #self.conn.commit()

    # Étape 3 : Mettre à jour les enregistrements existants avec la somme des deux autres colonnes
    #def update_conn_with_sum_column(self):
     #   self.cursor.execute('UPDATE conn SET {} = wins + losses'.format(games_played))
      #  self.conn.commit()

  
