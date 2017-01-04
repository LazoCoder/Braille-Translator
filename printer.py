# Tool for printing standard letters and numbers and their respective braille representations.

import mapAlphaToBraille


def uppercase_alphabet_utf_codes():
    # Print capital alphabet based letters and their respective UTF codes.
    print("UTF Codes for Capital Letters:")
    for i in range(65, 91):
        print(chr(i), i, end='    ')
        if i % 8 == 0:
            print()
    print()


def lowercase_alphabet_utf_codes():
    # Print alphabet based letters and their respective UTF codes.
    print("UTF Codes for Letters:")
    for i in range(97, 123):
        print("%c %3d" % (chr(i), i), end='   ')
        if i % 8 == 0:
            print()
    print()


def braille_utf_codes():
    # Print all 64 braille combinations and their respective UTF codes.
    print("UTF Codes for Braille Symbols:")
    for i in range(10240, 10304):
        print(chr(i), i, end='  ')
        if (i+1) % 8 == 0:
            print()


def alphabet():
    # Print the English alphabet with their respective Braille representations.
    print("Letters:")
    for i in range(97, 123):
        print(chr(i), mapAlphaToBraille.letters.get(chr(i)), end='   ')
        if i % 8 == 0:
            print()
    print()


def contractions():
    # Print Braille symbols that represent whole words.
    print("Contraction:")
    count = 0
    word_list = []
    for word in mapAlphaToBraille.contractions:
        word_list.append(word)
    word_list.sort()
    for word in word_list:
        formatted = '{:<10}'.format(word)
        print("%c %10s" % (mapAlphaToBraille.contractions.get(word), formatted), end="")
        count += 1
        if count % 5 == 0:
            print()
    print()


def numbers():
    # Print numbers in Braille and in standard notation.
    print("Numbers (must proceed after the ⠼ escape code):")
    count = 0
    num_list = []  # Punctuation list.
    for num in mapAlphaToBraille.numbers:
        num_list.append(num)
    num_list.sort()
    for num in num_list:
        print(num, mapAlphaToBraille.numbers.get(num), end="        ")
        count += 1
        if count % 5 == 0:
            print()


def punctuation():
    # Print Braille symbols for punctuation.
    print("Punctuation:")
    count = 0
    pun_list = []  # Punctuation list.
    for pun in mapAlphaToBraille.punctuation:
        pun_list.append(pun)
    pun_list.sort()
    for pun in pun_list:
        print(pun, mapAlphaToBraille.punctuation.get(pun), end="        ")
        count += 1
        if count % 5 == 0:
            print()
    print()


def all_utf_codes():
    # Print the UTF codes for both lowercase and uppercase letters and for Braille symbols.
    lowercase_alphabet_utf_codes()
    print()
    uppercase_alphabet_utf_codes()
    print()
    braille_utf_codes()


def all_braille():
    # Print all the Braille symbols and their standard alphabet based representations.
    alphabet()
    print()
    contractions()
    print()
    punctuation()
    print()
    numbers()
    print()
