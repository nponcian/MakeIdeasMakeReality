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
        return self.orderType in self.getOrderTypes().values()

    def sort(self, wordCountDictList):
        pass

    def run(self, wordCountDict):
        wordCountDictList = [{key : value} for key, value in wordCountDict.items()]
        return self.performRun(wordCountDictList)

    def performRun(self, wordCountDictList):
        if self.isSortRequired():
            wordCountDictList = self.sort(wordCountDictList)

        if self.nextSorter is not None:
            return self.nextSorter.performRun(wordCountDictList)

        return wordCountDictList