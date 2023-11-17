import unittest
import timeit
from unittest.mock import patch
from io import StringIO
from src.dao.participantDAO import ParticipantDAO

class TestParticipantDAO (unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.dao = ParticipantDAO(db_file=':memory:')
     

    def setUp(self):
        self.participant_dao = ParticipantDAO()  # Créer une instance de la DAO


if __name__ == '__main__':
    unittest.main()