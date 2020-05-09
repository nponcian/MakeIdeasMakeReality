import re

def _stripNonAlNum(word):
    # could be simplified to "if word.isalnum(): return word" but seems to be slower
    if len(word) <= 1: return word if word.isalnum() else ""

    substr = re.search("[a-zA-Z0-9].*[a-zA-Z0-9]", word)
    return substr.group(0) if substr is not None else ""

def groupWords(text):
    words = text.split()
    nonEmptyWords = list()

    for word in words:
        strippedWord = _stripNonAlNum(word)
        if len(strippedWord) > 0:
            nonEmptyWords.append(strippedWord)
        # or using another logic via filter:
        # nonEmptyWords = list(filter(lambda word: len(word) > 0, words))

    return nonEmptyWords
