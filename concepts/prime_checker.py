# concepts/prime_checker.py

from typing import List, Tuple

class PrimeChecker:
    """A class to check for prime numbers in a given range and provide prime factors of a number."""

    @staticmethod
    def is_prime(number: int) -> bool:
        """Check if a number is prime.

        Args:
            number (int): The number to be checked.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def prime_factors(number: int) -> List[int]:
        """Return a list of prime factors of the given number.

        Args:
            number (int): The number to find prime factors for.

        Returns:
            List[int]: A list of prime factors of the number.
        """
        factors = []
        if number <= 1:
            return factors
        for i in range(2, number + 1):
            while number % i == 0:
                if i not in factors:
                    factors.append(i)
                number //= i
        return factors

    @staticmethod
    def find_primes_in_range(start: int, end: int) -> List[int]:
        """Find all prime numbers in a specified range (inclusive).

        Args:
            start (int): The starting number of the range.
            end (int): The ending number of the range.

        Returns:
            List[int]: A list of prime numbers found in the range.
        """
        if start > end:
            raise ValueError("Start must be less than or equal to End.")
        return [num for num in range(start, end + 1) if PrimeChecker.is_prime(num)]


# Sample usage
if __name__ == "__main__":
    prime_checker = PrimeChecker()
    
    # Find primes in a range
    primes = prime_checker.find_primes_in_range(10, 50)
    print(f"Prime numbers between 10 and 50: {primes}")  # Should print a list of prime numbers
    
    # Get prime factors of a number
    number = 60
    prime_factors = prime_checker.prime_factors(number)
    print(f"Prime factors of {number}: {prime_factors}")  # Should print the prime factors of 60