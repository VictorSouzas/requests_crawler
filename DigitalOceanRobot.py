# -*- coding: utf-8 -*-

from lxml import html
from Robot import Robot



class DigitalOceanRobot(Robot):

    def __init__(self, url):
        Robot.__init__(self, url)

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

    def get_table(self, table):
        attr = self.extract_data(table, '//div[@class="bui-Col bui-Col-6@large"]//table//tr//th')
        tble = self.extract_data(table, '//div[@class="bui-Col bui-Col-6@large"]//table//tr/td')
        self.lst = self.split_count(tble, len(attr))
        data = []
        for i in self.lst:
            data.append(dict(zip(attr, i)))
        return data

    def parse(self):
        # remove javascript garbage
        content = self.content.text.split("id=tab-droplets data-bui-tabbed-nav-pane>")
        # takes what's important
        content = html.fromstring(content[1])
        title = self.extract_data(content, '//div[@class="bui-Col bui-Col-6@large"]//h2')
        machines = self.split_data(content, '//div[@class="bui-Col bui-Col-6@large"]')
        machines.extend(self.split_data(html.fromstring(machines[1]), '//div[@class="bui-Col bui-Col-6@large"]//div[@class="bui-u-mb--xlarge"]'))
        del machines[1]
        data = {}
        for i, x in enumerate(machines):
            table = html.fromstring(x)
            data[title[i]] = self.get_table(table)



if __name__ == '__main__':
    digital_ocean = DigitalOceanRobot()
    digital_ocean.parse()
