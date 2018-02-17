# -*- coding: utf-8 -*-

from lxml import html


class Htmlhandler:

    def split_data(self, content, pattern):
        table = []
        for i, x in enumerate(content.xpath(pattern)):
            table.append(html.tostring(x))
        return table

    def split_count(self, data, limit=0, i=0, grouped_data=[], group_data=[]):
        if len(data) == 0:
            return grouped_data
        if limit == i:
            grouped_data.append(group_data)
            return self.split_count(data, limit, 0, grouped_data, [])
        group_data.append(data[0])
        del data[0]
        return self.split_count(data, limit, i + 1, grouped_data, group_data)

    def extract_data(self, data, pattern):
        processed_data = []
        for i in data.xpath(pattern):
            processed_data.append(i.text_content())
        return processed_data
