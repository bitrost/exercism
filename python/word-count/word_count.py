import re

def word_count(phrase):

    # Remove punctuation, make phrase lower case
    phrase = re.sub("[^a-zA-Z\s0-9]"," ",phrase).lower()
    phrase = phrase.replace("\t", " ").replace("\n", " ")
    
    # Split phrase into list
    phrase = phrase.split(" ")
    # Remove empty strings
    phrase = [i for i in phrase if i != '']

    # Count word frequency, then create a dictionary of words and frequencies
    frequencies = [phrase.count(p) for p in phrase]

    return dict(zip(phrase, frequencies))
