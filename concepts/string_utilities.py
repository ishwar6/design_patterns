# concepts/string_utilities.py

class StringUtilities:
    """A collection of utilities for string manipulation."""

    @staticmethod
    def reverse_string(input_string: str) -> str:
        """Reverses the provided string.

        Args:
            input_string (str): The string to be reversed.

        Returns:
            str: The reversed string.
        """
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string.")
        return input_string[::-1]

    @staticmethod
    def is_palindrome(input_string: str) -> bool:
        """Checks if the provided string is a palindrome.

        Args:
            input_string (str): The string to be checked.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string.")
        cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
        return cleaned_string == cleaned_string[::-1]

    @staticmethod
    def count_vowels(input_string: str) -> int:
        """Counts the number of vowels in the provided string.

        Args:
            input_string (str): The string to be checked.

        Returns:
            int: The number of vowels in the string.
        """
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string.")
        return sum(1 for char in input_string.lower() if char in 'aeiou')


# Sample usage
if __name__ == "__main__":
    sample_string = "A man, a plan, a canal, Panama"

    reversed_str = StringUtilities.reverse_string(sample_string)
    print(f"Reversed String: {reversed_str}")

    palindrome_check = StringUtilities.is_palindrome(sample_string)
    print(f"Is Palindrome: {palindrome_check}")

    vowel_count = StringUtilities.count_vowels(sample_string)
    print(f"Vowel Count: {vowel_count}")