import unittest
from unittest.mock import patch
import sys
from io import StringIO
from src.dao.participantDAO import ParticipantDAO

class testParticipantDAO ():
    
    @classmethod
    def setUpClass(cls):
        # Initialisez la base de données avec des données de test si nécessaire
        # Cela pourrait être utilisé pour ajouter des données temporaires pour les tests
        # Par exemple, en utilisant un fichier de script SQL de test.
        cls.dao = ParticipantDAO(db_file=':memory:')
        #cls.dao.insert_temporary_champion("ChampionTest1", win=10, total_parties=20)
        #cls.dao.insert_temporary_champion("ChampionTest2", win=15, total_parties=25)

    def setUp(self):

        pass


    ###Tests pour find_best_champ: Appel à la méthode avec critère valide (Per_game, Per_lane,...)

    def test_find_best_champ_per_game(self):

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.dao.find_best_champ("Per_game")
        result = mock_stdout.getvalue().strip()

    
    def test_find_best_champ_per_winrate(self):

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.dao.find_best_champ("Per_winrate")
        result = mock_stdout.getvalue().strip()

    
    def test_find_best_champ_per_KDA(self):

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.dao.find_best_champ("Per_KDA")
        result = mock_stdout.getvalue().strip()

    
    def test_find_best_champ_per_gold(self):

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.dao.find_best_champ("Per_gold")
        result = mock_stdout.getvalue().strip()

    
    def test_find_best_champ_per_lane(self):

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.dao.find_best_champ("Per_lane")
        result = mock_stdout.getvalue().strip()
    

    def test_find_best_champ_per_other_stat(self):

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.dao.find_best_champ("Per_other_stat")
        result = mock_stdout.getvalue().strip()
  

    ###Test pour stat_champ_name: S'assurer que le champion entré existe vraiment ou que le nom du champion est valide
    def test_champion_exists(self):
        # Initialise une instance de ParticipantDAO avec une base de données en mémoire
        dao = ParticipantDAO(db_file=':memory:')

        # Ajoutez des données temporaires à la base de données pour le test
        # Ici, nous ajoutons un champion fictif appelé "TestChampion"
        dao.insert_temporary_champion("TestChampion")

        # On fait appel à la méthode stat_champ_by_name avec un champion existant
        with self.assertLogs() as logs:
            dao.stat_champ_by_name("TestChampion")

        # Vérifiez que le message de log "Champion not found." n'est pas présent
        self.assertNotIn("Champion not found.", logs.output)

    
    def test_champion_not_exists(self):
        # Initialise une instance de ParticipantDAO avec une base de données en mémoire
        dao = ParticipantDAO(db_file=':memory:')

        # On fait appel à la méthode stat_champ_by_name avec un champion inexistant
        result = dao.stat_champ_by_name("ChampionInexistant")

        # Vérifie que le résultat est vide
        self.assertIsNone(result, "Le champion inexistant ne devrait pas être trouvé")


if __name__ == '__main__':
    unittest.main()