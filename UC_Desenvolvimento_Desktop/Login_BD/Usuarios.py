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
                usuarios.nome,
                usuarios.usuario,
                usuarios.mensagem,
                usuarios.photo,
                perfil.descricao
            from 
                usuarios 
            JOIN
                perfil ON usuarios.perfil_id = perfil.id
            where 
                usuarios.usuario = '{self.usuario}'
                and usuarios.senha = '{self.senha}'
        """

        response = sql.exec_query(where_query)

        
        if not response:
            return False
        
        return response

if __name__ == "__main__":
    import Main
    
    Main