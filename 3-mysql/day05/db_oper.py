# db_oper.py
# pymysql数据库访问类
import db_conf
import pymysql

class DBOper:
    def __init__(self): #构造方法
        self.host = db_conf.host
        self.user = db_conf.user
        self.password = db_conf.password
        self.dbname = db_conf.dbname
        self.db_conn = None   #数据库连接对象

    def open_conn(self): #连接数据库
        try:
            self.db_conn = pymysql.connect(self.host, self.user, self.password, self.dbname)
        except Exception as e:
            print("连接数据库错误")
            print(e)
        else:
            print("连接数据库成功")    

    def close_conn(self): #关闭数据库
        try:
            self.db_conn.close()
        except Exception as e:
            print("关闭数据库错误")
            print(e)
        else:
            print("关闭数据库成功") 

    def do_query(self, sql): #查询
        try:
            cursor = self.db_conn.cursor()  #获取游标
            if not sql:
                print("SQL语句对象不合法")
                return None
            if sql == "":
                print("SQL语句不能为空")
                return None
            
            #执行查询
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close() #关闭游标
            return result
        except Exception as e:
            print("执行SQL语句错误")
            print(e)
            return None

    def do_update(self, sql):#执行增删改
        try:
            cursor = self.db_conn.cursor()  #获取游标
            if not sql:
                print("SQL语句对象不合法")
                return None
            if sql == "":
                print("SQL语句不能为空")
                return None
            
            #执行查询
            result = cursor.execute(sql)
            self.db_conn.commit()
            cursor.close()  #关闭游标
            return result
        except Exception as e:
            self.db_conn.rollback()
            print("执行SQL语句错误")
            print(e)
            return None

if __name__ == "__main__":
    dboper = DBOper()
    dboper.open_conn()
    ret = dboper.do_query("select * from acct")
    for x in ret:
        print(x)

    ret = dboper.do_update("update acct set balance = balance + 100 where acct_no = '622345000001'")

    print(ret)