from SqlHandler import SqlHandler


class Produtos:
    def __init__(self, connector: SqlHandler) -> None:
        self.connector = connector

    @staticmethod
    def prepareJoin(join: bool|list):
        joins = ''
        if not join:
            return joins

        for item in join:
            joins += f"JOIN {item['table']} ON products.{item['foreing_key']} = {item['table']}.{item['primary_key']}"

        return joins

    def getById(self, id, join: bool|list=False):
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
        response = self.connector.execQuery(whereQuery)

        if not response:
            return False

        return response[0]

    def getAll(self, join: bool|list=False):
        joinQuery = self.prepareJoin(join=join)

        whereQuery = f"""
            select
                *
            from 
                products
            {joinQuery}
        """
        response = self.connector.execQuery(whereQuery)

        if not response:
            return False

        return response

    def getAllByCategory(self, category, join: bool|list=False):
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
        response = self.connector.execQuery(whereQuery)

        if not response:
            return False

        return response
