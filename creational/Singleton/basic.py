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

