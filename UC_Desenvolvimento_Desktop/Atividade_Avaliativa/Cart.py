class Cart:
    def __init__(self, connector) -> None:
        self.connector = connector

    def get_all(self):
        query = "SELECT * FROM cart"
        response = self.connector.exec_query(query)
        return response if response else False

    def add_item(self, product_id, quantity):
        query = "INSERT INTO cart (product_id, quantity, status) VALUES (%s, %s, %s)"
        params = (product_id, quantity, 'open')
        response = self.connector.exec_query(query, params, True)
        return True if response else False

    def remove_item(self, product_id):
        query = "DELETE FROM cart WHERE product_id = %s"
        params = (product_id,)
        response = self.connector.exec_query(query, params, True)
        return True if response else False

    def update_item(self, product_id, quantity):
        query = "UPDATE cart SET quantity = %s WHERE product_id = %s"
        params = (quantity, product_id)
        response = self.connector.exec_query(query, params, True)
        return True if response else False

    def get_total(self):
        query = """
            SELECT SUM(p.price * c.quantity) AS total
            FROM cart c
            JOIN products p ON p.id = c.product_id
        """
        response = self.connector.exec_query(query)
        return response[0]['total'] if response else False

    def finish_cart(self):
        query = "UPDATE cart SET status = 'closed'"
        response = self.connector.exec_query(query, commit=True)
        if not response:
            return False

    def get_open_cart(self):
        query = "SELECT * FROM cart WHERE status = 'open'"
        response = self.connector.exec_query(query)
        return response if response else False