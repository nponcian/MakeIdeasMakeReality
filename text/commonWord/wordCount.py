from collections import Counter

def count(words):
    return Counter(words)
    # return {k : v for k, v in Counter(words).most_common()}

class WordCountSorter:
    @classmethod
    def name(cls):
        return "WordCountSorter"

    @staticmethod
    def getOrderTypes():
        return\
            {
                "ALPHA" : "alphabetical",
                "INC" : "increasing",
                "DEC" : "decreasing",
            }

    def __init__(self, orderType):
        self.orderType = orderType
        self.nextSorter = None

    def setNextSorter(self, nextSorterObj):
        self.nextSorter = nextSorterObj

    def isSortRequired(self):
        return self.orderType in WordCountSorter.getOrderTypes().values()

    def sort(self, wordCountDict):
        pass

    def run(self, wordCountDict):
        print(self.name(), "before run", wordCountDict)
        if self.isSortRequired():
            wordCountDict = self.sort(wordCountDict)
        print(self.name(), "after run", wordCountDict)

        if self.nextSorter is not None:
            return self.nextSorter.run(wordCountDict)

        print(self.name(), "return it ^")
        return wordCountDict

class AplhabeticalSorter(WordCountSorter):
    @classmethod
    def name(cls):
        return "AplhabeticalSorter"

    def __init__(self, orderType):
        super().__init__(orderType)

    def sort(self, wordCountDict):
        # sorted(wordCountDict.items(), key = lambda item : item[0])}
        return {key : value for key, value in sorted(wordCountDict.items())}

class CountSorter(WordCountSorter):
    @classmethod
    def name(cls):
        return "CountSorter"

    def __init__(self, orderType):
        super().__init__(orderType)
        self.targetOrderTypes =\
            [
                WordCountSorter.getOrderTypes()["INC"],
                WordCountSorter.getOrderTypes()["DEC"],
            ]

    def isSortRequired(self):
        return self.orderType in self.targetOrderTypes

    def sort(self, wordCountDict):
        keySorter = lambda item : item[1]
        shouldReverse = self.orderType == self.targetOrderTypes[1]

        return {key : value for key, value in
                sorted(wordCountDict.items(), key = keySorter, reverse = shouldReverse)}

def order(wordCountDict, orderType):
    alphabeticalSorter = AplhabeticalSorter(orderType)
    countSorter = CountSorter(orderType)

    alphabeticalSorter.setNextSorter(countSorter)

    wordCountDict = alphabeticalSorter.run(wordCountDict)
    return wordCountDict
