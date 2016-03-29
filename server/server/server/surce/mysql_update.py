import MySQLdb

conn=MySQLdb.connect(
                     host='127.0.0.1',
                     port=3306,
                     user='root',
                     passwd='123456',
                     db='mysql_test',
                     charset='utf8'
                     )

cursor=conn.cursor() 

sql_insert= "insert into user(userid,username) value(10,'name10')"
sql_update="update user set username='name91' where userid=9"
sql_dalete="delete from user where userid<3"
try:
    cursor.execute(sql_insert)
    print cursor.rowcount
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_dalete)
    print cursor.rowcount
    conn.commit()
except Exception as e:
    print e
    conn.rollback()

cursor.close()
conn.close()