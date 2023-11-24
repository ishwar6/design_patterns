# lets make a remote: that can work with TV, AC and Fridge. 
# It can do on and off : all devices. 

# Python Code for Abstraction:

from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


# this is abstraction: we created remote, that can do on off; 
# we created a high-level interface (the universal remote) that hides the complex details of each device.


# Note that this class is totally different, not inheriting or related to above Device Class. :)
class Television:
    def __init__(self):
        self._volume = 10  # Internal state and it is not directly accessible

    def increase_volume(self):
        if self._volume < 100:
            self._volume += 1
        print(f"Volume: {self._volume}")

    def decrease_volume(self):
        if self._volume > 0:
            self._volume -= 1
        print(f"Volume: {self._volume}")


# The Television class encapsulates the volume attribute. 
# It's marked as private (with an underscore) to indicate that it should not be accessed directly from outside the class.



# This is Encapsulation - we have wrapped the complex internals of the TV and exposed only what is necessary to the user, 
# protecting the internal state and functionality.


# Abstraction is about hiding complexity by creating simple interfaces. 
# It's like the universal remote, allowing users to interact with devices without knowing their internal workings.
# AND
# Encapsulation is about protecting the internal state of an object and only exposing what is necessary.
# It's like the internal workings of the TV, which are hidden from the user, providing a safeguard against misuse.



