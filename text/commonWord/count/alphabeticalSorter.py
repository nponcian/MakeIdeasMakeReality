from text.commonWord.count import wordCountSorter

class AlphabeticalSorter(wordCountSorter.WordCountSorter):
    @classmethod
    def name(cls):
        return "AlphabeticalSorter"

    def __init__(self, orderType):
        super().__init__(orderType)

    def sort(self, wordCountDictList):
        dictKeySorter = lambda wordCountDict : list(wordCountDict.keys())[0]
        wordCountDictList.sort(key =  dictKeySorter)
        return wordCountDictList
