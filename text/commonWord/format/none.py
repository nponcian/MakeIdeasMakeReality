from text.commonWord.format import textFormatter

class NoneFormatter(textFormatter.TextFormatter):
    def reconstruct(self, text):
        return text
