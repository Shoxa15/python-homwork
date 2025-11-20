# 1. Leap Year Check
def is_leap(year: int) -> bool:
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# 2. Conditional Statements Exercise
def weird_or_not(n: int) -> str:
    """
    Determines output based on integer n according to rules:
    - If n is odd, return "Weird"
    - If n is even and 2 <= n <= 5, return "Not Weird"
    - If n is even and 6 <= n <= 20, return "Weird"
    - If n is even and n > 20, return "Not Weird"
    """
    if n % 2 == 1:
        return "Weird"
    elif 2 <= n <= 5:
        return "Not Weird"
    elif 6 <= n <= 20:
        return "Weird"
    else:
        return "Not Weird"


# 3. Find Even Numbers Between a and b (inclusive)

# Solution 1: Using if-else
def even_numbers_if_else(a: int, b: int) -> list:
    """
    Returns a list of even numbers between a and b inclusive using if-else logic.
    """
    result = []
    start = a if a % 2 == 0 else a + 1
    if start > b:
        return []
    result = list(range(start, b+1, 2))
    return result


# Solution 2: Without using if-else (using arithmetic)
def even_numbers_no_if(a: int, b: int) -> list:
    """
    Returns a list of even numbers between a and b inclusive without using if-else.
    """
    start = a + (a % 2)
    return list(range(start, b+1, 2))


# Dictionary for Telegram Bot Access
TASKS = {
    "is_leap": is_leap,
    "weird_or_not": weird_or_not,
    "even_numbers_if_else": even_numbers_if_else,
    "even_numbers_no_if": even_numbers_no_if
}
