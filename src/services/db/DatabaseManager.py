import os, sys
          
import pymysql 
from dotenv import load_dotenv; load_dotenv()
import os 
from logging import getLogger


class DatabaseManager:

    def __init__(self):
        self.host = os.getenv("MYSQL_HOST")
        self.username =  os.getenv("MYSQL_USERNAME")
        self.password = os.getenv("MYSQL_PASSWORD")
        self.database_name = os.getenv("MYSQL_DATABASE")
        self.table_name = os.getenv("MYSQL_TABLE")

        self.logger = getLogger(__name__)

        try: 
            self.conn= pymysql.Connection(
                host=self.host,
                user=self.username,
                password=self.password
            )
            self.my_cursor = self.conn.cursor()
            self.logger.warning("MySQL Is Working")
            self.create_db_and_table_if_not_exists()
            

        except Exception as e :
            self.logger.warning(f"MySQL Is Down !!!\nError: {e}")

    def create_db_and_table_if_not_exists(self):

        self.my_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database_name}")
        self.my_cursor.execute(F"USE {self.database_name}")
        self.my_cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} ( id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(20), password VARCHAR(10), email VARCHAR(50));")    
        self.conn.commit()
        self.logger.warning(f"created database {self.database_name} & created table {self.table_name} successfully !")

    def fetch_data(self,limit: int=None):
        self.my_cursor.execute("SELECT * FROM users;")
        data = self.my_cursor.fetchmany(size=limit)
        return data
    

    def insert_into_users_table(self,username:str,password:str,email:str): 

        self.my_cursor.execute("SELECT * FROM users where username = %s AND password = %s AND email = %s", 
                               args=[username,password,email] )
        data = self.my_cursor.fetchone()

        if data is None:
            self.my_cursor.execute(F"INSERT INTO {self.table_name} (username,password,email) VALUES (%s,%s,%s)",
                                args=[username,password,email])
            self.conn.commit()
            self.logger.warning("data inserted ssuccessfully")
        


