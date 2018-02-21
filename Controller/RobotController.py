# -*- coding: utf-8

import DataBase.Connect as db
import DataBase.Page as pg
import DataBase.Machine as mcn
import DataBase.Plans as pln
import hashlib

def save(data):
    conn = db.Connect()
    service = data[1]
    url = data[0]
    page = pg.Page(conn.conn)
    select = page.select_one(url,service)
    if select == None:
        page_id = page.insert(url, service)
    else:
        page_id = select[0]
    machine_names = data[2].keys()
    machine = mcn.Machine(conn.conn)
    data = data[2]
    for x in machine_names:
        select = machine.select_one(page_id, x)
        if select == None:
            machine_id = machine.insert(page_id, x)
        else:
            machine_id = select[0]
        plans = pln.Plans(conn.conn)
        for y in data[x]:
            hash = hashlib.sha256("%s%s%s%s%s%s" % (y[1], y[0], y[2], y[3], y[4], y[5])).hexdigest()
            select = plans.select_from_hash(hash)
            if select == None:
                plans.insert(machine_id, y[1], y[0], y[2], y[3], y[4], y[5], hash)

