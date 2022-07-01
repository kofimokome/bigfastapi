import mysql.connector
import mysql.connector.cursor
from decouple import config


DB_NAME = 'cpmeapi'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_PORT = '3306'


class DB:
    cnx: mysql.connector = None
    is_cnx_initialised = False

    @staticmethod
    def init() -> mysql.connector.cursor:
        config = {
            'user': DB_USER,
            'password': DB_PASSWORD,
            'host': DB_HOST,
            'database': DB_NAME,
            'raise_on_warnings': True
        }

        DB.cnx = mysql.connector.connect(**config)
        return DB.cnx.cursor()

    @staticmethod
    def get_cursor() -> mysql.connector.cursor:
        if DB.is_cnx_initialised:
            return DB.cnx.cursor()
        else:
            return DB.init()

    @staticmethod
    def get_db() -> mysql.connector:
        return DB.cnx
