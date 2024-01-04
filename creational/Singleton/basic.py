# The singleton pattern is used to limit creation of a class to only one object.
# This is beneficial when one (and only one) object is needed to coordinate actions across the system. 
  
# There are several examples of where only a single instance of a class should exist, including caches, thread pools, and registries.
# It’s trivial to initiate an object of a class — but how do we ensure that only one object ever gets created? 
# The answer is to make the constructor ‘private’ to the class we intend to define as a singleton.
# That way, only the members of the class can access the private constructor and no one else.

# Important consideration: It’s possible to subclass a singleton by making the constructor protected instead of private. 
#   This might be suitable under some circumstances. 
# One approach taken in these scenarios is to create a register of singletons of the subclasses and the getInstance method can take in a parameter or use an environment variable to return the desired singleton. 
# The registry then maintains a mapping of string names to singleton objects, which can be accessed as needed.


class Singleton:
    _instance = None

    def __new__(cls):
        '''
          We define a Singleton class that overrides the __new__ method. 
          The __new__ method is responsible for controlling the instance creation process. 
          It checks whether an instance already exists and creates one if it doesn't.
        '''
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.init_singleton()
        return cls._instance

    def init_singleton(self):
        # Initialize the Singleton instance as needed
        self.data = []

    def add_data(self, item):
        self.data.append(item)

# Example usage
s1 = Singleton()
s1.add_data("Data 1")

s2 = Singleton()

print(s1 is s2)  # True, both variables point to the same instance

s2.add_data("Data 2")

print(s1.data)  # ['Data 1', 'Data 2']


# Key Characteristics of a Singleton:

# Single Instance: A Singleton class should have only one instance that is shared by all clients.

# Global Access: Clients can access the Singleton instance globally, typically through a static method or property.

# Lazy Initialization: The Singleton instance is created only when it is first requested, ensuring efficient resource usage.

# Thread Safety: In a multi-threaded environment, the Singleton should be thread-safe to prevent the creation of multiple instances.



