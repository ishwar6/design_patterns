# concepts/string_analyzer.py

class StringAnalyzer:
    """
    A class to analyze strings for various metrics such as word count,
    character count, and the frequency of characters.
    """

    def __init__(self, input_string: str):
        """
        Initializes the StringAnalyzer with a given string.

        :param input_string: The string to be analyzed
        """
        self.input_string = input_string

    def word_count(self) -> int:
        """
        Counts the number of words in the input string.

        :return: The total word count
        """
        if not self.input_string.strip():
            return 0
        return len(self.input_string.split())

    def character_count(self) -> int:
        """
        Counts the number of characters in the input string.

        :return: The total character count including spaces
        """
        return len(self.input_string)

    def character_frequency(self) -> dict:
        """
        Computes the frequency of each character in the input string.

        :return: A dictionary with characters as keys and their counts as values
        """
        frequency = {}
        for char in self.input_string:
            frequency[char] = frequency.get(char, 0) + 1
        return frequency


def main():
    """
    Sample usage of the StringAnalyzer class.
    """
    sample_text = "Hello, world! This is a test."
    analyzer = StringAnalyzer(sample_text)

    print(f"Input String: {sample_text}")
    print(f"Word Count: {analyzer.word_count()}")
    print(f"Character Count: {analyzer.character_count()}")
    print(f"Character Frequency: {analyzer.character_frequency()}")


if __name__ == "__main__":
    main()