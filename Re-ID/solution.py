# solution.py


def generate_primes():
    """Generates an infinite sequence of prime numbers using the Sieve of Eratosthenes.

    Yields:
        int: The next prime number.
    """
    composite_to_primes = {}
    test_prime = 2  # Starting integer to check for primality

    while True:
        if test_prime not in composite_to_primes:
            # test_prime is a new prime. Yield it and mark its first multiple.
            yield test_prime
            composite_to_primes[test_prime * test_prime] = [test_prime]
        else:
            # test_prime is not a prime. Increment multiples of its smallest prime factor.
            for prime in composite_to_primes[test_prime]:
                composite_to_primes.setdefault(prime + test_prime, []).append(prime)
            # Remove this number from the dictionary as we are done with it.
            del composite_to_primes[test_prime]
        test_prime += 1


def get_primes_string(max_length):
    """Generates a string of prime numbers concatenated together up to a max length.

    Args:
        max_length (int): The desired minimum length of the prime number string.

    Returns:
        str: A string of concatenated prime numbers up to the desired length.
    """
    prime_gen = generate_primes()
    primes_string = ""
    for prime in prime_gen:
        primes_string += str(prime)
        if len(primes_string) >= max_length:
            break
    return primes_string


def solution(i):
    """Finds the substring of the first 'n' concatenated prime numbers.

    Given an index n, this function generates a string of concatenated prime numbers
    and returns a substring of length 5 starting from that index.

    Args:
        i (int): The starting index from where to extract the 5-digit substring.

    Returns:
        str: The 5-digit substring starting at index n.
    """
    # Calculate the necessary string length to include the index and the 5 digits.
    needed_length = i + 5
    primes_string = get_primes_string(needed_length)
    return primes_string[i : i + 5]
