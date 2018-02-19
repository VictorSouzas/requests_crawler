# -*- coding: utf-8 -*-

class Plans:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, id_machine, cpus, memory, storage, monthly_bandwidth, monthly_price, hourly_price):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO plans VALUES((SELECT max(id) FROM plans) + 1, \"id_machine\", \"cpus\", \"memory\", \"storage\", \"monthly_bandwidth\", \"monthly_price\", \"hourly_price\")")
        self.conn.commit()
        return cursor.lastrowid