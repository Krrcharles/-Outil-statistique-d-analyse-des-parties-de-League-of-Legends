import unittest
from src.dao.userDAO import UserDAO
from unittest.mock import patch

class TestUserDAO() : 
    

    def setUp(self):
        # Common setup code for both test methods
        self.dao = UserDAO("test_db.sqlite")  # Assuming you have a constructor that takes the database name
        self.new_login = "new_user"
        self.new_password = "password123"
        self.login = "bamara"
        self.non_existant_login = "utilisateur_test"
        self.expected_mdp = "E5B8F9D03C93E55E81C2DE945C13522EC3EAE0893B73A9BD5E8629063CFB2E46"

    def tearDown(self):
        # Common teardown code for both test methods
        pass

    @patch("your_module.sqlite3.connect")
    @patch("your_module.UserDAO.verifier_utilisateur")


    def test_verifier_utilisateur_userDAO (self, mock_connect) :
        # Given
        mock_cursor = mock_connect.return_value.cursor.return_value

        # When
        result_exists = self.dao.verifier_utilisateur(self.login)
        result_not_exists = self.dao.verifier_utilisateur(self.non_existant_login)

        # Then
        mock_cursor.execute.assert_any_call("SELECT * FROM utilisateur WHERE login = ?", (self.login,))
        mock_cursor.execute.assert_any_call("SELECT * FROM utilisateur WHERE login = ?", (self.non_existant_login,))

        # User exists, so the result should be True
        self.assertTrue(result_exists)

        # User does not exist, so the result should be False
        self.assertFalse(result_not_exists)


    def test_rajouter_utilisateur_userDAO (self, mock_verifier_utilisateur, mock_connect):
        # Test code for rajouter_utilisateur method
        # Given
        mock_verifier_utilisateur.return_value = False  # Assuming the user doesn't exist
        mock_cursor = mock_connect.return_value.cursor.return_value

        # When
        result = self.dao.rajouter_utilisateur(self.new_login, self.new_password)

        # Then
        mock_verifier_utilisateur.assert_called_once_with(self.new_login)
        if not result:
            mock_cursor.execute.assert_called_once_with(
                "INSERT INTO utilisateur (login, password, isadmin) VALUES (?,?,?)",
                (self.new_login, self.new_password, 0)
            )
            mock_connect.return_value.commit.assert_called_once()
            mock_cursor.close.assert_called_once()
            mock_connect.return_value.close.assert_called_once()

        self.assertEqual(result, not mock_verifier_utilisateur.return_value)



    def test_recuperer_mdp_userDAO(self, mock_connect) :

        # Given 
        mock_cursor = mock_connect.return_value.cursor.return_value

        # When

        result = self.dao.UserDAO.recuperer_mdp(self,login)

        # Then 
        
        mock_cursor.execute.assert_called_once_with("SELECT password, isadmin FROM utilisateur WHERE login = ?", (self.login,))
        mock_cursor.fetchone.assert_called_once()

        expected_result = (self.login, 0)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()