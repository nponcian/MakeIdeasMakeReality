from text.commonWord.count import wordCountSorter

class CountSorter(wordCountSorter.WordCountSorter):
    @classmethod
    def name(cls):
        return "CountSorter"

    def __init__(self, orderType):
        super().__init__(orderType)
        self.targetOrderTypes =\
            [
                self.getOrderTypes()["INC"],
                self.getOrderTypes()["DEC"],
            ]

    def isSortRequired(self):
        return self.orderType in self.targetOrderTypes

    def sort(self, wordCountDictList):
        dictValueSorter = lambda wordCountDict : list(wordCountDict.values())[0]
        shouldReverse = self.orderType == self.targetOrderTypes[1]

        wordCountDictList.sort(key =  dictValueSorter, reverse = shouldReverse)
        return wordCountDictList
