# -*- coding: utf-8 -*-

from Robot import Robot
from lxml import html


class VultrRobot(Robot):

    def __init__(self):
        Robot.__init__(self, "https://www.vultr.com/pricing/")

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

    def extract_tag(self, data, pattern, tag):
        return_data = []
        for x in data:
            content = html.fromstring(x)
            for y in content.xpath(pattern):
                return_data.extend(y.xpath(tag))
        return return_data

    def parse(self):
        content = self.content.text
        pattern = '//div[@class="container"]//div[@class="packages"]//div[@class="col-sm-3 col-xs-6"]'
        content = self.split_data(html.fromstring(content), pattern)
        labels = {"storage": self.extract_text(content, '//h3')}
        labels["hourly-price"] = self.extract_tag(content, '//span[@class="package-price"]', '@data-hourly')
        labels["monthly-price"] = self.extract_tag(content, '//span[@class="package-price"]', '@data-monthly')
        labels["cpu"] = cpu = []
        labels["memory"] = memory = []
        labels["bandwidth"] = bandwidth = []
        li = self.extract_text(content, "//ul//li")
        for x in li:
            cpu.append(x[0])
            memory.append(x[1])
            bandwidth.append(x[2])



if __name__ == '__main__':
    vultr = VultrRobot()
    vultr.parse()
