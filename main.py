import sys
from stats import count_words
from stats import count_chars
from stats import convert_to_list    
#from stats import sort_on

try:
    book_path = sys.argv[1]
except Exception:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
#book_path = "books/frankenstein.txt"

def get_book_text():
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def sort_on(item):
    return item["num"]

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
    char_list.sort(reverse=True, key=sort_on)
    #ordered_chars = ordered_chars[0]
    print_pretty(book_path,book_length,char_list)
main()
