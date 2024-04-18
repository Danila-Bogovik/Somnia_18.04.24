import sqlite3
from app.config import CONFIG

db_name = CONFIG["SqlLiteDB_path"]

class Database:
    def __init__(self):
        # with sqlite3.connect(db_name) as connection:
        #     cursor = connection.cursor()
        #     cursor.execute("""CREATE TABLE IF NOT EXISTS Users
        #                 (
        #                     uid INTEGER PRIMARY KEY AUTOINCREMENT,
        #                     username TEXT,
        #                     password TEXT,
        #                 );""")
        pass

    def fetchData(self, request:str) -> list:
        try:
            with sqlite3.connect(db_name) as connection:
                result = connection.cursor().execute(request).fetchall()
                if result == None:
                    raise Exception()
                else:
                    return result
        except:
            return []
    
    def fetchOneData(self, request:str) -> tuple:
        try:
            with sqlite3.connect(db_name) as connection:
                result = connection.cursor().execute(request).fetchone()
                if result == None:
                    raise Exception()
                else:
                    return result
        except:
            return ()
    
    def executeData(self, request:str, parameters:tuple ) -> bool:
        try:
            with sqlite3.connect(db_name) as connection:
                connection.cursor().execute(request, parameters)
                connection.commit()
            return True
        except:
            return False