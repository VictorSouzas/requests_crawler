# -*- coding: utf-8 -*-

from lxml import html
from Robot import Robot
import re


class DigitalOceanRobot(Robot):

    def __init__(self, url):
        Robot.__init__(self, url)

    def get_lines(self, table):
        attr = self.extract_data(html.fromstring(table), '//tr//th')
        attr[-1] = "monthly-price"
        attr.append("hourly-price")
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
            return_data.append(dict(zip(attr, x)))
        return return_data

    def parse(self):
        # remove javascript garbage
        content = self.content.text.split("id=tab-droplets data-bui-tabbed-nav-pane>")
        # takes what's important
        content = html.fromstring(content[1])
        title = self.extract_data(content, '//div[@class="bui-Col bui-Col-6@large"]//h2')
        machines = self.split_data(content, '//div[@class="bui-Col bui-Col-6@large"]//table')

        self.data = {}
        for i, x in enumerate(machines):
            self.data[re.split(" ", title[i])[0]] = self.get_lines(x)
        return self.data



if __name__ == '__main__':
    digital_ocean = DigitalOceanRobot("https://www.digitalocean.com/pricing/#droplet")
    digital_ocean.parse()
