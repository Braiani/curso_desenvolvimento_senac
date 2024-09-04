import mysql.connector
from mysql.connector import Error

class SqlHandle:
    def __init__(self) -> None:
        try:
            self.connection = mysql.connector.connect(host='10.28.2.15',
                                                      port='3306',
                                                      database='cadastros',
                                                      user='suporte',
                                                      password='suporte')
            if self.connection.is_connected():
                db_info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_info)
        except Error as e:
            print("Error while connecting to MySQL", e)
    
    def exec_query(self, query, params=None, commit=False):
        if not self.connection.is_connected():
            print("Não conectado ao banco de dados!")
            return False
        
        cursor = self.connection.cursor(dictionary=True)

        try:
            cursor.execute(query, params)
            if not commit:
                records = cursor.fetchall()
                return records
            else:
                self.connection.commit()
                return cursor.rowcount
        except Error as e:
            print(e)
            return False
        finally:
            cursor.close()



def adicionar_numero_cell(connector: SqlHandle):
    sql = "SELECT * FROM cliente"

    registros = connector.exec_query(sql)

    for registro in registros:
        if len(registro['telefone_cliente']) > 10:
            continue

        query = "UPDATE cliente SET telefone_cliente = %s WHERE id_cliente = %s"

        new_tel = ''
        count = 0
        for n in registro['telefone_cliente']:
            if count == 2:
                new_tel += '9'
            new_tel += n
            count +=1
        
        connector.exec_query(query=query, params=(new_tel, registro['id_cliente']), commit=True)
    
    print("Tudo certo!!!\n\n")
    
            

def alter_cidade_curitiba(connector: SqlHandle):
    sql = "SELECT * FROM cidade"

    print(connector.exec_query(sql))

def alter_dominio_email(conncetor: SqlHandle):
    pass

def mostrar_menu():
    print("\n--- Menu Principal ---")
    print("1. Adicione um 9 a mais no telefone")
    print("2. A cidade de Curitiba agora fará parte do estado do RJ")
    print("3. Altere o domínio do cliente 20 ao 45, substitua @exemplo.com para @teste.com")
    print("4. Sair")


if __name__ == '__main__':
    connector = SqlHandle()

    while True:
        mostrar_menu()
        try:
            escolha = input("Escolha uma opção (1-4): ")
        except KeyboardInterrupt:
            escolha = '4'

        if escolha == '1':
            adicionar_numero_cell(connector=connector)
        elif escolha == '2':
            alter_cidade_curitiba(connector=connector)
        elif escolha == '3':
            alter_dominio_email(conncetor=connector)
        elif escolha == '4':
            print("\nSaindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
