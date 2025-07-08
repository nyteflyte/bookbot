    
def get_book_text():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents):
    string = file_contents.split()
    num_words = len(string)
    return num_words

def main():
    book_text = get_book_text()
    book_length = count_words(book_text)
    print(f"{book_length} words found in the document")

main()
