#__author__: Ishwar Jangid
#Strategy Pattern book definition:  this pattern allows defining a family of algorithms, encapsulating each one, 
# and making them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

#so Aggressive and Balanced are our algos and we will use them interchangably in GameCharacter Class. Here GameCharacter class is client in which algos are varying independently. 

from abc import ABC, abstractmethod

#strategy interface

class BattleStrategy(ABC):
    
    @abstractmethod
    def execute_strategy(self):
        pass
    

#implementation of different methods: We have 3 ALGORITHMS

class Aggressive(BattleStrategy):
    def execute_strategy(self):
        return "attack with full force!"
           
class Defensive(BattleStrategy):
    def execute_strategy(self):
        return "defend and counter-attack"
        
class Balanced(BattleStrategy):
    def execute_strategy(self):
        return "Balance between attack and defenced"
        
        


# we will use those strategies in this class: This is CLIENT
class GameCharacter:
    def __init__(self, strategy: BattleStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: BattleStrategy):
        self.strategy = strategy
        
    def execute_strategy(self):
        return self.strategy.execute_strategy()


#lets make strategies
agg = Aggressive()
defe = Defensive()


#this is plug and play: we plug defe, we get defe output
game = GameCharacter(defe)
print(game.execute_strategy())

game = GameCharacter(agg)
print(game.execute_strategy())

        












