def get_num_words(text):
    """
    Counts the number of words in a given text.

    Args:
        text (str): The input text.
    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)


def get_chars_counts(text):
    """
    Counts the occurrences of each character in the given text. Returns a list of dictionaries with character counts.
    Args:
        text (str): The input text.
    Returns:
        list: A list of dictionaries with character counts. Format: [{"char": char, "num": count}, ...]
    """
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    formatted_counts = []
    for char in char_counts:
        formatted_counts.append({"char": char, "num": char_counts[char]})
    return formatted_counts


def sort_on(items):
    """
    A helper function to sort character count dictionaries based on the count.
    Args:
        items (dict): A dictionary with character count.
    Returns:
        int: The count of the character.
    """
    return items["num"]


def sort_chars_counts(char_counts):
    """
    Sorts a list of character count dictionaries in descending order based on the count.
    Args:
        char_counts (list): A list of dictionaries with character counts.
    Returns:
        list: The sorted list of dictionaries with character counts.
    """
    sorted_counts = char_counts.sort(key=sort_on, reverse=True)
    return char_counts
