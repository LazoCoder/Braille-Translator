# Braille-Translator
Translating text to Grade 2 Braille is a non-trivial task since it is not just a variant of the alphabet, it is an independent writing system. Iterating over a string and translating it one character at a time will not yield correct results for Grade 2 Braille. Many braille symbols have multiple meanings and this can lead to ambiguities. Furthermore, certain words and letters that are commonly seen in the English language can be represented by fewer braille symbols than there are letters (these are called contractions). The algorithm used in this software is summarized below.

## Sample
The following is the above introduction translated to braille:

⠠⠞⠗⠁⠝⠎⠇⠁⠞⠊⠝⠛ ⠞⠑⠭⠞ ⠖ ⠠⠛⠗⠁⠙⠑ ⠼⠃ ⠠⠃⠗⠁⠊⠇⠇⠑ ⠊⠎ ⠁ ⠝⠕⠝⠤⠞⠗⠊⠧⠊⠁⠇ ⠞⠁⠎⠅ ⠎⠊⠝⠉⠑ ⠭ ⠊⠎ ⠝ ⠚ ⠁ ⠧⠁⠗⠊⠁⠝⠞ ⠷ ⠮ ⠁⠇⠏⠓⠁⠃⠑⠞⠂ ⠭ ⠊⠎ ⠁⠝ ⠊⠝⠙⠑⠏⠑⠝⠙⠑⠝⠞ ⠺⠗⠊⠞⠊⠝⠛ ⠎⠽⠎⠞⠑⠍⠲ ⠠⠊⠞⠑⠗⠁⠞⠊⠝⠛ ⠕⠧⠑⠗ ⠁ ⠎⠞⠗⠊⠝⠛ ⠯ ⠞⠗⠁⠝⠎⠇⠁⠞⠊⠝⠛ ⠭ ⠕⠝⠑ ⠉⠓⠁⠗⠁⠉⠞⠑⠗ ⠁⠞ ⠁ ⠞⠊⠍⠑ ⠺ ⠝ ⠽⠊⠑⠇⠙ ⠉⠕⠗⠗⠑⠉⠞ ⠗⠑⠎⠥⠇⠞⠎ ⠿ ⠠⠛⠗⠁⠙⠑ ⠼⠃ ⠠⠃⠗⠁⠊⠇⠇⠑⠲ ⠠⠍⠁⠝⠽ ⠃⠗⠁⠊⠇⠇⠑ ⠎⠽⠍⠃⠕⠇⠎ ⠓ ⠍⠥⠇⠞⠊⠏⠇⠑ ⠍⠑⠁⠝⠊⠝⠛⠎ ⠯ ⠞⠓⠊⠎ ⠉ ⠇⠑⠁⠙ ⠖ ⠁⠍⠃⠊⠛⠥⠊⠞⠊⠑⠎⠲ ⠠⠋⠥⠗⠞⠓⠑⠗⠍⠕⠗⠑⠂ ⠉⠑⠗⠞⠁⠊⠝ ⠺⠕⠗⠙⠎ ⠯ ⠇⠑⠞⠞⠑⠗⠎ ⠞ ⠁⠗⠑ ⠉⠕⠍⠍⠕⠝⠇⠽ ⠎⠑⠑⠝ ⠔ ⠮ ⠠⠑⠝⠛⠇⠊⠎⠓ ⠇⠁⠝⠛⠥⠁⠛⠑ ⠉ ⠃⠑ ⠗⠑⠏⠗⠑⠎⠑⠝⠞⠑⠙ ⠃⠽ ⠋⠑⠺⠑⠗ ⠃⠗⠁⠊⠇⠇⠑ ⠎⠽⠍⠃⠕⠇⠎ ⠞⠓⠁⠝ ⠞⠓⠑⠗⠑ ⠁⠗⠑ ⠇⠑⠞⠞⠑⠗⠎ ⠶⠞⠓⠑⠎⠑ ⠁⠗⠑ ⠉⠁⠇⠇⠑⠙ ⠉⠕⠝⠞⠗⠁⠉⠞⠊⠕⠝⠎⠶⠲ ⠠⠮ ⠁⠇⠛⠕⠗⠊⠞⠓⠍ ⠥⠎⠑⠙ ⠔ ⠞⠓⠊⠎ ⠎⠕⠋⠞⠺⠁⠗⠑ ⠊⠎ ⠎⠥⠍⠍⠁⠗⠊⠵⠑⠙ ⠃⠑⠇⠕⠺⠲

## Usage
```

Usage:
    Usage:
        main.py <parameter>
        main.py <file name> <parameter>
    Parameters:
        -braille | --b      translate braille to text
        -text    | --t      translate text to braille
        -help    | --h      display this screen
        -map     | --m      print translation map

```

## The Algorithm for Translating Alphabet Based Text to Grade 2 Braille:
1. Split up the text into words by dividing them based on whitespace characters.
    - Whitespace includes spaces (' ') and new lines ('\n')
2. For each word, handle the numbers first.
    - Numbers in braille use the same symbols as the first 10 letters of the alphabet.
        - The number '7' and the letter 'g' are both represented by '⠛'.
        - To differentiate between numbers and letters, an escape code (⠼) is placed before groups of numbers.
        - Therefore '7' is actually '⠼⠛' whereas 'g' is only '⠛'.
    - In this step, only the numbers are dealt with, so there will be a mix of both braille and Alphabet symbols.
        - Example: "123-456-JUNK" becomes "⠼⠁⠃⠉-⠼⠙⠑⠋-JUNK"
3. Handle the capitals.
    - Similarly to numbers in braille, capital letters need an escape code (⠠).
    - The escape code (⠠) is added to the beginning of each capital letter and the letter is changed to lowercase.
        - Example 1: "⠼⠁⠃⠉-⠼⠙⠑⠋-JUNK" becomes "⠼⠁⠃⠉-⠼⠙⠑⠋-⠠j⠠u⠠n⠠k". The dashes still remain.
        - Example 2: "Sweet" becomes "⠠sweet". The non-capital letters remain untouched.
4. Trim the word.
    - Sometimes the words extracted contain punctuation attached to them such as commas or brackets.
    - Words need to be trimmed so that they can be converted to contractions.
        - Example: The word "the" is represented by a single braille symbol (⠮).
        - If the word "the" has punctuation around it ("the!") then it will not be interpreted correctly.
        - This is also why capitals are converted to lowercase in step 3 because "The" would not work either.
    - The characters that are trimmed off are called "shavings".
        - Example: In the word "!where?", the shavings are "!?" and the trimmed word is "where".
5. Build the translation.
    1. Check to see if the trimmed word can be contracted.
        - This includes common words like "the", "in", "you" etc...
    2. Translate the remaining characters that are still alphabetic.
    3. Translate the shavings (this will mostly just be punctuation).
        - Exceptions to be mindful of:
            - There is no braille symbol for a generic quote (")
            - There is only open quotation (“) and closed quotation (”).
            - Therefore we must keep track of what the last quotation was to translate it correctly.

## Disclaimer
Creating a perfect braille translation can only be done by a human as it requires an understanding of the content at hand. Also, many braille contractions follow pronunciation so programming this can be quite tricky. For instance, the “th” contraction that is used in “thought” would not be used in “pothole”.

This Braille Translator does not include partial contractions as this would increase the complexity of the code ten-fold. This software is meant to provide a rough translation and was written as a means for me to learn Python. Anyone who wants to produce quality braille to meet contract standards should consider consulting an expert instead.
