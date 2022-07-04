import os

import mysql.connector
import mysql.connector.cursor
from dotenv import load_dotenv

load_dotenv('.env')

DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")


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
