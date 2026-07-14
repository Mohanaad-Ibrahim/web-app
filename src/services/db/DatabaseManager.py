import os, sys
_here = os.path.dirname(os.path.abspath(__file__))  
_src  = os.path.abspath(os.path.join(_here, ".."));     sys.path.insert(0, _here);          sys.path.insert(0, _src)           
import pymysql 
from dotenv import load_dotenv; load_dotenv()
import os 
from logging import getLogger

# cd src && python -m streamlit run streamlit_app/app.py

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
        self.logger.info(f"created database {self.database_name} & created table {self.table_name} successfully !")

    def fetch_data(self,limit: int=None):
        self.my_cursor.execute("SELECT * FROM users ")
        data = self.my_cursor.fetchmany(size=limit)
        return data
    








