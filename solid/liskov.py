# Liskov Substitution Principle (LSP)
# It is based on the concept of "substitutability" – a principle in object-oriented programming stating that an object (such as a class) 
# may be replaced by a sub-object (such as a class that extends the first class) without breaking the program. 


# this is simple: you can substitute Son in place of Father; you can put chile class in place of base class. 
# if putting son in place of father gives issue -> it breaks LSP; (eg. son can't go to work in father's office, a silly eg. but breaks LSP)

class Father:
    def goes_to_office(self):
        print("goes to office")

class Son(Father):
    def goes_to_office(self):
        raise Exception("Cannot go to office")

def testing_office_going_condition(Father: Father):
    Father.goes_to_office()


#now lets use it: we will pass son in last method. 

# This will raise an exception, violating LSP
try:
    testing_office_going_condition(Son())
except Exception as e:
    print(e)


# Circle–ellipse problem: a violation of LSP

# The existence of the circle–ellipse problem is sometimes used to criticize object-oriented programming.
# It may also imply that hierarchical taxonomies are difficult to make universal, 
# implying that situational classification systems may be more practical.


# so how to make it allow: LSP -> for methods that are not common (like going to office) put them in separate
# class or interface -> add only common methods like can_love, can_eat into base/father class :)


#for ex: here fly is not applicable to Penguin, so if we place penguin (a child class) in place of Bird (a base class) -> its an issue; 

class Bird:
    def fly(self):
        print("Bird is flying")

class Penguin(Bird):
    def fly(self):
        raise Exception("Cannot fly")

def test_bird_flying(bird: Bird):
    bird.fly()

# This will raise an exception, violating LSP
try:
    test_bird_flying(Penguin())
except Exception as e:
    print(e)



# lets take out fly() into another method and make base class with common method like eat only :)
class Bird:
    def eat(self):
        print("Bird is eating")

class FlyingBird(Bird):
    def fly(self):
        print("Bird is flying")

class SwimmingBird(Bird):
    def swim(self):
        print("Bird is swimming")

class Sparrow(FlyingBird):
    pass

class Penguin(SwimmingBird):
    pass

def test_bird_eating(bird: Bird):
    bird.eat()

def test_flying_bird(bird: FlyingBird):
    bird.fly()

# Now these functions respect LSP
test_bird_eating(Sparrow())
test_bird_eating(Penguin())
test_flying_bird(Sparrow())

# test_flying_bird(Penguin()) # This would be incorrect and should not be done



# LSP ensures that subclasses are proper extensions of their superclasses.
# By following LSP, we avoid surprises and bugs when using polymorphism, as subclasses behave as expected from the viewpoint of a superclass's contract.
# This leads to more robust and predictable object-oriented systems.


# this was given by Barbara Liskov in 1985 pressentation. 


