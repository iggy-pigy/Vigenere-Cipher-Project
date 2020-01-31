import string
import re


def check_format_of_input(input_value):
    while not re.match("^[a-z]*$", input_value):
        input_value = input("Oops! That was not a valid string. Try again... ")


original_text = input("Please enter original text: ")
key_word = input("Please enter key word: ")


if len(original_text) != len(key_word):
    if len(original_text) > len(key_word):
        key_word = (int(len(original_text)/len(key_word)))*key_word
    else:
        original_text = (int(len(key_word)/len(original_text)))*original_text


def to_numbers(word):
    return ([string.ascii_lowercase.index(char) for char in word])


def encrypt(word1, word2):
    sums = [a + b for a, b in zip(to_numbers(word1), to_numbers(word2))]
    new_sums = []
    for value in sums:
        if value > 25:
            value = value-26
            new_sums.append(value)
        else:
            new_sums.append(value)

    return ''.join([string.ascii_lowercase[index] for index in new_sums])


print(encrypt(original_text, key_word))
