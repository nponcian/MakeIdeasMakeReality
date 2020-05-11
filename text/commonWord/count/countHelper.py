from collections import Counter
from django.contrib.staticfiles.storage import staticfiles_storage

from text.commonWord.count import sorterChain

def count(words):
    # return {k : v for k, v in Counter(words).most_common()}
    return Counter(words)

def order(wordsAndCountDict, orderType):
    sorters = sorterChain.buildSortersChain(orderType)
    return sorters.run(wordsAndCountDict)

def ignore(wordsAndCountDict, ignoreList):
    DEFAULT = "__DEFAULT__"
    PATH_TO_IGNORE_FILE = 'text/assets/txt/commonWords.txt'

    for wordToIgnore in set(ignoreList):
        if wordToIgnore == DEFAULT:
            # staticfiles_storage.url('txt/file.txt') # staticfiles_storage.path('txt/file.txt')
            toIgnoreFile = staticfiles_storage.open(PATH_TO_IGNORE_FILE)
            for defaultIgnore in toIgnoreFile.readlines():
                if isinstance(defaultIgnore, (bytes, bytearray)):
                    defaultIgnore = defaultIgnore.decode()

                defaultIgnore = defaultIgnore.strip()
                wordsAndCountDict.pop(defaultIgnore, None)
        else:
            wordsAndCountDict.pop(wordToIgnore, None)

    return wordsAndCountDict
