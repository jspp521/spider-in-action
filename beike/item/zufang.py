# coding=utf-8
# 二手房信息的数据结构


class ZuFang(object):
    def __init__(self, district, area, xiaoqu, layout, size, price):
        self.district = district
        self.area = area
        self.xiaoqu = xiaoqu
        self.layout = layout
        self.size = size
        self.price = price

    def text(self):
        return self.district + "," + \
                self.area + "," + \
                self.xiaoqu + "," + \
                self.layout + "," + \
                self.size + "," + \
                self.price
