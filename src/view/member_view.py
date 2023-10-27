from InquirerPy import prompt
from InquirerPy.separator import Separator
from services.connexion_services import Connexion_services
from services.player_service import PlayerService

from view.invite_view import InviteView
from view.session import Session


class MemberView(InviteView):
    def __init__(self):
        super().__init__()
        self.infos_option.append(Separator("🔍"))
        self.infos_option.append("Stats Account")
        questions = [
            {
                "type": "input",
                "name": "identifiant",
                "message": "What is your login",
            },
            {
                "type": "input",
                "name": "password",
                "message": "What is your password",
            },]
        question = [{
                "type": "list",
                "name": "choix",
                "message": "What are you looking for",
                "choices": self.infos_option,
            },
        ]
        self.__questions = questions
        self.__question = question


    def display_info(self):
        print(f"") # a def

    def make_choice(self):
        answers = prompt(self.__questions)

        Session().user_identifiant = answers["identifiant"]
        Session().user_mdp = answers["password"]

        user_identifiant = answers["identifiant"]
        password = answers["password"]
        
        # Vérification que l'identifiant existe, et que l'identifiant et le mot de passe coincident 

        instance = Connexion_services()
        resultat = instance.connexion(user_identifiant,password)

        if resultat == "failed" :
            print(f"Il se peut que votre nom d'utilisateur ou mot de passe soit incorrect ou que vous deviez passer à un compte Riot si vous n'avez pas joué depuis quelques mois.")

            from view.member_view import MemberView

            return MemberView()

        elif resultat == "admin":
            from view.admin_view import AdminView

            return AdminView()

        while True:
            answer = prompt(self.__question)

            # Méthodes

            if answer['choix'] == "Stats Champion" :
                print ("SC")

            elif answer['choix'] == "Ranking Champion" :
                print ("RC")

            elif answer['choix'] == "Stats Player" :
                pass
            
            else :
                print("SA")

            self.display_info()  # Appelez la fonction display_info pour afficher les informations

            another_infos = prompt(
                [
                    {
                        "type": "confirm",
                        "name": "continue",
                        "message": "Another Information ?",
                        "default": True,
                    }
                ]
            )

            if not another_infos["continue"]:
                from view.start_view import StartView

                return StartView()



