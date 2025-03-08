# creational/item_factory.py

class Item:
    """Represents an item with a name and a price."""
    
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class ItemFactory:
    """A factory to create Item instances with specific configurations."""
    
    def __init__(self):
        self.items = []

    def create_item(self, name: str, price: float) -> Item:
        """Creates an Item instance and stores it in the factory."""
        if price < 0:
            raise ValueError("Price must be a non-negative value.")
        
        item = Item(name, price)
        self.items.append(item)
        return item

    def get_items(self):
        """Returns a list of all created items."""
        return self.items


# Sample usage
if __name__ == "__main__":
    factory = ItemFactory()
    item1 = factory.create_item("Apple", 0.99)
    item2 = factory.create_item("Banana", 0.59)
    
    print("Created Items:")
    for item in factory.get_items():
        print(item)