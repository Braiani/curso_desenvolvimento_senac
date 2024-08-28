from SqlHandler import SqlHandler

class Categoria:
    def __init__(self) -> None:
        pass

    def getById(self, id):
        sql = SqlHandler()
        whereQuery = f"""
            select
                id,
                description as descricao
            from 
                categories
            where 
                id = '{id}'
        """
        response = sql.execQuery(whereQuery)
        
        if not response:
            return False
        
        return response
    
    def getAll(self):
        sql = SqlHandler()
        whereQuery = f"""
            select
                id,
                description as descricao
            from 
                categories
        """
        response = sql.execQuery(whereQuery)
        
        if not response:
            return False
        
        return response