# concepts/string_utilities.py

class StringManipulator:
    """
    A class to manipulate strings with various utility functions.
    """

    @staticmethod
    def reverse_string(input_string: str) -> str:
        """
        Reverses the given string.

        Args:
            input_string (str): The string to be reversed.

        Returns:
            str: The reversed string. If input is not a string, returns an error message.
        """
        if not isinstance(input_string, str):
            return "Error: Input must be a string"
        return input_string[::-1]

    @staticmethod
    def count_vowels(input_string: str) -> int:
        """
        Counts the number of vowels in the given string.

        Args:
            input_string (str): The string in which to count vowels.

        Returns:
            int: The count of vowels. Returns -1 if input is not a string.
        """
        if not isinstance(input_string, str):
            return -1
        vowels = 'aeiouAEIOU'
        return sum(1 for char in input_string if char in vowels)

    @staticmethod
    def capitalize_words(input_string: str) -> str:
        """
        Capitalizes the first letter of each word in the string.

        Args:
            input_string (str): The string to be capitalized.

        Returns:
            str: The string with each word capitalized. Returns an error message for non-string inputs.
        """
        if not isinstance(input_string, str):
            return "Error: Input must be a string"
        return ' '.join(word.capitalize() for word in input_string.split())

# Sample usage
if __name__ == "__main__":
    test_string = "hello world"
    print(StringManipulator.reverse_string(test_string))  # Output: "dlrow olleh"
    print(StringManipulator.count_vowels(test_string))    # Output: 3
    print(StringManipulator.capitalize_words(test_string)) # Output: "Hello World"