import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
from stats import count_words
from stats import count_characters
from stats import sort_count_dict_list_by_value
# def get_book_text(file_path):
#     with open(file_path) as f:
#         return f.read()
# def count_words(text):
#     words = text.split()
#     return len(words)
# def count_characters(text):
#     alphabet_specialcharacters = "abcdefghijklmnopqrstuvwxyzàáâãäåæçðèéêëìíîïñòóôõöøœùúûüýÿßśšžźż"
#     count_dict = {}
#     for char in (text.lower()):
#         if char in alphabet_specialcharacters:
#             count_dict[char] = count_dict.get(char, 0) + 1
#     return count_dict
# def sort_count_dict_by_value(char_dict, char_dict_count):
#     char_dict = count_characters(text)
#     sorted_dict = {}
#     sorted_keys = sorted(char_dict, key=char_dict.get, reverse=True)
#     for key in sorted_keys:
#         sorted_dict[key] = char_dict[key]
#     return sorted_dict
def main():
    path = sys.argv[1]
    # path = "book.txt"
    book_text = get_book_text(path)
    # book_text = get_book_text("book.txt")
    word_count = count_words(book_text)
    count_of_each_character = count_characters(book_text)
    sorted_dict = sort_count_dict_list_by_value(count_of_each_character)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()    
