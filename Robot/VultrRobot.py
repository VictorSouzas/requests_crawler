# -*- coding: utf-8 -*-

from Robot.Robot import Robot
from lxml import html
import numpy as np


class VultrRobot(Robot):

    def __init__(self):
        Robot.__init__(self, "https://www.vultr.com/pricing/")

    def normalize_data(self, data):
        return_data = []
        for i, x in enumerate(data):
            if i == 0:
                for y in x:
                    return_data.append([y])
                continue
            for j, y in enumerate(x):
                return_data[j].append(y)
        return return_data



    def parse(self):
        content = self.content.text
        pattern = '//div[@class="container"]//div[@class="packages"]//div[@class="col-sm-3 col-xs-6"]'
        content = self.split_data(html.fromstring(content), pattern)
        cpu = []
        memory = []
        bandwidth = []
        li = self.extract_text(content, "//ul//li")
        for x in li:
            cpu.append(x[0])
            memory.append(x[1])
            bandwidth.append(x[2])
        labels = [cpu]
        labels.append(memory)
        labels.append(self.extract_text(content, '//h3'))
        labels.append(bandwidth)
        labels.append(self.extract_tag(content, '//span[@class="package-price"]', '@data-monthly'))
        labels.append(self.extract_tag(content, '//span[@class="package-price"]', '@data-hourly'))
        labels = self.normalize_data(labels)
        return labels



if __name__ == '__main__':
    vultr = VultrRobot()
    vultr.parse()
