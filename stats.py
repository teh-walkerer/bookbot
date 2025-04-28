def count_words(text):
    words = text.split()
    return len(words)
def count_characters(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count_dict = {}
    for char in (text.lower()):
        if char in alphabet:
            count_dict[char] = count_dict.get(char, 0) + 1   
    return count_dict
