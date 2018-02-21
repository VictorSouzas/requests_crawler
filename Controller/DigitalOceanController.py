# -*- coding: utf-8

import DataBase.Connect as db
import DataBase.Page as pg
import DataBase.Machine as mcn
import DataBase.Plans as pln

def save(data):
    conn = db.Connect()
    conn = conn.get_connection()
    service = data[0]
    url = data[1]
    page = pg.Page(conn)
    page_id = page.insert(url, service)
    machine_names = data[2].keys()
    machine = mcn.Machine(conn)
    data = data[2]
    for x in machine_names:
        machine_id = machine.insert(page_id, x)
        plans = pln.Plans(conn)
        for y in data[x]:
            plans.insert(machine_id, y[1], y[0], y[2], y[3], y[4], y[5])

