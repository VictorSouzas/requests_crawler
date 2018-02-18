from lxml import html
from Robot import Robot


class PacketRobot(Robot):
    def __init__(self):
        Robot.__init__(self, "https://www.packet.net/bare-metal/")

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

    def split_data(self, content, pattern):
        table = []
        for i, x in enumerate(content.xpath(pattern)):
            table.append(html.tostring(x))
        return table

    def parse(self):
        content = html.fromstring(self.content.text)
        pattern = '//section[@id="pricing-items"]//article[@class="pricing-item col-3"]'
        machines = self.split_data(content, pattern)
        print(machines)



if __name__ == '__main__':
    vultr = PacketRobot()
    vultr.parse()
