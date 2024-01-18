#https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs
#CQRS stands for Command and Query Responsibility Segregation, a pattern that separates read and update operations for a data store. 
#Implementing CQRS in your application can maximize its performance, scalability, and security. 
#The flexibility created by migrating to CQRS allows a system to better evolve over time and prevents update commands from causing merge conflicts at the domain level.

#https://martinfowler.com/bliki/CQRS.html
# At its heart is the notion that you can use a different model to update information than the model you use to read information. 
# For some situations, this separation can be valuable, but beware that for most systems CQRS adds risky complexity.

# The change that CQRS introduces is to split that conceptual model into separate models for update and display, 
# which it refers to as Command and Query respectively following the vocabulary of CommandQuerySeparation.

# CQRS fits well with event-based programming models. It's common to see CQRS system split into separate services communicating with Event Collaboration.
# This allows these services to easily take advantage of Event Sourcing.

# The other main benefit is in handling high performance applications. CQRS allows you to separate the load from reads and writes allowing you to scale each independently. 
# If your application sees a big disparity between reads and writes this is very handy. Even without that, you can apply different optimization strategies to the two sides. 
# An example of this is using different database access techniques for read and update.

from abc import ABC, abstractmethod
from typing import List, Union

# Query interface

# Query Interface (ProductsDao): This interface defines methods for querying product-related data. 
# It corresponds to the "query" part of CQRS, responsible for retrieving data from the system.

class ProductsDao(ABC):
    @abstractmethod
    def find_by_id(self, product_id: int):
        pass

    @abstractmethod
    def find_by_name(self, name: str) -> List[ProductDisplay]:
        pass

    @abstractmethod
    def find_out_of_stock_products(self) -> List[ProductInventory]:
        pass

    @abstractmethod
    def find_related_products(self, product_id: int) -> List[ProductDisplay]:
        pass

# ProductDisplay and ProductInventory Classes: These classes represent the data models for displaying product information and managing inventory. 
# They are used to structure the data returned by queries.

class ProductDisplay:
    def __init__(self, id, name, description, unit_price, is_out_of_stock, user_rating):
        self.id = id
        self.name = name
        self.description = description
        self.unit_price = unit_price
        self.is_out_of_stock = is_out_of_stock
        self.user_rating = user_rating

class ProductInventory:
    def __init__(self, id, name, current_stock):
        self.id = id
        self.name = name
        self.current_stock = current_stock



# Command handlers
# ProductsCommandHandler Class: This class implements command handlers for various operations like 
# adding a new product, rating a product, adding to inventory, confirming items shipped, and updating stock from an inventory recount.
# Each method in this class corresponds to a command and handles the "command" part of CQRS, where write operations are performed.

class ProductsCommandHandler:
    def __init__(self, repository):
        self.repository = repository

    def handle_add_new_product(self, command):
        # Handle adding a new product
        pass

    def handle_rate_product(self, command):
        product = self.repository.find(command.product_id)
        if product:
            product.rate_product(command.user_id, command.rating)
            self.repository.save(product)

    def handle_add_to_inventory(self, command):
        # Handle adding to inventory
        pass

    def handle_confirm_items_shipped(self, command):
        # Handle confirming items shipped
        pass

    def handle_update_stock_from_inventory_recount(self, command):
        # Handle updating stock from inventory recount
        pass

# Example command classes
# Command Classes: The command classes (e.g., AddNewProduct, RateProduct) encapsulate the data required to perform specific write operations.
# They are used to send commands to the ProductsCommandHandler.
class AddNewProduct:
    def __init__(self, product_data):
        self.product_data = product_data

class RateProduct:
    def __init__(self, product_id, user_id, rating):
        self.product_id = product_id
        self.user_id = user_id
        self.rating = rating

class AddToInventory:
    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity

class ConfirmItemsShipped:
    def __init__(self, order_id):
        self.order_id = order_id

class UpdateStockFromInventoryRecount:
    def __init__(self, product_id, new_stock_count):
        self.product_id = product_id
        self.new_stock_count = new_stock_count


# We saw that the this Python code provided follows the principles of CQRS by separating the concerns of read (query) and write (command) operations. 
# The ProductsDao handles query-related tasks, while the ProductsCommandHandler manages command-related tasks, adhering to the CQRS pattern.






