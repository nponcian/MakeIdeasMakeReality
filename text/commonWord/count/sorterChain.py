from text.commonWord.count import alphabeticalSorter
from text.commonWord.count import countSorter

def buildSortersChain(orderType):
    sorterByAlphabet = alphabeticalSorter.AlphabeticalSorter(orderType)
    sorterByCount = countSorter.CountSorter(orderType)

    sorterByAlphabet.setNextSorter(sorterByCount)

    return sorterByAlphabet
