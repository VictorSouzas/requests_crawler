# -*- coding: utf-8 -*-

from lxml import html
from Robot.Robot import Robot
import re


class DigitalOceanRobot(Robot):

    def __init__(self):
        Robot.__init__(self, "https://www.digitalocean.com/pricing/#droplet")

    def __get_lines(self, table):
        trs = self.split_data(html.fromstring(table), '//tbody//tr')
        data = []
        for x in trs:
            data.append(self.extract_data(html.fromstring(x), '//td'))
        return_data = []
        for x in data:
            if len(re.split('Popular', x[0])) == 2:
                x[0] = re.split('Popular', x[0])[1]
            x[0] = x[0].strip()
            split = re.split(" ", x[-1])
            x[-1] = split[0]
            x.append(split[2])
            return_data.append(x)
        return return_data

    def parse(self):
        # remove javascript garbage
        content = self.content.text.split("})(window,document,'script','dataLayer','GTM-KHWBBT');</script>")
        # takes what's important
        content = html.fromstring(content[1])
        title = self.extract_data(content, '//div[@class="bui-Col bui-Col-6@large"]//h2')
        machines = self.split_data(content, '//div[@class="bui-Col bui-Col-6@large"]//table')
        data = []
        data.append(self.url)
        data.append(self.extract_data(content, '//li//a[@href="#tab-droplets"]//div')[0])
        data.append({})
        for i, x in enumerate(machines):
            data[-1][re.split(" ", title[i])[0]] = self.__get_lines(x)
        return data
