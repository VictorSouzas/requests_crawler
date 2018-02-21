# -*- coding: utf-8 -*-

class Machine:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, id_page, name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO machine VALUES((SELECT max(id) FROM machine) + 1, '%d', '%s')" % (id_page, name))
        self.conn.commit()
        return cursor.lastrowid