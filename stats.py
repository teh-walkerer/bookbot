def count_words(text):
    words = text.split()
    # Split the text into words using whitespace as the delimiter
    # and return the number of words
    return len(words)
def count_characters(text):
    # Count the number of characters in the text
    # and return a dictionary with the character as the key
    # and the count as the value
    alphabet_specialcharacters = "abcdefghijklmnopqrstuvwxyzàáâãäåæçðèéêëìíîïñòóôõöøœùúûüýÿßśšžźż"
    # Define the alphabet and special characters
    count_dict = {}
    for char in (text.lower()):
        if char in alphabet_specialcharacters:
            count_dict[char] = count_dict.get(char, 0) + 1   
    return count_dict

def sort_on(dict):
    # Sort the dictionary by the value of "num" in descending order
    return dict["num"]
def sort_count_dict_list_by_value(char_dict):
    list_of_dicts = []
    # Convert the dictionary to a list of dictionaries
    # Each dictionary in the list will contain the character and its count
    # Iterate through the dictionary and create a list of dictionaries
    for char, count in char_dict.items():
        char_info = {"char": char, "num": count}
        list_of_dicts.append(char_info)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts


