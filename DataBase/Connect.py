# -*- coding: utf-8 -*-

import sqlite3

class Connect:
    def __make_connection(self):
        self.conn = sqlite3.connect('Robots.db')
    def get_connection(self):
        self.__make_connection()
        return self.conn