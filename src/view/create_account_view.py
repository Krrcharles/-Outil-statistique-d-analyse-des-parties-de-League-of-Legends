from InquirerPy import prompt
from view.abstract_view import AbstractView
from view.session import Session

import sqlite3
import pandas as pd

class CreateAccountView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "identifiant",
                "message": "What's your login",
            },
            {
                "type": "input",
                "name": "password",
                "message": "What's your password",
            }
        ]

    def display_info(self):
        print("Hello, please enter your new login and password")

    def make_choice(self):
        answers = prompt(self.__questions)
        user_identifiant = answers["identifiant"]
        Session().user_identifiant = user_identifiant

        # Connexion à la base de données
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Exécutez une requête pour vérifier si le user_identifiant existe dans la table joueur
        query = "SELECT COUNT(*) FROM joueur WHERE summonerName = ?"
        cursor.execute(query, (user_identifiant,))
        result = cursor.fetchone()[0]  # Récupérez la valeur de COUNT(*)

        if result == 0:
            print(f"Le summonerName {user_identifiant} n'existe pas dans la base de données.")
            # Ajoutez ici le code pour gérer le cas où le summonerName n'existe pas

            return CreateAccountView()

        # Fermez la connexion à la base de données
        conn.close()

        Session().user_mdp = answers["password"]

        # methode en suspens

        choice = prompt(
            [
                {
                    "type": "confirm",
                    "name": "connect",
                    "message": "Do you want to connect ?",
                    "default": True,
                }
            ]
        )

        if choice["connect"]:
            from view.member_view import MemberView

            return MemberView()

        else:
            from view.invite_view import InviteView

            return InviteView()