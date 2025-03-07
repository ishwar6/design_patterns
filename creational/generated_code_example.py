python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class DatabaseConnection(Singleton):
    def __init__(self, db_name):
        if not hasattr(self, 'initialized'):
            self.db_name = db_name
            self.initialized = True
            self.connect()

    def connect(self):
        print(f"Connecting to database: {self.db_name}")

def get_database_connection(db_name):
    return DatabaseConnection(db_name)