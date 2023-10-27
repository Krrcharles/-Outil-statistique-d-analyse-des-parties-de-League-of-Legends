import os
import dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from src.utils.singleton import Singleton

class AbstractDAO(metaclass=Singleton):
    """
    Technical class to open only one connection to the DB.
    """

    def __init__(self):
        dotenv.load_dotenv(override=True)
        try:
            # Open the connection.
            self.__connection = psycopg2.connect(
                HOST=os.environ["HOST"],
                PORT=os.environ["PORT"],
                DATABASE=os.environ["DATABASE"],
                USER=os.environ["USER"],
                PASSWORD=os.environ["PASSWORD"],
                CURSOR_FACTORY=RealDictCursor,
            )
        except KeyError as e:
            raise ValueError(f"Missing environment variable: {e}") from None
        except Exception as e:
            raise ConnectionError("Unable to establish a database connection.") from e

    @property
    def connection(self):
        """
        return the opened connection.

        :return: the opened connection.
        """
        return self.__connection
