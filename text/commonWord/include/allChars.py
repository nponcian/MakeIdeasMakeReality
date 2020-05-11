from text.commonWord.include import includerStrategy

class AllChars(includerStrategy.IncluderStrategy):
    def __init__(self):
        super().__init__()

    def reconstruct(self, text):
        return text.casefold()
