from config import CONN, CURSOR
from song import Song

import ipdb; ipdb.set_trace()

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT
            EXISTS songs (id INTEGER PRIMARY KEY, name TEXT, album TEXT
            )
        """
        CURSOR.execute(sql)
        
    pass