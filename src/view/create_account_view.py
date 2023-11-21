from InquirerPy import prompt
from src.view.abstract_view import AbstractView
from src.view.session import Session
from src.services.connexion_services import Connexion_services
from src.view.connexion_view import ConnexionView

import sqlite3
import pandas as pd

class CreateAccountView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "identifiant",
                "message": "What is your login",
            },
            {
                "type": "input",
                "name": "password",
                "message": "What is your password",
            }
        ]

    def display_info(self):
        print("Hello, please enter your new login and password")

    def make_choice(self):
        answers = prompt(self.__questions)
        user_identifiant = answers["identifiant"]
        password = answers["password"]
        
        if password == "" or user_identifiant == "":
            print("Le pseudo et le mot de passe ne doivent pas être vide")

            from src.view.create_account_view import CreateAccountView

            return CreateAccountView()

        # Vérification que l'identifiant n'existe pas 

        instance = Connexion_services()
        resultat = instance.inscription(user_identifiant,password)

        if resultat == False :
            print(f"L'identifiant '{user_identifiant}' est déjà utilisé")

            from src.view.create_account_view import CreateAccountView

            return CreateAccountView()

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
            from src.view.connexion_view import ConnexionView

            return ConnexionView()

        else:
            from src.view.invite_view import InviteView

            return InviteView()