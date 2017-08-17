def to_rna(dnaStrand):
    rnaStrand = ""

    for nuc in dnaStrand:
        if (nuc == "G"):
            rnaStrand = rnaStrand+"C"
        elif (nuc == "C"):
            rnaStrand = rnaStrand+"G"
        elif (nuc == "T"):
            rnaStrand = rnaStrand+"A"
        elif (nuc == "A"):
            rnaStrand = rnaStrand+"U"

    if(len(rnaStrand) != len(dnaStrand)):
        rnaStrand = ""
        print("Invalid DNA strand input.")

    return rnaStrand
