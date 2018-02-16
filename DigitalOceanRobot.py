# -*- coding: utf-8 -*-

import requests
from lxml import html
from Machinne import Machine


class DigitalOceanRobot:

    def __init__(self):
        self.url = "https://www.digitalocean.com/pricing/"
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"}
        self.content = requests.get(url=self.url, headers=self.headers, timeout=2.5)

    def __split_data(self, content, pattern, limit=False):
        table = []

        for i in content.xpath(pattern):
            table.append(html.tostring(i))
        return table

    def __extract_data(self, data, pattern):

        processed_data = []
        for i in data.xpath(pattern):
            processed_data.append(i)
        return processed_data

    def parse(self):
        # remove javascript garbage
        content = self.content.text.split("id=tab-droplets data-bui-tabbed-nav-pane>")
        # takes what's important
        content = html.fromstring(content[1])
        machines = self.__split_data(content, '//div[@class="bui-Col bui-Col-6@large"]')

        machines += self.__split_data(html.fromstring(machines[1]), '//div[@class="bui-Col bui-Col-6@large"]')
        del machines[1]
        table = html.fromstring(machines[0])
        attributes = self.__extract_data(table, '//div[@class="bui-Col bui-Col-6@large"]//table//tr//th')

        table_lines = self.__split_data(table, '//div[@class="bui-Col bui-Col-6@large"]//table//tr//td')
        print(table_lines)


if __name__ == '__main__':
    digital_ocean = DigitalOceanRobot()
    digital_ocean.parse()
