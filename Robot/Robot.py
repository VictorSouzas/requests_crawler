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

    def extract_data(self, data, pattern):
        processed_data = []
        for i in data.xpath(pattern):
            processed_data.append(i.text_content().strip())
        return processed_data

    def extract_tag(self, data, pattern, tag):
        return_data = []
        for x in data:
            content = html.fromstring(x)
            for y in content.xpath(pattern):
                return_data.extend(y.xpath(tag))
        return return_data

    def extract_text(self, data, pattern, limit=1):
        group_data = []
        return_data = []
        for i, x in enumerate(data):
            if 0 == i % limit and i != 0:
                return_data.append(group_data)
                group_data = []
            content = html.fromstring(x)
            for y in content.xpath(pattern):
                group_data.append(y.text_content())
        if len(group_data) != 0: return_data.append(group_data)
        return return_data
