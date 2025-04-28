def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
from stats import count_words
from stats import count_characters
def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = count_words(book_text)
    count_of_each_character = count_characters(book_text)
    print(f"{word_count} words found in the document")
    print(count_of_each_character)
main()    
