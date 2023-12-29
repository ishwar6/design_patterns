import sqlite3
import threading

class DatabaseConnectionPool:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(DatabaseConnectionPool, cls).__new__(cls)
                    cls._instance.init_pool()
        return cls._instance

    def init_pool(self, initial_size=5, db_file="my_database.db"):
        self.connections = []
        self.db_file = db_file
        for _ in range(initial_size):
            connection = sqlite3.connect(self.db_file)
            self.connections.append(connection)

    def get_connection(self):
        if len(self.connections) > 0:
            return self.connections.pop()
        else:
            print("No available connections.")
            return None

    def release_connection(self, connection):
        if connection:
            self.connections.append(connection)

# lets create our first pool: 
pool1 = DatabaseConnectionPool()
connection1 = pool1.get_connection()
print("Connection 1:", connection1)

# similarly, second
pool2 = DatabaseConnectionPool()
connection2 = pool2.get_connection()
print("Connection 2:", connection2)

# Check if both instances refer to the same pool
print("Pool 1 is Pool 2:", pool1 is pool2)  # True

# Release connections back to the pool
pool1.release_connection(connection1)
pool2.release_connection(connection2)
