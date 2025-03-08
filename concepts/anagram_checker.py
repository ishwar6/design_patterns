# concepts/anagram_checker.py

from collections import Counter

class AnagramChecker:
    """
    A class to check if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters
    of a different word or phrase, using all the original letters
    exactly once.
    """

    @staticmethod
    def are_anagrams(str1: str, str2: str) -> bool:
        """
        Check if two strings are anagrams of each other.

        Args:
            str1 (str): The first string to compare.
            str2 (str): The second string to compare.

        Returns:
            bool: True if the strings are anagrams, False otherwise.
        """
        if len(str1) != len(str2):
            return False
        
        # Normalize case and remove whitespace
        normalized_str1 = str1.replace(" ", "").lower()
        normalized_str2 = str2.replace(" ", "").lower()
        
        return Counter(normalized_str1) == Counter(normalized_str2)


def main():
    """
    Sample usage of AnagramChecker.
    """
    test_cases = [
        ("listen", "silent"),
        ("triangle", "integral"),
        ("apple", "pale"),
        ("Dormitory", "Dirty room"),
        ("The eyes", "They see"),
        ("hello", "world"),
    ]

    for str1, str2 in test_cases:
        result = AnagramChecker.are_anagrams(str1, str2)
        print(f'"{str1}" and "{str2}" are anagrams: {result}')


if __name__ == "__main__":
    main()