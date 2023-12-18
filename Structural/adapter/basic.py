# this is the Target Interface. This interface will be used in rest of adapters. like mysql, psql, mongodb etc. 

class DatabaseInterface:
    def connect(self):
        pass

    def execute_query(self, query):
        pass


# Lets implement: first adapter by using above DatabaseInterface. 

import mysql.connector

class MySQLAdapter(DatabaseInterface):
    def __init__(self, host, user, password, database):
        self.connection = None
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result



# EXAMPLE 2: Lets implement: second adapter by using above DatabaseInterface. 
import psycopg2

class PostgreSQLAdapter(DatabaseInterface):
    def __init__(self, host, user, password, database):
        self.connection = None
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        self.connection = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result


#CALLING: 

# Initialize adapters
mysql_adapter = MySQLAdapter('localhost', 'root', 'password', 'db')
postgresql_adapter = PostgreSQLAdapter('localhost', 'user', 'password', 'psql_db')

# Connect to MySQL
mysql_adapter.connect()
result = mysql_adapter.execute_query('SELECT * FROM users')
print('MySQL Results:', result)

# Connect to PostgreSQL
postgresql_adapter.connect()
result = postgresql_adapter.execute_query('SELECT * FROM users')
print('PostgreSQL Results:', result)



