# -*- coding: utf-8 -*-
import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='test')
cursor = conn.cursor()

cursor.execute('drop table IF  EXISTS test_python ; ')
cursor.execute('create table IF NOT EXISTS test_python (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into test_python (id, name) values (%s, %s)', ['1', 'Michael'])
rowcount = cursor.rowcount
print('---影响行数: ', rowcount)
conn.commit()

cursor = conn.cursor()

cursor.execute('select * from test_python where id = %s', ('1',))

values = cursor.fetchall()
print('---结果: ', values)
cursor.close()

conn.close()
