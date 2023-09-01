import random


def simple_list():
    """
    Generate and return a list of dictionaries simulating person data.
    Each dictionary contains the keys 'id' and 'age', where 'id' is a
    number from 1 to 10, and 'age' is a random number between 1 and 100.
    Returns:
        list: A list of dictionaries with simulated person information.
    """
    return [{"id": i, "age": random.randint(1, 100)} for i in range(1, 11)]


def sort_list(dicts):
    """
    Sort a list of dictionaries by the 'age' key.
    Args:
        dicts (list): A list of dictionaries with person information.
    Returns:
        list: The list of dictionaries sorted by the 'age' key.
    """
    return sorted(dicts, key=lambda x: x.get("age"))
