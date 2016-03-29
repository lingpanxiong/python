# codeing:utf8
import sys
import MySQLdb

class transfermoney(object):
    def _init_(self,conn):
        self.conn=conn
        #定义各功能函数
        def check_account_availabel(self,accountid):
            cursor=self.conn.cursor()
            try:
                sql="select * from account where accountid=%s"%accountid
                cursor.execute(sql)
                print "account_availabel"
                rs=cursor.fetchall()
                if lens(rs) !=1:
                    raise Exception("账号%s不存在"%accountid)
            finally:
                cursor.close()

        def has_enough_money(self,accountid,money):
            cursor=self.conn.cursor()
            try:
                sql="select * from account where accountid=%s and money>s%"%(accountid,money)
                cursor.execute(sql)
                print "has_enough_money:"+sql
                rs=cursor.fetchall()
                if lens(rs) !=1:
                    raise Exception("账号%s没有足够的钱"%accountid)
            finally:
                cursor.close()
        def reduce_money(self,accountid,money):
            cursor=self.conn.cursor()
            try:
                sql="update account set money=money-%s where accountid=%s"%(money,accountid)
                cursor.execute(sql)
                print "reduce_money:"+sql
                rs=cursor.fetchall()
                if cursor.rowconut !=1:
                    raise Exception("账号%s减款失败！"%accountid)
            finally:
                cursor.close()
        def add_money(self,accountid,money):
            cursor=self.conn.cursor()
            try:
                sql="update account set money=money+%s where accountid=%s"%(money,accountid)
                cursor.execute(sql)
                print "add_money:"+sql
                rs=cursor.fetchall()
                if cursor.rowconut !=1:
                    raise Exception("账号%s增款失败！"%accountid)
            finally:
                cursor.close()

                #定义函数
    def transfer(self,source_accountid,target_accountid,money):
        try:
            self.check_account_availabel(source_accountid)
            self.check_account_availabel(source_accountid)
            self.has_enough_money(source_accountid,money)
            self.reduce_money(source_accountid,money)
            self.add_money(target_accountid,money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
        #脚本入口
if __name__=="__main__":
    source_accountid = sys.argv[1] #参数
    target_accountid = sys.argv[2]
    money = sys.argv[3]
    conn=mysqldb.connect(host='127.0.0.1',UserWarning='root',passwd='123456',port=3306,db='mysql_test',)
    tr_money= transfermoney(conn)
    try:
        tr_money.transfer(source_accountid,target_accountid,money)
    except Exception as e:
        print "something wrong!"+str(e)
    finally:
        conn.close()


