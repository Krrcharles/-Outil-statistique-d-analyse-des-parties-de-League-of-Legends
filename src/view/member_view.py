from InquirerPy import prompt
from InquirerPy.separator import Separator

from services.connexion_services import Connexion_services
from services.player_service import PlayerService
from services.champion_service import ChampionService

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
        champion_question = [
            {
                "type": "list",
                "name": "choix",
                "message": "What are you looking for",
                "choices": "Name Champion",
            }
        ]
        rank_champion_question = [
            {
                "type": "list",
                "name": "choix",
                "message": "What are you looking for",
                "choices": "Name Champion",
            }
        ]
        player_question = [
            {
                "type": "list",
                "name": "choix",
                "message": "What are you looking for",
                "choices": "Name Player",
            }
        ]
        self.__questions = questions
        self.__question = question
        self.infos_option = infos_option
        self.__champion_question = champion_question
        self.__rank_champion_question = rank_champion_question
        self.__player_question = player_question


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

            if answer['choix'] == "Stats Champion" :
                instance = ChampionService()

                rep = prompt[self.__champion_question]
                stats_champion = rep['choix']
                stats_champion = instance.afficher_stat_player(stats_champion)
                print (stats_champion)

            elif answer['choix'] == "Ranking Champion" :
                print ("RC")

            elif answer['choix'] == "Stats Player" :
                instance = PlayerService()

                rep = prompt(self.__player_question)
                stats_player = rep['choix']
                stats_player = instance.afficher_stat_player(stats_player)
                print (stats_player)
            
            else :
                instance = PlayerService()
                stats_player = instance.afficher_stat_player(answers["identifiant"])
                print (stats_player)


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



