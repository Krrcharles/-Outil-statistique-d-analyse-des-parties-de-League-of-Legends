import psycopg2

from typing import Optional
from src.dao.db_connection import AbstractDAO
from src.utils.singleton import Singleton

class participantDAO(metaclass=Singleton):
    """
    Communicate with the player table
    """

    def find_all_statistics(self) -> list[str]:
        """
        Get all statistics return a list

        :return: A list of the statistics of the participant
        :rtype: List of str
        """
        with AbstractDAO.connection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT *                                  "
                    "  FROM data                  "
                )

                # to store raw results
                res = cursor.fetchall()

        # Create an empty list to store formatted results
        participant_stat: list[str] = []

        # if the SQL query returned results (ie. res not None)
        if res:
            for row in res:
                participant_stat.append(row["summonerName"])

                print(row["summonerId"])

        return participant_stat

    def find_id_by_label(self, label: str) -> Optional[int]:
        """
        Get the id_participant from the label
        """
        with connection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT summonerId                  "
                    "  FROM data                       "
                    " WHERE summonerId = %(summonerId)s ",
                    {"participant": label},
                )
                res = cursor.fetchone()

        if res:
            return res["summonerId"]


if __name__ == "__main__":
    # Pour charger les variables d'environnement contenues dans le fichier .env
    import dotenv

    dotenv.load_dotenv(override=True)

    participant= participantDAO().find_all_statistics()
    print(participant)