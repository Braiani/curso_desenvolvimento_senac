import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

class SqlHandler:
    def __init__(self) -> None:
        try:
            config = self.get_info_from_env()
            if not config:
                raise Exception('Erro ao carregar variáveis de ambiente')
            
            self.connection = mysql.connector.connect(host=config['host'],
                                                      port=config['port'],
                                                      database=config['database'],
                                                      user=config['user'],
                                                      password=config['password'])
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
        except Error as e:
            print("Error while connecting to MySQL", e)

    def get_info_from_env(self):
        try:
            load_dotenv()
            return {
                'host': os.getenv('host', '10.28.2.15'),
                'port': os.getenv('port', '3306'),
                'database': os.getenv('database', 'pythonapps'),
                'user': os.getenv('user', 'suporte'),
                'password': os.getenv('password', 'suporte')
            }
        except:
            print('Erro ao carregar variáveis de ambiente')
            return False

    def execQuery(self, query):
        if not self.connection.is_connected():
            print("Não conectado ao banco de dados!")
            return False
        
        cursor = self.connection.cursor()

        try:
            cursor.execute(query)
            records = cursor.fetchall()

            cursor.close()

            return records
        except Error as e:
            print(e)
            cursor.close()
            return False