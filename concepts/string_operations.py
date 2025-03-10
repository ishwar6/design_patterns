# concepts/string_utilities.py

from typing import List, Optional

class StringUtilities:
    """A utility class for string operations."""

    @staticmethod
    def split_string(input_string: str, delimiter: str = ' ') -> List[str]:
        """
        Splits a string into a list of substrings based on the provided delimiter.

        Args:
            input_string (str): The string to be split.
            delimiter (str): The delimiter on which to split the string. Defaults to space.

        Returns:
            List[str]: A list of substrings.

        Raises:
            ValueError: If input_string is empty or None.
        """
        if not input_string:
            raise ValueError("Input string cannot be empty or None.")

        return input_string.split(delimiter)

    @staticmethod
    def join_strings(strings: List[str], delimiter: str = ' ') -> str:
        """
        Joins a list of strings into a single string with the specified delimiter.

        Args:
            strings (List[str]): The list of strings to join.
            delimiter (str): The delimiter to use between strings. Defaults to space.

        Returns:
            str: A single string with all input strings joined by the delimiter.

        Raises:
            ValueError: If strings list is empty or contains only None.
        """
        if not strings or all(s is None for s in strings):
            raise ValueError("The list of strings cannot be empty or contain only None values.")

        return delimiter.join(strings)

    @staticmethod
    def capitalize_words(input_string: str) -> str:
        """
        Capitalizes the first letter of each word in the input string.

        Args:
            input_string (str): The string to capitalize words in.

        Returns:
            str: The input string with each word capitalized.

        Raises:
            ValueError: If input_string is empty or None.
        """
        if not input_string:
            raise ValueError("Input string cannot be empty or None.")

        return ' '.join(word.capitalize() for word in input_string.split())

# Sample Usage
if __name__ == "__main__":
    string_util = StringUtilities()

    # Example 1: Split a string
    sample_string = "hello world from python"
    split_result = string_util.split_string(sample_string)
    print(f"Split Result: {split_result}")

    # Example 2: Join a list of strings
    strings_to_join = ["hello", "world", "from", "python"]
    join_result = string_util.join_strings(strings_to_join, "-")
    print(f"Join Result: {join_result}")

    # Example 3: Capitalize words
    capitalized_result = string_util.capitalize_words(sample_string)
    print(f"Capitalized Result: {capitalized_result}")