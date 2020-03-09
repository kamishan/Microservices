
from flask_mysqldb import MySQL
import redis


class BDRedisConnetion:#conectando base de datos REDIS
    def __init__(self,hosst,Json_file):
        self.host = hosst
        self.jsonfile = Json_file
    
    def Insert_data(self):#insertando datos en REDIS
        redis_server = redis.Redis(self.host)
        redis_server.set("data",self.jsonfile)
        
 


class BDmySQLConnetion:#conectando base de datos mySQL
    def __init__(self,Jsonn,curs,mySQ):
        self.Json = Jsonn
        self.cursor = curs
        self.mysql = mySQ

    def Create_table(self):#Creando tablas
        self.cursor.execute("CREATE TABLE IF NOT EXISTS data ( data JSON NOT NULL )")
    
    def Insert_data(self):#insertando datos en mySQL
        self.cursor.execute("INSERT INTO data  VALUES (%s)",(self.Json,) )
        self.mysql.connection.commit()
        self.cursor.close()
