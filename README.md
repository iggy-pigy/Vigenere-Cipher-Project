# Vigenère Cipher

## Description

Is a method of encrypting alphabetic text. In reality the encryption of the original text is done using the _Vigenère square_ or _Vigenère table_ where this program use math method to figure out encrypted text.

To encrypt text the user should type in original text and key word. Each letter has its own value (e.g. A = 0, B =1 etc.). If we want to encrypt the word **MOPSIK**(original text) and use the key word **DOG**, then the result should be **PCVVWQ** (encrypted text).

## Getting started

To run this code you need **Python3**.

## Known issues

- At the moment the program supports original text with a character length that is divisible by the length of key e.g. `len("MOPSIK") % LEN("DOG") === 0`.
- Also both, original text and key word should be typed in without whitespace.
- Only supports text encryption NOT decryption.
