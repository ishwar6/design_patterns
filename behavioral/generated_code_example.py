python
import random

class Behavior:
    def __init__(self, name):
        self.name = name
    
    def perform(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

class RandomWalk(Behavior):
    def __init__(self, name, steps):
        super().__init__(name)
        self.steps = steps
    
    def perform(self):
        position = 0
        for _ in range(self.steps):
            step = random.choice([-1, 1])
            position += step
        return position

class SocialBehavior(Behavior):
    def __init__(self, name, traits):
        super().__init__(name)
        self.traits = traits
    
    def perform(self):
        interaction = random.choice(self.traits)
        return f"{self.name} interacts with {interaction}"

class MimicBehavior(Behavior):
    def __init__(self, name, sounds):
        super().__init__(name)
        self.sounds = sounds
    
    def perform(self):
        sound = random.choice(self.sounds)
        return f"{self.name} mimics sound: {sound}"