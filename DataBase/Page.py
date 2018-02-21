# -*- coding: utf-8 -*-

class Page:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def insert(self, site, service):
        self.cursor.execute("INSERT INTO page VALUES((SELECT max(id) FROM page) + 1, '"+site+"', '"+service+"')")
        self.conn.commit()
        return self.cursor.lastrowid

    def select_one(self, site, service):
        self.cursor.execute("SELECT * FROM page WHERE site= '%s' AND service= '%s'" % (site, service))
        one = self.cursor.fetchone()
        return one

    def select(self):
        self.cursor.execute("SELECT * FROM page")
        return self.cursor.fetchall()
