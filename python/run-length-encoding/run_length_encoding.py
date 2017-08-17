import collections

def decode(toDecode):
    pass


def encode(toEncode):
    encodedL = []
    encodedS = ""
    dict = {}

    # What I want to do:
    # Count a sequence of letters within a string up until a different
    # string occurs
    for i in toEncode:


    count = collections.Counter(toEncode)

    for item in count:
        encodedL.append(count[item])
        encodedL.append(item)

    encodedS = ''.join(str(x) for x in encodedL)

    return encodedS

print(encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"))
# print(decode("12WB12W3B24WB"))
