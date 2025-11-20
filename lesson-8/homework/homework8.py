# EXCEPTION HANDLING AND FILE I/O 
# ===============================

import os
import random
import string

# Exception Handling Exercises
# -------------------------------

# 1. ZeroDivisionError
def safe_divide(a: float, b: float):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"


# 2. ValueError for integer input
def check_integer(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError("Input is not a valid integer")


# 3. FileNotFoundError
def open_file_safe(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"


# 4. TypeError for numerical input
def add_two_numbers(a, b):
    try:
        return a + b
    except TypeError:
        raise TypeError("Inputs must be numbers")


# 5. PermissionError
def open_file_permission(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except PermissionError:
        return f"Error: Permission denied for file '{filename}'"


# 6. IndexError
def access_list(lst, idx):
    try:
        return lst[idx]
    except IndexError:
        return "Error: Index out of range"


# 7. KeyboardInterrupt
def input_number(prompt="Enter number: "):
    try:
        return int(input(prompt))
    except KeyboardInterrupt:
        return "Input cancelled by user"


# 8. ArithmeticError
def safe_arithmetic(a, b):
    try:
        return a / b
    except ArithmeticError:
        return "Arithmetic error occurred"


# 9. UnicodeDecodeError
def read_file_unicode(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        return f"Error: Cannot decode file '{filename}'"


# 10. AttributeError
def list_append_safe(lst, value):
    try:
        lst.append(value)
        return lst
    except AttributeError:
        return "Error: Object has no attribute 'append'"


# -------------------------------
# File Input/Output Exercises
# -------------------------------

# 1. Read entire file
def read_entire_file(filename):
    with open(filename, 'r') as f:
        return f.read()


# 2. Read first n lines
def read_first_n_lines(filename, n):
    with open(filename, 'r') as f:
        return [next(f).rstrip('\n') for _ in range(n)]


# 3. Append text to file
def append_text(filename, text):
    with open(filename, 'a') as f:
        f.write(text + '\n')
    return read_entire_file(filename)


# 4. Read last n lines
def read_last_n_lines(filename, n):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [line.rstrip('\n') for line in lines[-n:]]


# 5. Read file into list
def file_to_list(filename):
    with open(filename, 'r') as f:
        return [line.rstrip('\n') for line in f]


# 6. Read file into variable
def file_to_variable(filename):
    with open(filename, 'r') as f:
        return f.read()


# 7. Read file into array
def file_to_array(filename):
    with open(filename, 'r') as f:
        return list(f.read())


# 8. Find longest words
def longest_words(filename):
    with open(filename, 'r') as f:
        words = f.read().replace('\n',' ').split()
    max_len = max(len(w) for w in words)
    return [w for w in words if len(w) == max_len]


# 9. Count lines
def count_lines(filename):
    with open(filename, 'r') as f:
        return sum(1 for _ in f)


# 10. Word frequency
def word_frequency(filename):
    with open(filename, 'r') as f:
        words = f.read().replace('\n',' ').split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w,0)+1
    return freq


# 11. File size
def file_size(filename):
    return os.path.getsize(filename)


# 12. Write list to file
def write_list_to_file(lst, filename):
    with open(filename, 'w') as f:
        for item in lst:
            f.write(str(item) + '\n')
    return True


# 13. Copy file
def copy_file(src, dest):
    with open(src, 'r') as fsrc, open(dest, 'w') as fdest:
        fdest.write(fsrc.read())
    return True


# 14. Combine lines from two files
def combine_files_linewise(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        combined = [l1.rstrip('\n') + l2.rstrip('\n') for l1,l2 in zip(f1,f2)]
    return combined


# 15. Read random line
def random_line(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return random.choice(lines).rstrip('\n')


# 16. Check if file is closed
def is_file_closed(f):
    return f.closed


# 17. Remove newline characters
def remove_newlines(filename):
    with open(filename, 'r') as f:
        return [line.rstrip('\n') for line in f]


# 18. Count words in file
def count_words(filename):
    with open(filename, 'r') as f:
        text = f.read().replace(',', ' ')
        return len(text.split())


# 19. Extract characters into list
def extract_characters(filename):
    with open(filename, 'r') as f:
        return list(f.read())


# 20. Generate 26 text files A.txt to Z.txt
def generate_26_files(directory="."):
    for ch in string.ascii_uppercase:
        with open(os.path.join(directory, f"{ch}.txt"), 'w') as f:
            f.write('')
    return True


# 21. Create alphabet file with N letters per line
def alphabet_file(filename, n_per_line):
    with open(filename, 'w') as f:
        for i in range(0, 26, n_per_line):
            f.write(''.join(string.ascii_lowercase[i:i+n_per_line]) + '\n')
    return True


# Dictionary for Telegram Bot Access
TASKS = {
    # Exception Handling
    "safe_divide": safe_divide,
    "check_integer": check_integer,
    "open_file_safe": open_file_safe,
    "add_two_numbers": add_two_numbers,
    "open_file_permission": open_file_permission,
    "access_list": access_list,
    "input_number": input_number,
    "safe_arithmetic": safe_arithmetic,
    "read_file_unicode": read_file_unicode,
    "list_append_safe": list_append_safe,
    # File I/O
    "read_entire_file": read_entire_file,
    "read_first_n_lines": read_first_n_lines,
    "append_text": append_text,
    "read_last_n_lines": read_last_n_lines,
    "file_to_list": file_to_list,
    "file_to_variable": file_to_variable,
    "file_to_array": file_to_array,
    "longest_words": longest_words,
    "count_lines": count_lines,
    "word_frequency": word_frequency,
    "file_size": file_size,
    "write_list_to_file": write_list_to_file,
    "copy_file": copy_file,
    "combine_files_linewise": combine_files_linewise,
    "random_line": random_line,
    "is_file_closed": is_file_closed,
    "remove_newlines": remove_newlines,
    "count_words": count_words,
    "extract_characters": extract_characters,
    "generate_26_files": generate_26_files,
    "alphabet_file": alphabet_file
}
