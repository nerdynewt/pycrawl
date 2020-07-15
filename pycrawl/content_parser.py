#!/bin/env python3

import re

def compress(text):
    text = re.sub(r'[^A-Za-z ]', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\r', ' ', text)
    text = re.sub(r' +', ' ', text)
    return text


class Content:
    def __init__(self, content, url):
        self.content = content
        self.url = url
        try:
            self.title = re.search('(?<=<title>).+?(?=</title>)', url.text, re.DOTALL).group().strip()
        except:
            self.title = self.url
        self.clean = compress(self.content)
        self.links = re.findall(r'href="(http.*?)"', content, re.IGNORECASE)
