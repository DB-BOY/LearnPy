# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
e = cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
e = cursor.execute('insert into user values(1,\"sssss\")')
print(e)
rowcount = cursor.rowcount
print('rowcount: ', rowcount)
cursor.close()
conn.commit()
conn.close()

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user where id=?', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
