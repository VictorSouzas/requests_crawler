# -*- coding: utf-8 -*-

class Machine:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def insert(self, id_page, name):
        self.cursor.execute("INSERT INTO machine VALUES((SELECT max(id) FROM machine) + 1, %d, '%s')" % (id_page, name))
        self.conn.commit()
        return self.cursor.lastrowid

    def select_one(self, id_page, name):
        self.cursor.execute("SELECT * FROM machine WHERE id_page= '%d' AND name= '%s'" % (id_page, name))
        one = self.cursor.fetchone()
        return one