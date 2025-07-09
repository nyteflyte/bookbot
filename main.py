from stats import count_words
from stats import count_chars
from stats import convert_to_list    
from stats import sort_on

book_path = "books/frankenstein.txt"

def get_book_text():
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def print_pretty(book_path,book_length,ordered_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {book_length} total words")
    print("--------- Character Count -------")
    for i in ordered_chars:
        char = i['char']
        num = i['num']
        print (f"{char}: {num}")


def main():
    book_text = get_book_text()
    book_length = count_words(book_text)
    char_count = count_chars(book_text)
    char_list = convert_to_list(char_count)
    ordered_chars = [char_list]
    ordered_chars.sort(reverse=True, key=sort_on)
    ordered_chars = ordered_chars[0]
    print_pretty(book_path,book_length,ordered_chars)
main()
