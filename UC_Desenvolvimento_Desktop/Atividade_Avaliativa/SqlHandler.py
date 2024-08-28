import mysql.connector
from mysql.connector import Error

class SqlHandler:
    def __init__(self) -> None:
        try:
            self.connection = mysql.connector.connect(host='10.28.2.15',
                                                      port='3306',
                                                      database='pythonapps',
                                                      user='suporte',
                                                      password='suporte')
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
        except Error as e:
            print("Error while connecting to MySQL", e)

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