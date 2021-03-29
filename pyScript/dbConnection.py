import os
from dotenv import load_dotenv, find_dotenv
import psycopg2
class Connction:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.DB_NAME = os.getenv('DB_NAME')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASS = os.getenv('DB_PASS')
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_PORT = os.getenv('DB_PORT')

    def makeConnection(self, db_name=""):
        db= db_name if db_name!="" else self.DB_NAME
        return psycopg2.connect(user=self.DB_USER,
        password=self.DB_PASS,
        host=self.DB_HOST,
        port=self.DB_PORT,
        database=db
        )
# data = Connction()
# if data.makeConnection():
#     print("Connected")
# else:
#     print("Error")
