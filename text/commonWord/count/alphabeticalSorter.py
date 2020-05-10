from text.commonWord.count import wordCountSorter

class AlphabeticalSorter(wordCountSorter.WordCountSorter):
    @classmethod
    def name(cls):
        return "AlphabeticalSorter"

    def __init__(self, orderType):
        super().__init__(orderType)

    def sort(self, wordCountDict):
        # sorted(wordCountDict.items(), key = lambda item : item[0])} # happens by default
        return {key : value for key, value in sorted(wordCountDict.items())}
