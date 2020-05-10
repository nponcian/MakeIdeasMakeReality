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

    def sort(self, wordCountDict):
        keySorter = lambda item : item[1]
        shouldReverse = self.orderType == self.targetOrderTypes[1]

        return {key : value for key, value in
                sorted(wordCountDict.items(), key = keySorter, reverse = shouldReverse)}
