
# 1. Sort a Dictionary by Value
def sort_dict(d: dict, reverse: bool = False) -> dict:
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))


# 2. Add a Key to a Dictionary
def add_key(d: dict, key, value) -> dict:
    d[key] = value
    return d


# 3. Concatenate Multiple Dictionaries
def concat_dicts(*dicts) -> dict:
    result = {}
    for d in dicts:
        result.update(d)
    return result


# 4. Generate a Dictionary with Squares (1 to n)
def squares_dict(n: int) -> dict:
    return {i: i*i for i in range(1, n+1)}


# 5. Dictionary of Squares from 1 to 15
def squares_dict_1_15() -> dict:
    return {i: i*i for i in range(1, 16)}


# -------------------------------
# Set Exercises
# -------------------------------

# 1. Create a Set
def create_set(items: list) -> set:
    return set(items)


# 2. Iterate Over a Set
def iterate_set(s: set) -> list:
    return [item for item in s]


# 3. Add Member(s) to a Set
def add_members(s: set, *members) -> set:
    s.update(members)
    return s


# 4. Remove Item(s) from a Set
def remove_items(s: set, *items) -> set:
    for item in items:
        s.discard(item)
    return s


# 5. Remove an Item if Present in the Set
def remove_if_present(s: set, item) -> set:
    s.discard(item)
    return s


# Dictionary for Telegram Bot Access
TASKS = {
    # Dictionary tasks
    "dict_sort": sort_dict,
    "dict_add_key": add_key,
    "dict_concat": concat_dicts,
    "dict_squares_n": squares_dict,
    "dict_squares_1_15": squares_dict_1_15,
    # Set tasks
    "set_create": create_set,
    "set_iterate": iterate_set,
    "set_add_members": add_members,
    "set_remove_items": remove_items,
    "set_remove_if_present": remove_if_present
}
