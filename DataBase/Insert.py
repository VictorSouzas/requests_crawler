# -*- coding: utf-8 -*-

from DataBase.Connect import Connect


class Insert(Connect):
    def __init__(self):
        Connect.__init__(self)
        self.__table = ""

    def set_table(self, table):
        self.__table = table.strip()



    def __del__(self):
        Connect.__del__(self)
