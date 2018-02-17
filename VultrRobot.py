# -*- coding: utf-8 -*-

from Robot import Robot
from lxml import html


class VultrRobot(Robot):

    def __init__(self):
        Robot.__init__(self, "https://www.vultr.com/pricing/")

    def extract_text(self, data, pattern):
        return_data = []
        for x in data:
            content = html.fromstring(x)
            for y in content.xpath(pattern):
                return_data.append(y.text_content())
        return return_data

    def extract_tag(self, data, pattern, tag):
        return_data = []
        for x in data:
            content = html.fromstring(x)
            for y in content.xpath(pattern):
                return_data.extend(y.xpath(tag))
        return return_data


    def split_data(self, content, pattern):
        table = []
        for i, x in enumerate(content.xpath(pattern)):
            table.append(html.tostring(x))
        return table

    def parse(self):
        content = self.content.text
        pattern = '//div[@class="container"]//div[@class="packages"]//div[@class="col-sm-3 col-xs-6"]'
        content = self.split_data(html.fromstring(content), pattern)
        labels = {"storage": self.extract_text(content, '//h3')}
        labels["hourly-price"] = self.extract_tag(content, '//span[@class="package-price"]', '@data-hourly')
        labels["monthly-price"] = self.extract_tag(content, '//span[@class="package-price"]', '@data-monthly')
        ul = self.extract_text(content, "//ul")
        li = self.extract_text(content, "//ul//li")
        limit = len(li) / len(ul)


if __name__ == '__main__':
    vultr = VultrRobot()
    vultr.parse()
