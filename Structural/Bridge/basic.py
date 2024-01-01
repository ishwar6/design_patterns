# Bridge is a structural design pattern that lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—
# which can be developed independently of each other.

# Scenario: Universal Remote Control System
# Imagine a universal remote control system designed to operate various electronic devices like TVs, DVD players, and Music Systems.
# Each device type has its own set of functionalities, and the remote control interface should work with all these different devices.

#The challenge is to create a remote control system that is decoupled from the devices it controls,
# allowing for the easy addition of new types of devices without modifying the remote control interface and vice versa.

# Implementation Hierarchy

# This interface defines the operations that all devices should implement (like power on/off, volume up/down).
class Device:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

    def set_volume(self, volume):
        pass

# Concrete Implementations
class TV(Device):
    def turn_on(self):
        print("TV turned on")

    def turn_off(self):
        print("TV turned off")

    def set_volume(self, volume):
        print(f"TV volume set to {volume}")

class DVDPlayer(Device):
    def turn_on(self):
        print("DVD Player turned on")

    def turn_off(self):
        print("DVD Player turned off")

    def set_volume(self, volume):
        print(f"DVD Player volume set to {volume}")

# Abstraction Hierarchy
# This interface defines the operations provided by a remote control, like button presses.

class RemoteControl:
    def __init__(self, device):
        self.device = device

    def toggle_power(self):
        pass

# Refined Abstraction
class BasicRemoteControl(RemoteControl):
    def toggle_power(self):
        self.device.turn_on() if not self.device.is_on else self.device.turn_off()

# Extended Refined Abstraction
class AdvancedRemoteControl(BasicRemoteControl):
    def set_volume(self, volume):
        self.device.set_volume(volume)

# Usage
tv = TV()
remote = AdvancedRemoteControl(tv)
remote.toggle_power() # Turns on the TV
remote.set_volume(50) # Sets volume of the TV



# The Bridge Pattern is instrumental in this scenario, providing a scalable and flexible architecture 
# that separates the abstraction (remote controls) from their implementation (devices), allowing them to vary independently.
# This pattern is particularly useful in systems where abstractions and their implementations both can vary and need to be extended over time.
