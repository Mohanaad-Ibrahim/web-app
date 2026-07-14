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
            self.logger.warning("MySQL Is Working")

        except Exception as e :
            self.logger.warning(f"MySQL Is Down !!!\nError: {e}")

    def create_db_and_table_if_not_exists(self):

        my_cursor = self.conn.cursor()
        my_cursor.execute(f"CREATE DATABASE {self.database_name} IF NOT EXISTS")
        my_cursor.execute(F"USE {self.database_name}")
        my_cursor.executemany(f"""
            CREATE TABLE {self.table_name} IF NOT EXISTS(
            id INR 
            
            )
        
    """)




