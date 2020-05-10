from collections import Counter

from text.commonWord.count import sorterChain

def count(words):
    # return {k : v for k, v in Counter(words).most_common()}
    return Counter(words)

def order(wordCountDict, orderType):
    sorters = sorterChain.buildSortersChain(orderType)
    return sorters.run(wordCountDict)
