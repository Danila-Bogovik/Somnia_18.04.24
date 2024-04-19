import sqlite3
from core.config import CONFIG

db_name = CONFIG["SqlLiteDB_path"]

class Database:
    def __init__(self):
        #debug
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS Users 
                           (
                                id TEXT PRIMARY KEY,
                                name TEXT NOT NULL,
                                email TEXT UNIQUE NOT NULL,
                                profile_pic TEXT NOT NULL
                            );""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS AllowedUsers
                           (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                email TEXT UNIQUE NOT NULL 
                            );""")

    def _fetchData(self, request:str) -> list:
        with sqlite3.connect(db_name) as connection:
            result = connection.cursor().execute(request).fetchall()
            return result
    
    def _fetchOneData(self, request:str) -> tuple:
        with sqlite3.connect(db_name) as connection:
            result = connection.cursor().execute(request).fetchone()
            return result

    def _executeData(self, request:str, parameters:tuple ) -> bool:
        try:
            with sqlite3.connect(db_name) as connection:
                connection.cursor().execute(request, parameters)
                connection.commit()
            return True
        except:
            return False