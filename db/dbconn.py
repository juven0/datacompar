import pyodbc
import os 

class SqlServerDB:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = None

    def connect(self):
        try:
            self.conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                f'SERVER={self.server};'
                f'DATABASE={self.database};'
                f'UID={self.username};'
                f'PWD={self.password}'
            )
            print("Connection successful")
        except Exception as e:
            print(f"Error connecting to SQL Server: {e}")

    def execute_query(self, query):
        if not self.conn:
            print("Not connected to database")
            return
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            results = []
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            return results
        except Exception as e:
            print(f"Error executing query: {e}")
    def close(self):
        if self.conn:
            try:
                self.conn.close()
                print("Connection closed")
            except Exception as e:
                print(f"Error closing connection: {e}")