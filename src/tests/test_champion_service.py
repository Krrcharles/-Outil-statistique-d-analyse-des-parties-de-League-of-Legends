import unittest
from unittest.mock import patch
import sys
from io import StringIO
from src.services.champion_service import ChampionService


class TestChampionService(unittest.TestCase):

    def test_classement_champion_invalid_critere(self):
        champion_service = ChampionService()
        result = champion_service.classement_champion(123)
        self.assertEqual(result, "Le critère n'est pas une chaine de caractère")

    @patch('src.dao.participantDAO.ParticipantDAO.find_best_champ')
    def test_classement_champion_Per_game(self, mock_find_best_champ):
        mock_find_best_champ.return_value = [('Champion1', 100), ('Champion2', 90), ('Champion3', 80)]
        champion_service = ChampionService()
        result = champion_service.classement_champion("Per_game")
        expected_output = (
            "+------------------------------------------------------+\n"
            "| Voici le classement des champions par parties jouées |\n"
            "+------------------------------------------------------+\n"
            "|            Champion1 : 100 parties jouées            |\n"
            "|            Champion2 : 90 parties jouées             |\n"
            "|            Champion3 : 80 parties jouées             |\n"
            "+------------------------------------------------------+"
        )
        self.assertEqual(result, expected_output)

    @patch('src.dao.participantDAO.ParticipantDAO.find_best_champ')
    def test_classement_champion_Per_winrate(self, mock_find_best_champ):
        mock_find_best_champ.return_value = [('Champion1', 0, 0, 93.5), ('Champion2', 0, 0, 73), ('Champion3', 0, 0, 12)]
        champion_service = ChampionService()
        result = champion_service.classement_champion("Per_winrate")
        expected_output = (
            "+-----------------------------------------------+\n"
            "| Voici le classement des champions par winrate |\n"
            "+-----------------------------------------------+\n"
            "|     Champion1 : 93.5% de parties gagnées      |\n"
            "|      Champion2 : 73% de parties gagnées       |\n"
            "|      Champion3 : 12% de parties gagnées       |\n"
            "+-----------------------------------------------+"
        )
        self.assertEqual(result, expected_output)

    @patch('src.dao.participantDAO.ParticipantDAO.find_best_champ')
    def test_classement_champion_Per_KDA(self, mock_find_best_champ):
        mock_find_best_champ.return_value = [('Champion1', 13), ('Champion2', 9), ('Champion3', 2.3)]
        champion_service = ChampionService()
        result = champion_service.classement_champion("Per_KDA")
        expected_output = (
            "+-------------------------------------------+\n"
            "| Voici le classement des champions par KDA |\n"
            "+-------------------------------------------+\n"
            "|           Champion1 : 13 de KDA           |\n"
            "|           Champion2 : 9 de KDA            |\n"
            "|          Champion3 : 2.3 de KDA           |\n"
            "+-------------------------------------------+"
        )
        self.assertEqual(result, expected_output)

    @patch('src.dao.participantDAO.ParticipantDAO.find_best_champ')
    def test_classement_champion_Per_gold(self, mock_find_best_champ):
        mock_find_best_champ.return_value = [('Champion1', 9.8), ('Champion2', 7), ('Champion3', 5.4)]
        champion_service = ChampionService()
        result = champion_service.classement_champion("Per_gold")
        expected_output = (
            "+---------------------------------------------------+\n"
            "| Voici le classement des champions par gold gagnés |\n"
            "+---------------------------------------------------+\n"
            "|         Champion1 : 9.8 golds par minute          |\n"
            "|          Champion2 : 7 golds par minute           |\n"
            "|         Champion3 : 5.4 golds par minute          |\n"
            "+---------------------------------------------------+"
        )
        self.assertEqual(result, expected_output)

    def test_stat_champion_invalid_champ(self):
        champion_service = ChampionService()
        with patch('builtins.print') as mock_print:
            result = champion_service.stat_champion(123)
            mock_print.assert_called_with("Le champion n'est pas une chaine de caractère")
        self.assertFalse(result)

    @patch('src.dao.participantDAO.ParticipantDAO.stat_champ_by_name')
    def test_stat_champion_valid_champ(self, mock_stat_champ_by_name):
        mock_stat_champ_by_name.return_value = ('Champion1', 'Role1', 60.0, 4.0, 200)
        champion_service = ChampionService()
        with patch('builtins.print') as mock_print:
            result = champion_service.stat_champion("Champion1")
            mock_print.assert_called_with(
                "+-----------------------------------------------+\n"
                "| Champion1 60.0% WIN - 4.0 KDA - 200 Golds/min |\n"
                "+-----------------------------------------------+"
            )
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
