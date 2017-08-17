def distance(strandOne, strandTwo):
    count = 0

    if (len(strandOne) != len(strandTwo)):
        raise ValueError("Strands are not of equal length.")

    for i in range(len(strandOne)):
        if (strandOne[i] != strandTwo[i]):
            count += 1

    return count
