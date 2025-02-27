import pymysql
from utilities.file_utils import ConfigReader


class DatabaseConnection:
    def __init__(self, env):
        config =  ConfigReader().get_config(env)
        self.connection = pymysql.connect(
            host=config['db_host'],
            user=config['db_user'],
            password=config['db_password']
        )

    def execute_query(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
        
    def close(self):
        self.connection.close()