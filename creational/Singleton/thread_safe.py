import threading

class Singleton:
    """
    Singleton class that ensures only one instance is created.

    This class implements the Singleton pattern, allowing only one instance of the
    class to be created. It also provides thread safety using a lock.

    Attributes:
        _instance (Singleton): The single instance of the Singleton class.
        _lock (threading.Lock): Lock for ensuring thread safety during instance creation.
    """

    _instance = None
    _lock = threading.Lock()  # This is the lock for thread safety

    def __new__(cls):
        """
        Create or return the Singleton instance.

        Returns:
            Singleton: The single instance of the Singleton class.
        """
        if cls._instance is None:
            with cls._lock:  # Use a lock to ensure thread safety
                if cls._instance is None:  # Double-check for instance existence
                    cls._instance = super(Singleton, cls).__new__(cls)
                    cls._instance.init_singleton()
        return cls._instance

    def init_singleton(self):
        """
        Initialize the Singleton instance.

        This method initializes the Singleton instance as needed. You can customize
        this method to perform any necessary setup.

        Returns:
            None
        """
        self.data = []

    def add_data(self, item):
        """
        Add data to the Singleton instance.

        Args:
            item (Any): The data item to be added to the Singleton.

        Returns:
            None
        """
        self.data.append(item)

# Example usage with multiple threads
def worker():
    singleton = Singleton()
    singleton.add_data("Data from Thread")

threads = []
for _ in range(5):
    thread = threading.Thread(target=worker)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

singleton = Singleton()
print(singleton.data)  
