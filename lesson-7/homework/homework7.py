# 1. is_prime(n)
def is_prime(n: int) -> bool:
    """
    Returns True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    # Check divisibility from 2 to sqrt(n)
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))


# 2. digit_sum(k)
def digit_sum(k: int) -> int:
    """
    Returns the sum of digits of the number k.
    Example: 502 -> 5 + 0 + 2 = 7
    """
    return sum(map(int, str(abs(k))))  # Using map to convert each digit to int


# 3. powers_of_two_up_to_n(n)
def powers_of_two_up_to_n(n: int) -> list:
    """
    Returns all powers of 2 (2**k) less than or equal to n.
    """
    result = []
    power = 2
    while power <= n:
        result.append(power)
        power *= 2
    return result


# Dictionary for Telegram Bot Access
TASKS = {
    "is_prime": is_prime,
    "digit_sum": digit_sum,
    "powers_of_two_up_to_n": powers_of_two_up_to_n
}
