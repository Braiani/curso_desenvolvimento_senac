import mysql.connector
from mysql.connector import Error

class Database:

    def __init__(self, host, user, password, database) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None
        self.conector = None

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            if not self.conexao.is_connected():
                raise Error
            
            self.conector = self.conexao.cursor()
            
        except Error as err:
            print(f'Não foi possível conectar: {err}')

    def desconectar(self):
        if self.conexao.is_connected():
            self.conexao.close()
            self.conexao = None
            self.cursor = None

        print('Desconectado com sucesso!')
    
    def execute_query(self, query, params:None|list = None, commit:bool = False):
        try:
            self.conectar()

            cursor = self.conexao.cursor(dictionary=True)
            
            cursor.execute(query, params)
            if commit:
                self.conexao.commit()
                return cursor.rowcount
            else:
                records = cursor.fetchall()
                return records
            
        except Error as err:
            print(f'Ocorreu um erro: {err}')
            return False
        finally:
            self.desconectar()