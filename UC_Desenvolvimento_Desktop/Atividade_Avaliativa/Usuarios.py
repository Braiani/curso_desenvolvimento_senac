from SqlHandler import SqlHandler

class Usuarios:
    def __init__(self, usuario, senha) -> None:
        self.usuario = usuario
        self.senha = senha

    def validar_login(self):
        sql = SqlHandler()
        whereQuery = f"""
            select
                username, name
            from 
                users 
            where 
                username = '{self.usuario}'
                and password = '{self.senha}'
        """

        response = sql.execQuery(whereQuery)
        
        if not response:
            return False
        
        return response