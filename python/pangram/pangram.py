import re

def is_pangram(sentence):
    lettersUsed = []

    sentence = sentence.lower()
    # Remove non-alphabetic characters
    sentence = re.sub("[^a-z]","",sentence)

    for letter in sentence:
        if (letter not in lettersUsed):
            lettersUsed.append(letter)

    if (len(lettersUsed) == 26):
        return True
    else:
        return False
