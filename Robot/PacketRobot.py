# -*- coding: utf-8 -*-

from lxml import html
from Robot.Robot import Robot
import re


class PacketRobot(Robot):

    def __init__(self):
        Robot.__init__(self, "https://www.packet.net/bare-metal/")

    def __get_data(self, url, bandwidth):
        robot = Robot(url)
        content = html.fromstring(robot.content.text)
        return_data = {"name": robot.extract_data(content, '//h1')[0]}
        return_data['bandwidth'] = bandwidth
        pattern = '//span[@class="price"]//span[@class="price_hourly active"]'
        return_data["hourly-price"] = robot.extract_data(content, pattern)[0]
        pattern = '//span[@class="price"]//span[@class="price_monthly inactive"]'
        return_data["monthly-price"] = robot.extract_data(content, pattern)[0]
        itens = robot.split_data(content, '//div[@id="hardware-spec"]//div[@class="ssp-btn"]')
        for x in itens:
            content = html.fromstring(x)
            pattern =  '//p[@class="p13 spc-btn-ifo absolute row-md-ct pdr-20 pdl-20"]//span'
            return_data[self.extract_data(content, '//h5')[0].lower()] = self.extract_data(content, pattern)[0]
        return return_data

    def normalize(self, data):
        return_data = {}
        for x in data:
            dt = {x['name']: [[]]}
            if 'processor' in x.keys():
                dt[x['name']][0].append(x['processor'])
            else:
                dt[x['name']][0].append(x['processors'])
            dt[x['name']][0].append(x['memory'])
            dt[x['name']][0].append(x['storage'])
            dt[x['name']][0].append(x['bandwidth'])
            dt[x['name']][0].append(x['monthly-price'])
            dt[x['name']][0].append(x['hourly-price'])
            return_data.update(dt)
        return return_data

    def parse(self):
        content = html.fromstring(self.content.text)
        pattern = '//section[@id="pricing-items"]//article[@class="pricing-item col-3"]'
        bandwidth = content.xpath('//span[@class="p7 fc-lig"]//p')[0].text_content()
        bandwidth = re.split('\\$', bandwidth)[1][0:-1]
        machines = self.split_data(content, pattern)
        url = self.extract_tag(machines, '//a', '@href')
        data = list()
        data.append(self.url)
        data.append(content.xpath('//a[@id="server-configs"]//span')[0].text_content())
        data.append([])
        for x in url:
            data[2].append(self.__get_data(x, bandwidth))
        data[2] = self.normalize(data[2])
        return data


if __name__ == '__main__':
    vultr = PacketRobot()
    vultr.parse()
