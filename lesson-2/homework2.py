import random
import string

# 1. Age Calculator
def age_calculator(name: str, year_of_birth: int) -> str:
    age = 2025 - year_of_birth
    return f"{name}, your age is {age}."


# 2. Extract Car Name (Mercedes)
def extract_car_1(txt: str) -> str:
    return txt[1::2]


# 3. Extract Car Name (Mazda)
def extract_car_2(txt: str) -> str:
    return txt[0::2]


# 4. Extract Residence Area
def extract_area(txt: str) -> str:
    return txt.split("from")[1].strip()


# 5. Reverse String
def reverse_string(s: str) -> str:
    return s[::-1]


# 6. Count Vowels
def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)


# 7. Find Maximum Value
def find_max(nums: list) -> int:
    return max(nums)


# 8. Check Palindrome
def is_palindrome(word: str) -> bool:
    return word.lower() == word.lower()[::-1]


# 9. Extract Email Domain
def extract_domain(email: str) -> str:
    return email.split("@")[1]


# 10. Generate Random Password
def generate_password(length: int = 12) -> str:
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))


# Dictionary for Telegram bot
TASKS = {
    1: age_calculator,
    2: extract_car_1,
    3: extract_car_2,
    4: extract_area,
    5: reverse_string,
    6: count_vowels,
    7: find_max,
    8: is_palindrome,
    9: extract_domain,
    10: generate_password
}
