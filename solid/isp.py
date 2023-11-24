# Bookish wiki def: the interface segregation principle (ISP) states that no code should be forced to depend on methods it does not use. 
# ISP is intended to keep a system decoupled and thus easier to refactor, change, and redeploy.


# father wants to make son actor as well as programmer -> son only loves acting (he might have seen us) -> forcing him to learn both will make things worst
# thats why ISP says -> make son only learn acting. :)

class Training:
    def develop_software(self):
        pass

    def learn_acting(self):
        pass

class Son(Training):
    def develop_software(self):
        # he just hates it
        pass

    def learn_acting(self):
        # Junior is not skilled in hardware
        print("Loving it!, learning acting is just awesome!")




# so, lets make training more fun and relavant 


from abc import ABC, abstractmethod

class SoftwareDevelopment(ABC):
    @abstractmethod
    def develop_software(self):
        pass

class LearnActing(ABC):
    @abstractmethod
    def learn_acting(self):
        pass

class Son(LearnActing):
    def learn_acting(self):
        print("Loving it!, learning acting is just awesome!")



# The Interface Segregation Principle advocates for creating specific interfaces instead of general-purpose, "do-it-all" interfaces.
# This approach ensures that implementing classes (like Son) don't get burdened with irrelevant methods,
# making the code more maintainable and easier to understand.
# It promotes a more focused and efficient design, especially in systems with a diverse set of clients with different needs.


# lets take a real case problem: 


#lets assume this is our base class:
class IDocumentProcessor:
    def read(self):
        pass

    def write(self):
        pass

    def print(self):
        pass

#other 2 will use above class (although with some issues): 

#class 1
class TextDocumentProcessor(IDocumentProcessor):
    def read(self):
        print("Reading a text document")

    def write(self):
        print("Writing to a text document")

    # TextDocumentProcessor doesn't need a print method
    def print(self):
        pass

#class 2
class Printer(IDocumentProcessor):
    # Printer only needs a print method
    def print(self):
        print("Printing document")
    
    def read(self):
        pass

    def write(self):
        pass

# TextDocumentProcessor and Printer are forced to implement methods they don't use. This violates ISP.


# Scenario With ISP (Adherence):
# To follow our great ISP, we would create specific interfaces for each distinct functionality.


from abc import ABC, abstractmethod

class IReader(ABC):
    @abstractmethod
    def read(self):
        pass

class IWriter(ABC):
    @abstractmethod
    def write(self):
        pass

class IPrinter(ABC):
    @abstractmethod
    def print(self):
        pass

class TextDocumentProcessor(IReader, IWriter):
    def read(self):
        print("Reading a text document")

    def write(self):
        print("Writing to a text document")

class Printer(IPrinter):
    def print(self):
        print("Printing document")

# TextDocumentProcessor implements IReader and IWriter, focusing only on reading and writing.
# Printer implements IPrinter, dedicated only to printing.
# Each class is responsible only for methods that are relevant to it, adhering to ISP.

# The example shows us how ISP promotes segregation of interfaces into smaller, more specific ones, 
# ensuring that implementing classes don't have to depend on interfaces they don't use









