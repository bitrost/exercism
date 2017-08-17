def is_isogram(words):
    characterList = []
    words = words.lower()
    words = words.replace(" ","").replace("-","")

    for character in words:
        if (character not in characterList):
            characterList.append(character)
        else:
            return False
    return True
