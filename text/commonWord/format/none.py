from text.commonWord.format import textFormatter

class NoneFormatter(textFormatter.TextFormatterStrategy):
    def __init__(self):
        super().__init__()

    def reconstruct(self, text):
        return text.casefold()
