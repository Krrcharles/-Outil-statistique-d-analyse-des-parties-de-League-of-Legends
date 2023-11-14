import unittest
from unittest.mock import patch
import sys
from io import StringIO
from src.services.champion_service import ChampionService


class TestChampionService(unittest.TestCase):

    def test_classement_champion(self):
        expected_output = """+------------------------------------------------------+
        | Voici le classement des champions par parties jouées |
        +------------------------------------------------------+
        |              Kaisa : 451 parties jouées              |
        |              Rakan : 371 parties jouées              |
        |             Orianna : 359 parties jouées             |
        |             Graves : 355 parties jouées              |
        |             Ezreal : 341 parties jouées              |
        |              Rell : 331 parties jouées               |
        |            Nautilus : 325 parties jouées             |
        |             Syndra : 282 parties jouées              |
        |             Taliyah : 270 parties jouées             |
        |              Jayce : 267 parties jouées              |
        +------------------------------------------------------+"""

        original_stdout = sys.stdout
        ChampionService().classement_champion("Per_game")
        output = StringIO().getvalue()
        sys.stdout = original_stdout

        self.maxDiff = None
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
