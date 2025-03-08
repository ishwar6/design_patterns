# concepts/string_utils.py

class StringManipulator:
    """
    A class to perform various string manipulation operations.
    """

    @staticmethod
    def reverse_string(input_string: str) -> str:
        """
        Reverse the given string.

        :param input_string: The string to be reversed.
        :return: A new string which is the reverse of the input.
        """
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string.")
        
        return input_string[::-1]

    @staticmethod
    def is_palindrome(input_string: str) -> bool:
        """
        Check if the given string is a palindrome.

        :param input_string: The string to check.
        :return: True if the string is a palindrome, False otherwise.
        """
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string.")
        
        cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
        return cleaned_string == cleaned_string[::-1]

    @staticmethod
    def count_vowels(input_string: str) -> int:
        """
        Count the number of vowels in the given string.

        :param input_string: The string to count vowels in.
        :return: The number of vowels in the string.
        """
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string.")
        
        vowels = set('aeiouAEIOU')
        return sum(char in vowels for char in input_string)


# Sample Usage
if __name__ == "__main__":
    sample_string = "A man, a plan, a canal, Panama"
    
    reversed_string = StringManipulator.reverse_string(sample_string)
    print(f"Reversed String: {reversed_string}")  # Output: "amanaP ,analp ,an am A"

    is_palindrome = StringManipulator.is_palindrome(sample_string)
    print(f"Is Palindrome: {is_palindrome}")  # Output: True

    vowel_count = StringManipulator.count_vowels(sample_string)
    print(f"Vowel Count: {vowel_count}")  # Output: 10