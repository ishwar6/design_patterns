# behavioral/word_counter.py

from collections import Counter
import re

class WordCounter:
    """
    A class to count the occurrences of words in a given text.
    
    Attributes
    ----------
    text : str
        The input text for which word occurrences need to be counted.
        
    Methods
    -------
    count_words() -> dict
        Returns a dictionary with words as keys and their respective counts as values.
    """

    def __init__(self, text: str):
        """
        Constructs all the necessary attributes for the WordCounter object.
        
        Parameters
        ----------
        text : str
            The input text for counting words.
        """
        self.text = text.lower()

    def count_words(self) -> dict:
        """
        Counts the occurrences of each word in the instance's text.
        
        Returns
        -------
        dict
            A dictionary mapping each word to its count.
        """
        words = re.findall(r'\b\w+\b', self.text)
        word_count = Counter(words)
        return dict(word_count)

def sample_usage():
    """
    Demonstrates the usage of the WordCounter class.
    """
    sample_text = """
    Python is a great programming language. Python is used for web development,
    data science, and artificial intelligence. Python makes development easy and fun!
    """
    
    word_counter = WordCounter(sample_text)
    counts = word_counter.count_words()
    for word, count in counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    sample_usage()