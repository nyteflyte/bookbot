def count_words(file_contents):
    string = file_contents.split()
    num_words = len(string)
    return num_words

def count_chars(file_contents):
    char_count = {}
    lower_case = file_contents.lower()

    for character in lower_case:
        if character.isalpha():
            if character not in char_count:
                char_count[character] = 1
            else:
                char_count[character] += 1
    return char_count

def convert_to_list(char_count):
    list_of_chars = []
    for char in char_count:
        value = char_count[char]
        char_dict = {
            "char" : char,
            "num" : value
        }
        list_of_chars.append(char_dict)
    return list_of_chars

#def sort_on(char_list):
#    for i in char_list:
#        print(i)
#       return i["num"]