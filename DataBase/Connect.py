# -*- coding: utf-8 -*-

import sqlite3

class Connect:
    def __init__(self):
        self.conn = sqlite3.connect('Robots.db')

    def __del__(self):
        self.conn.close()
