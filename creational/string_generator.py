# creational/string_factory.py

class StringFactory:
    """
    A factory class to create various types of strings based on specified parameters.
    
    This class provides methods to create standardized strings such as 
    alphanumeric, numeric, and custom strings with specific lengths and characters.
    """

    @staticmethod
    def create_alphanumeric_string(length: int) -> str:
        """
        Create an alphanumeric string of the specified length.
        
        Args:
            length (int): Length of the generated string.
        
        Returns:
            str: An alphanumeric string of the specified length.
        
        Raises:
            ValueError: If length is less than 1.
        """
        if length < 1:
            raise ValueError("Length must be at least 1.")
        import random
        import string
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    @staticmethod
    def create_numeric_string(length: int) -> str:
        """
        Create a numeric string of the specified length.
        
        Args:
            length (int): Length of the generated string.
        
        Returns:
            str: A numeric string of the specified length.
        
        Raises:
            ValueError: If length is less than 1.
        """
        if length < 1:
            raise ValueError("Length must be at least 1.")
        import random
        characters = string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    @staticmethod
    def create_custom_string(length: int, characters: str) -> str:
        """
        Create a custom string of the specified length from the given characters.
        
        Args:
            length (int): Length of the generated string.
            characters (str): String of characters to choose from.
        
        Returns:
            str: A custom string of the specified length.
        
        Raises:
            ValueError: If length is less than 1 or characters is empty.
        """
        if length < 1:
            raise ValueError("Length must be at least 1.")
        if not characters:
            raise ValueError("Character set must not be empty.")
        import random
        return ''.join(random.choice(characters) for _ in range(length))


# Sample Usage
if __name__ == "__main__":
    print("Alphanumeric String (length 8):", StringFactory.create_alphanumeric_string(8))
    print("Numeric String (length 6):", StringFactory.create_numeric_string(6))
    print("Custom String (length 10, characters 'abc123'):", StringFactory.create_custom_string(10, 'abc123'))