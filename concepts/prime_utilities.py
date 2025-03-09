# concepts/prime_checker.py

def is_prime(number: int) -> bool:
    """
    Check if a number is prime.

    A prime number is defined as a natural number greater than 1 that cannot be formed 
    by multiplying two smaller natural numbers. In other words, a prime number has no 
    positive divisors other than 1 and itself.

    Parameters:
    number (int): The number to check for primality.

    Returns:
    bool: True if number is prime, False otherwise.
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_primes_up_to(limit: int) -> list:
    """
    Generate a list of all prime numbers up to a given limit.

    This function uses the Sieve of Eratosthenes algorithm to find all primes 
    less than or equal to the specified limit.

    Parameters:
    limit (int): The upper limit up to which to find prime numbers.

    Returns:
    list: A list of prime numbers up to the specified limit.
    """
    if limit < 2:
        return []
        
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = False
                
    return [num for num, is_prime in enumerate(sieve) if is_prime]


if __name__ == "__main__":
    # Sample usage
    test_number = 29
    print(f"Is {test_number} a prime number? {is_prime(test_number)}")

    upper_limit = 50
    print(f"Prime numbers up to {upper_limit}: {generate_primes_up_to(upper_limit)}")