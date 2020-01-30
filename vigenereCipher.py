import string
open_text = input("Enter open text: ")
key_phrase = input("Enter key phrase: ")


def to_numbers(word):
    return ([string.ascii_lowercase.index(char) for char in word])
