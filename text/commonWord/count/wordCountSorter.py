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

    def sort(self, wordCountDict):
        pass

    def run(self, wordCountDict):
        if self.isSortRequired():
            wordCountDict = self.sort(wordCountDict)

        if self.nextSorter is not None:
            return self.nextSorter.run(wordCountDict)

        return wordCountDict
