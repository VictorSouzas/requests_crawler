# -*- coding: utf-8 -*-

from Robot.Robot import Robot
from lxml import html


class VultrRobot(Robot):

    def __init__(self):
        Robot.__init__(self, "https://www.vultr.com/pricing/")

    def parse(self):
        content = self.content.text
        pattern = '//div[@class="container"]//div[@class="packages"]//div[@class="col-sm-3 col-xs-6"]'
        content = self.split_data(html.fromstring(content), pattern)
        labels = {"storage": self.extract_text(content, '//h3')}
        labels["hourly-price"] = self.extract_tag(content, '//span[@class="package-price"]', '@data-hourly')
        labels["monthly-price"] = self.extract_tag(content, '//span[@class="package-price"]', '@data-monthly')
        labels["processor"] = cpu = []
        labels["memory"] = memory = []
        labels["bandwidth"] = bandwidth = []
        li = self.extract_text(content, "//ul//li")
        for x in li:
            cpu.append(x[0])
            memory.append(x[1])
            bandwidth.append(x[2])
        return labels



if __name__ == '__main__':
    vultr = VultrRobot()
    vultr.parse()
