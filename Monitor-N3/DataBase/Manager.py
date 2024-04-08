import mysql.connector

class DatabaseManager:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost:3306",
            user="root",
            password = "orsep929",
            database = "monitor-n3"
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

