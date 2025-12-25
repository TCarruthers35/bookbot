# Importing the function from stats module
import sys
from stats import get_num_words, get_chars_counts, sort_chars_counts


def get_book_text(file_path):
    """
    Reads the content of a text file and returns it as a string.

    Args:
        file_path (str): The path to the text file.
    Returns:
        str: The content of the text file.
    """
    with open(file_path) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    num_words = get_num_words(text)
    char_counts = get_chars_counts(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sort_chars_counts(char_counts):
        if entry["char"].isalpha():
            char = entry["char"]
            count = entry["num"]
            print(f"{char}: {count}")
    print("============= END ===============")


main()
