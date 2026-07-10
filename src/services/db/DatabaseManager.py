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

        self.logger = getLogger(__name__)

        try: 
            self.conn= pymysql.Connection(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database_name
            )
            self.logger.warning("MySQL Is Working")

        except Exception as e :
            self.logger.warning(f"MySQL Is Down !!!\nError: {e}")
