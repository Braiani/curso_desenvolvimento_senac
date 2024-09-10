from SqlHandler import SqlHandler

class Usuarios:
    def __init__(self, usuario: str, senha: str, connector: SqlHandler) -> None:
        self.usuario = usuario
        self.senha = senha
        self.connector = connector

    def validar_login(self):
        sql = self.connector
        where_query = f"""
            select
                username, name, mensagem, photo
            from 
                users 
            where 
                username = '{self.usuario}'
                and password = '{self.senha}'
        """

        response = sql.exec_query(where_query)
        
        if not response:
            return False
        
        return response

if __name__ == "__main__":
    import Main
    
    Main