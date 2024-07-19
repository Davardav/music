import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database
        
    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''CREATE TABLE (
                          
                        )''') 

            conn.commit()

    def __executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()
    
    def __select_data(self, sql, data = tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()
            
    def get_music_by_id(self,id):
        sql = sql="""SELECT * FROM data 
WHERE id = ?"""
        return self.__select_data(sql,(id))
    
    def get_music_by_name(self,name):
        sql = sql="""SELECT * FROM data 
WHERE name = ?"""
        return self.__select_data(sql,(name))
    
    def top_popularity(self):
        sql = sql="""SELECT name, popularity FROM data 
ORDER BY popularity DESC
LIMIT 10"""
        return self.__select_data(sql)

    def top_worst_popularity(self):
        sql = sql="""SELECT name, popularity FROM data 
ORDER BY popularity
LIMIT 10"""
        return self.__select_data(sql)

    def top_long(self):
        sql = sql="""SELECT name, duration_ms FROM data 
ORDER BY duration_ms
LIMIT 10"""
        return self.__select_data(sql)
    
    def artistss(self,artists):
        sql = sql="""SELECT name FROM data 
        WHERE name = ?"""
        return self.__select_data(sql,(artists))

if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
