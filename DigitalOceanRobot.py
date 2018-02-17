# -*- coding: utf-8 -*-

import requests
from lxml import html
from Htmlhandler import Htmlhandler


class DigitalOceanRobot:

    def __init__(self):
        self.url = "https://www.digitalocean.com/pricing/"
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"}
        self.content = requests.get(url=self.url, headers=self.headers, timeout=2.5)
        self.html_handler = Htmlhandler()

    def get_table(self, table):
        attr = self.html_handler.extract_data(table, '//div[@class="bui-Col bui-Col-6@large"]//table//tr//th')
        tble = self.html_handler.extract_data(table, '//div[@class="bui-Col bui-Col-6@large"]//table//tr/td')
        self.lst = self.html_handler.split_count(tble, len(attr))
        data = []
        for i in self.lst:
            data.append(dict(zip(attr, i)))
        return data

    def parse(self):
        # remove javascript garbage
        content = self.content.text.split("id=tab-droplets data-bui-tabbed-nav-pane>")
        # takes what's important
        content = html.fromstring(content[1])
        machines = self.html_handler.split_data(content, '//div[@class="bui-Col bui-Col-6@large"]')
        machines.extend(self.html_handler.split_data(html.fromstring(machines[1]), '//div[@class="bui-Col bui-Col-6@large"]//div[@class="bui-u-mb--xlarge"]'))
        print(machines)
        # data = {}
        # for x in machines:
        #     table = html.fromstring(x)
        #     name = table.xpath('//div[@class="bui-Col bui-Col-6@large"]//h2')
        #     data[name[0].text_content()] = self.get_table(table)
        # print(data)



if __name__ == '__main__':
    digital_ocean = DigitalOceanRobot()
    digital_ocean.parse()
