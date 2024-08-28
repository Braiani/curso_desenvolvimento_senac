from SqlHandler import SqlHandler
class Produtos:
    def __init__(self) -> None:
        pass

    def prepareJoin(self, join: list):
        joins = ''
        if not join:
            return joins
        
        for item in join:
            joins += f"JOIN {item['table']} ON products.{item['foreing_key']} = {item['table']}.{item['primary_key']}"
        
        return joins

    def getById(self, id, join = False):
        sql = SqlHandler()
        joinQuery = self.prepareJoin(join=join)

        whereQuery = f"""
            select
                *
            from 
                products
            {joinQuery}
            where 
                products.id = '{id}'
        """
        response = sql.execQuery(whereQuery)
        
        if not response:
            return False
        
        return response[0]
    
    def getAll(self, join = False):
        sql = SqlHandler()
        joinQuery = self.prepareJoin(join=join)

        whereQuery = f"""
            select
                *
            from 
                products
            {joinQuery}
        """
        response = sql.execQuery(whereQuery)
        
        if not response:
            return False
        
        return response
    
    def getAllByCategory(self, category, join = False):
        sql = SqlHandler()
        joinQuery = self.prepareJoin(join=join)

        whereQuery = f"""
            select
                *
            from 
                products
            {joinQuery}
            where
                products.category_id = {category}
        """
        response = sql.execQuery(whereQuery)
        
        if not response:
            return False
        
        return response