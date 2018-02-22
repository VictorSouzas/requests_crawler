# -*- coding: utf-8 -*-

class Plans:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def insert(self, id_machine, cpus, memory, storage, monthly_bandwidth, monthly_price, hourly_price, sha256):
        self.cursor.execute("INSERT INTO plans VALUES((SELECT max(id) FROM plans) + 1, %d, '%s',"
                            " '%s', '%s', '%s', '%s', '%s', '%s')"
                            % (id_machine, cpus.replace("'","''"), memory, storage,
                               monthly_bandwidth, monthly_price, hourly_price, sha256))
        self.conn.commit()
        return self.cursor.lastrowid

    def select_from_hash(self, hash):
        self.cursor.execute("SELECT * FROM plans WHERE hash= '%s'" % (hash))
        one = self.cursor.fetchone()
        return one

    def select_by_machine_id(self, id):
        self.cursor.execute("SELECT * FROM plans WHERE id_machine= %d" % (id))
        all_data = self.cursor.fetchall()
        return all_data

    def delete(self):
        self.cursor.execute("DELETE FROM plans")
        self.conn.commit()