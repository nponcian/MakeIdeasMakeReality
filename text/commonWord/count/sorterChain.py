from text.commonWord.count import (
    alphabeticalSorter,
    countSorter,
)

def buildSortersChain(orderType):
    sorterByAlphabet = alphabeticalSorter.AlphabeticalSorter(orderType)
    sorterByCount = countSorter.CountSorter(orderType)

    sorterByAlphabet.setNextSorter(sorterByCount)

    return sorterByAlphabet
