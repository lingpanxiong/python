#encoding:utf-8

import MySQLdb as mdb
import sys

conn = mdb.connect(
	
	host = '127.0.0.1',
	port = 3306,
	user = 'root',
	passwd = '123456',
	db = 'mysql_test',#链接的数据库名称
	charset = 'utf8',#数据库编码

	)
cursor = conn.cursor(mdb.cursors.DictCursor) #return a dict 
'''
cursor = conn.cursor() #return databash
#cursor.execute('create table if not exists \
#writers(id int primary key auto_increment,name varchar(25))')
cursor.execute('insert into writers(id,name) value(04,"nice")')
'''
cursor.execute('select * from writers')

#以上为数据库查询返回，以下为数据处理

'''
ax=cursor.fetchall()
for row in ax:
	print row
conn.commit()
'''
row = cursor.fetchall()#fetchall 全部，fetchone 一行，fetchmany(%d) d rows
print type (row)
for rows in row:
	print "%s %s" % (rows['id'],rows['name']) # if dict rows["%s"] else row [%d]

desc = cursor.description #获取字段名&信息,return tuple

conn.rollback()#request no change
cursor.close()
conn.close()