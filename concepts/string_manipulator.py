# concepts/string_manipulator.py

class StringManipulator:
    """
    A class to perform various string manipulation operations.
    """

    @staticmethod
    def reverse_string(input_string: str) -> str:
        """
        Reverses the given string.

        Parameters:
        input_string (str): The string to be reversed.

        Returns:
        str: The reversed string.
        """
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string.")
        return input_string[::-1]

    @staticmethod
    def is_palindrome(input_string: str) -> bool:
        """
        Checks if the given string is a palindrome.

        Parameters:
        input_string (str): The string to check.

        Returns:
        bool: True if the string is a palindrome, False otherwise.
        """
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string.")
        cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
        return cleaned_string == cleaned_string[::-1]

    @staticmethod
    def count_vowels(input_string: str) -> int:
        """
        Counts the number of vowels in the given string.

        Parameters:
        input_string (str): The string to analyze.

        Returns:
        int: The number of vowels in the string.
        """
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string.")
        vowels = "aeiouAEIOU"
        return sum(1 for char in input_string if char in vowels)


# Sample usage
if __name__ == "__main__":
    test_string = "A man a plan a canal Panama"

    reversed_string = StringManipulator.reverse_string(test_string)
    is_palindrome_result = StringManipulator.is_palindrome(test_string)
    vowel_count = StringManipulator.count_vowels(test_string)

    print(f"Original String: {test_string}")
    print(f"Reversed String: {reversed_string}")
    print(f"Is Palindrome: {is_palindrome_result}")
    print(f"Number of Vowels: {vowel_count}")