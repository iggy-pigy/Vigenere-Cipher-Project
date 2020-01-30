import string
open_text = input("Enter open text: ")
key_phrase = input("Enter key phrase: ")


if len(open_text) != len(key_phrase):
    if len(open_text) > len(key_phrase):
        key_phrase = (int(len(open_text)/len(key_phrase)))*key_phrase
    else:
        open_text = (int(len(key_phrase)/len(open_text)))*open_text


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


print(encrypt(open_text, key_phrase))
