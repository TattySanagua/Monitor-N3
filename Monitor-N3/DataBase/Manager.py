import mysql.connector

class DatabaseManager:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password = "orsep929",
            database = "db_monitor3"
        )
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def execute_query(self, query): #INSERT, UPDATE and DELETE
        self.cursor.execute(query)
        self.connection.commit()

    def fetch_data(self, query): #SELECT
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_one(self, query):  # SELECT (una fila o valor)
        self.cursor.execute(query)
        return self.cursor.fetchone()