# -*- coding: utf-8 -*-

from lxml import html
from Robot import Robot
import re


class DigitalOceanRobot(Robot):

    def __init__(self, url):
        Robot.__init__(self, url)

    def get_table(self, table):
        attr = self.extract_data(table, '//tr//th')
        tds = self.extract_data(table, '//tr/td')
        lst = self.split_count(tds, len(attr))
        data = []
        for i, x in enumerate(lst):
            if len(re.split('Popular ', x[0])) > 1:
                x[0] = re.split('Popular ', x[0])[1]
            data.append(dict(zip(attr, x)))
        return data

    def parse(self):
        # remove javascript garbage
        content = self.content.text.split("id=tab-droplets data-bui-tabbed-nav-pane>")
        # takes what's important
        content = html.fromstring(content[1])
        title = self.extract_data(content, '//div[@class="bui-Col bui-Col-6@large"]//h2')
        machines = self.split_data(content, '//div[@class="bui-Col bui-Col-6@large"]//table')

        self.data = {}
        for i, x in enumerate(machines):
            table = html.fromstring(x)
            self.data[re.split(" ", title[i])[0]] = self.get_table(table)
        return self.data



if __name__ == '__main__':
    digital_ocean = DigitalOceanRobot("https://www.digitalocean.com/pricing/#droplet")
    digital_ocean.parse()
