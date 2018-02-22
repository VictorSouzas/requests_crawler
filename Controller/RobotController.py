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
    select = page.select_one(url, service)
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
            sha256 = hashlib.sha256()
            string = '%s%s%s%s%s%s' % (y[0], y[1], y[2], y[3], y[4], y[5])
            sha256.update(bytes(string, encoding='utf-8'))
            digest = sha256.hexdigest()
            select = plans.select_from_hash(digest)
            if select == None:
                plans.insert(machine_id, y[0], y[1], y[2], y[3], y[4], y[5], digest)

def read():
    conn = db.Connect()
    page = pg.Page(conn.conn)
    pages = page.select()
    return_data = list()
    for x in pages:
        data = list()
        data.append(x[1])
        data.append(x[2])
        machine = mcn.Machine(conn.conn)
        machines = machine.select_by_page_id(x[0])
        for y in machines:
            rtn_data = list()
            rtn_data.append(y[2])
            plan = pln.Plans(conn.conn)
            rtn_data.append(plan.select_by_machine_id(y[0]))
            data.append(rtn_data)
        return_data.append(data)
    return return_data

def remove():
    conn = db.Connect()
    page = pg.Page(conn.conn)
    page.delete()
    machine = mcn.Machine(conn.conn)
    machine.delete()
    plan = pln.Plans(conn.conn)
    plan.delete()
