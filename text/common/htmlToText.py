from html.parser import HTMLParser
import requests

class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []

    def handle_data(self, d):
        self.result.append(d)

    def get_text(self):
        return ''.join(self.result)

def htmlContentsToText(htmlContents):
    s = HTMLTextExtractor()
    s.feed(htmlContents)
    return s.get_text()

def htmlUrlsToText(*htmlUrls):
    mergedContent = str()
    for url in htmlUrls:
        url = url.strip()
        if len(url) == 0: continue

        response = requests.get(url)
        htmlContents = response.content
        if isinstance(htmlContents, (bytes, bytearray)):
            htmlContents = htmlContents.decode()
        mergedContent += htmlContentsToText(htmlContents) + "\n"

    return mergedContent
