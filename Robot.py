# -*- coding: utf-8 -*-

from lxml import html
import requests


class Robot:

    def __init__(self, url):
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"}
        self.content = requests.get(url=self.url, headers=self.headers, timeout=2.5)

    def split_data(self, content, pattern):
        table = []
        for i, x in enumerate(content.xpath(pattern)):
            table.append(html.tostring(x))
        return table
