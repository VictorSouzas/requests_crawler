# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('Robots.db')
cursor = conn.cursor()
query = ["CREATE TABLE IF NOT EXISTS page (id INTEGER PRIMARY KEY, site VARCHAR, service VARCHAR)"]
new_query = "CREATE TABLE IF NOT EXISTS machine " \
            "(id INTEGER PRIMARY KEY, id_page INTEGER," \
            " name VARCHAR,  FOREIGN KEY (id_page) REFERENCES page(id))"

query.append(new_query)
new_query = "CREATE TABLE IF NOT EXISTS plans" \
            "(id INTEGER PRIMARY KEY, id_machine INTEGER," \
            " cpus VARCHAR, memory VARCHAR, storage VARCHAR," \
            " monthly_bandwidth VARCHAR, monthly_price VARCHAR," \
            " hourly_price VARCHAR, hash VARCHAR, FOREIGN KEY (id_machine) REFERENCES machine(id))"
query.append(new_query)
for x in query:
    cursor.execute(x)
conn.commit()
conn.close()