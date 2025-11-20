# ===============================

# 1. Create and Access List Elements
def get_third_fruit(fruits: list) -> str:
    return fruits[2]


# 2. Concatenate Two Lists
def concat_lists(a: list, b: list) -> list:
    return a + b


# 3. Extract Elements from a List
def extract_first_middle_last(nums: list) -> list:
    mid = len(nums) // 2
    return [nums[0], nums[mid], nums[-1]]


# 4. Convert List to Tuple
def list_to_tuple(items: list) -> tuple:
    return tuple(items)


# 5. Check Element in a List
def check_paris(cities: list) -> bool:
    return "Paris" in cities


# 6. Duplicate a List Without Loops
def duplicate_list(nums: list) -> list:
    return nums * 2


# 7. Swap First and Last Elements
def swap_first_last(nums: list) -> list:
    nums[0], nums[-1] = nums[-1], nums[0]
    return nums


# 8. Slice a Tuple
def slice_tuple(t: tuple) -> tuple:
    return t[3:8]


# 9. Count Occurrences in a List
def count_blue(colors: list) -> int:
    return colors.count("blue")


# 10. Find Index of Element in Tuple
def index_of_lion(animals: tuple) -> int:
    return animals.index("lion")


# 11. Merge Two Tuples
def merge_tuples(a: tuple, b: tuple) -> tuple:
    return a + b


# 12. Find the Length of List and Tuple
def lengths(a_list: list, a_tuple: tuple) -> tuple:
    return len(a_list), len(a_tuple)


# 13. Convert Tuple to List
def tuple_to_list(t: tuple) -> list:
    return list(t)


# 14. Find Maximum and Minimum in a Tuple
def max_min_tuple(t: tuple) -> tuple:
    return max(t), min(t)


# 15. Reverse a Tuple
def reverse_tuple(t: tuple) -> tuple:
    return t[::-1]


# Dictionary for Telegram Bot Easy Access
TASKS = {
    1: get_third_fruit,
    2: concat_lists,
    3: extract_first_middle_last,
    4: list_to_tuple,
    5: check_paris,
    6: duplicate_list,
    7: swap_first_last,
    8: slice_tuple,
    9: count_blue,
    10: index_of_lion,
    11: merge_tuples,
    12: lengths,
    13: tuple_to_list,
    14: max_min_tuple,
    15: reverse_tuple
}
