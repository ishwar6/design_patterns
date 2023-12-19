# We need to render Shapes in Different Ways. 
# Assume a graphics application that needs to render shapes like circles and rectangles.
# These shapes can be rendered in different ways, such as raster graphics (pixel-based) or vector graphics (path-based).


# this is if we dont use bridge pattern: 
class Circle:
    def draw_pixel(self):
        print("Drawing a circle in pixel graphics")

    def draw_vector(self):
        print("Drawing a circle in vector graphics")

class Rectangle:
    def draw_pixel(self):
        print("Drawing a rectangle in pixel graphics")

    def draw_vector(self):
        print("Drawing a rectangle in vector graphics")

# Using to make circle and rectangle: 
circle = Circle()
circle.draw_pixel()  # Drawing a circle in pixel graphics
circle.draw_vector()  # Drawing a circle in vector graphics

rectangle = Rectangle()
rectangle.draw_pixel()  # Drawing a rectangle in pixel graphics
rectangle.draw_vector()  # Drawing a rectangle in vector graphics


# Problems Without Bridge Pattern

# Combination Explosion: For every new shape or rendering method, the number of methods grows exponentially.
# High Coupling: Shapes are tightly coupled with rendering methods, making the system less flexible.
# Difficult to Maintain: Adding a new rendering method requires modifying all shape classes.



############################## BRIDGE Approach ####################################

# Lets use bridge pattern: 
# approach we can use with Bridge Pattern

# Renderer Interface: An interface defining how to render shapes.
# RasterRenderer and VectorRenderer: Concrete implementations of the Renderer interface.
# Shape Class: An abstraction that has a reference to a Renderer. (Shapes and rendering methods are decoupled, allowing them to vary independently.)
# Circle and Rectangle: Refined abstractions that extend the Shape class. 
# (Adding a new shape or rendering method is easier and doesn't require modifying existing classes.)


from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render_shape(self, shape):
        pass

# Concrete Implementations
class RasterRenderer(Renderer):
    def render_shape(self, shape):
        print(f"Drawing {shape} in pixel graphics")

class VectorRenderer(Renderer):
    def render_shape(self, shape):
        print(f"Drawing {shape} in vector graphics")

# Shape Abstraction
class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass

# Concrete Shape Abstractions
class Circle(Shape):
    def draw(self):
        self.renderer.render_shape("circle")

class Rectangle(Shape):
    def draw(self):
        self.renderer.render_shape("rectangle")

# Usage
raster = RasterRenderer()
vector = VectorRenderer()

circle = Circle(raster)
circle.draw()  # Drawing circle in pixel graphics

rectangle = Rectangle(vector)
rectangle.draw()  # Drawing rectangle in vector graphics

# OUTPUT
# Drawing circle in pixel graphics
# Drawing rectangle in vector graphics




# Benefits of Using Bridge Pattern
# Decoupling: Shapes and rendering methods are decoupled, allowing them to vary independently.
# Scalability: Adding a new shape or rendering method is easier and doesn't require modifying existing classes.
# Flexibility: Can easily combine any shape with any rendering method.
# Single Responsibility Principle: Each class has a clear, distinct responsibility.


# The Bridge Pattern in this use case effectively separates the abstraction (shapes) from their implementation (rendering methods),
# providing a flexible and scalable design. This pattern is particularly useful in scenarios
# where both the abstractions (like different shapes) and their implementations (like rendering methods) can vary independently.





