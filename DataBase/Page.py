# -*- coding: utf-8 -*-

class Page:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, site, service):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO page VALUES((SELECT max(id) FROM page) + 1, \"site\", \"service\")")
        self.conn.commit()
        return cursor.lastrowid

